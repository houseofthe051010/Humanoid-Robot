#include <string.h>
#include <math.h>
#include "freertos/FreeRTOS.h"
#include "freertos/queue.h"
#include "freertos/semphr.h"
#include "esp_timer.h"
#include "esp_check.h"
#include "esp_twai.h"
#include "esp_twai_onchip.h"
#include "robot.h"
#include "pins.h"
// Explicit prototype CAN IDs; commission each axis to these IDs before use.
const motor_t motors[NM]={
 {0,1,7,0},{0,2,6,0},{0,3,5,0},{0,4,8,0},{0,5,3,1},{0,6,4,1},
 {1,1,21,0},{1,2,20,0},{1,3,19,0},{1,4,22,0},{1,5,17,1},{1,6,18,1},
 {2,1,9,0},{2,2,10,0},{2,3,11,0},{2,4,12,0},{2,5,1,0},{2,6,2,0},{2,7,0,0}};
typedef struct {int bus;uint32_t id;uint8_t n,data[8];int64_t time;} packet_t;
typedef struct {twai_node_handle_t node;SemaphoreHandle_t done;twai_frame_t tx;uint8_t data[8];bool failed;volatile bool tx_ok;} bus_t;
static bus_t buses[3];static QueueHandle_t rxq;static feedback_t fb[NM];
static bool received(twai_node_handle_t n,const twai_rx_done_event_data_t *e,void *ctx){
 (void)e;packet_t p={.bus=(int)(intptr_t)ctx,.time=esp_timer_get_time()};
 twai_frame_t f={.buffer=p.data,.buffer_len=8};BaseType_t wake=pdFALSE;
 if(twai_node_receive_from_isr(n,&f)==ESP_OK && !f.header.ide && !f.header.rtr){
  p.id=f.header.id;p.n=f.header.dlc;if(p.n<=8)xQueueSendFromISR(rxq,&p,&wake);
 }return wake==pdTRUE;
}
static bool sent(twai_node_handle_t n,const twai_tx_done_event_data_t *e,void *ctx){
 (void)n;BaseType_t wake=pdFALSE;buses[(int)(intptr_t)ctx].tx_ok=e->is_tx_success;
 xSemaphoreGiveFromISR(buses[(int)(intptr_t)ctx].done,&wake);return wake==pdTRUE;
}
esp_err_t can_start(void){
 rxq=xQueueCreate(128,sizeof(packet_t));if(!rxq)return ESP_ERR_NO_MEM;
 const int tx[]={CAN_A_TX,CAN_B_TX,CAN_C_TX},rx[]={CAN_A_RX,CAN_B_RX,CAN_C_RX};
 for(int i=0;i<3;i++){
  buses[i].done=xSemaphoreCreateBinary();if(!buses[i].done)return ESP_ERR_NO_MEM;
  twai_onchip_node_config_t c={.io_cfg={.tx=tx[i],.rx=rx[i],.quanta_clk_out=-1,.bus_off_indicator=-1},
    .bit_timing={.bitrate=500000},.tx_queue_depth=1,.fail_retry_cnt=1};
  ESP_RETURN_ON_ERROR(twai_new_node_onchip(&c,&buses[i].node),"can","create");
  twai_event_callbacks_t cb={.on_rx_done=received,.on_tx_done=sent};
  ESP_RETURN_ON_ERROR(twai_node_register_event_callbacks(buses[i].node,&cb,(void*)(intptr_t)i),"can","callbacks");
  ESP_RETURN_ON_ERROR(twai_node_enable(buses[i].node),"can","enable");
 }return ESP_OK;
}
// Persistent buffers remain alive until the TX callback. A timeout latches the bus offline.
static esp_err_t send(unsigned index,unsigned cmd,const void *data,unsigned len){
 if(index>=NM||len>8)return ESP_ERR_INVALID_ARG;
 const motor_t *m=&motors[index];bus_t *b=&buses[m->bus];if(b->failed)return ESP_ERR_INVALID_STATE;
 memset(b->data,0,8);if(len)memcpy(b->data,data,len);
 b->tx=(twai_frame_t){.header={.id=(m->node<<5)|cmd,.dlc=len},.buffer=b->data,.buffer_len=len};
 xSemaphoreTake(b->done,0);esp_err_t err=twai_node_transmit(b->node,&b->tx,0);
 if(err!=ESP_OK)return err;
 if(!xSemaphoreTake(b->done,pdMS_TO_TICKS(5))){b->failed=true;twai_node_disable(b->node);return ESP_ERR_TIMEOUT;}
 return b->tx_ok?ESP_OK:ESP_FAIL;
}
void can_poll(void){packet_t p;
 while(xQueueReceive(rxq,&p,0)==pdTRUE){
  for(unsigned i=0;i<NM;i++)if(motors[i].bus==p.bus&&motors[i].node==(p.id>>5)){
   if((p.id&31)==9&&p.n==8){float v[2];memcpy(v,p.data,8);
    if(isfinite(v[0])&&isfinite(v[1]))fb[i]=(feedback_t){v[0],v[1],p.time,true};}
   // Heartbeat errors invalidate that motor's feedback immediately.
   if((p.id&31)==1&&p.n>=4){uint32_t error;memcpy(&error,p.data,4);if(error)fb[i].valid=false;}
  }
 }
}
bool can_feedback(unsigned i,feedback_t *f){if(i>=NM)return false;*f=fb[i];return f->valid;}
esp_err_t can_position(unsigned i,float turns){if(!isfinite(turns))return ESP_ERR_INVALID_ARG;uint8_t data[8]={0};memcpy(data,&turns,4);return send(i,12,data,8);}
static esp_err_t state_all(uint32_t state){esp_err_t first=ESP_OK;for(unsigned i=0;i<NM;i++){esp_err_t e=send(i,7,&state,4);if(first==ESP_OK)first=e;}return first;}
esp_err_t can_idle_all(void){return state_all(1);}
esp_err_t can_enable_all(void){return state_all(8);}
