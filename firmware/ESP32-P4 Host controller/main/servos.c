#include <math.h>
#include <string.h>
#include "driver/uart.h"
#include "driver/gpio.h"
#include "driver/ledc.h"
#include "esp_timer.h"
#include "esp_log.h"
#include "robot.h"
#include "pins.h"
static feedback_t feedback[7];
static esp_err_t packet(int port,uint8_t id,uint8_t ins,const uint8_t *args,int n){
 uint8_t p[40]={255,255,id,n+2,ins};if(n>32)return ESP_ERR_INVALID_ARG;
 unsigned sum=id+n+2+ins;for(int i=0;i<n;i++){p[5+i]=args[i];sum+=args[i];}p[5+n]=~sum;
 uart_flush_input(port);int sent=uart_write_bytes(port,p,n+6);
 if(sent!=n+6){return ESP_FAIL;}
 return uart_wait_tx_done(port,pdMS_TO_TICKS(5));
}
void servos_start(void){
 const int pins[]={STS_PIN,HAND_PIN};
 for(int i=0;i<2;i++){
  uart_port_t port=i+1;uart_config_t c={.baud_rate=1000000,.data_bits=UART_DATA_8_BITS,
   .parity=UART_PARITY_DISABLE,.stop_bits=UART_STOP_BITS_1,.flow_ctrl=UART_HW_FLOWCTRL_DISABLE,.source_clk=UART_SCLK_DEFAULT};
  ESP_ERROR_CHECK(uart_driver_install(port,512,0,0,NULL,0));ESP_ERROR_CHECK(uart_param_config(port,&c));
  ESP_ERROR_CHECK(uart_set_pin(port,pins[i],pins[i],UART_PIN_NO_CHANGE,UART_PIN_NO_CHANGE));
  ESP_ERROR_CHECK(gpio_set_direction(pins[i],GPIO_MODE_INPUT_OUTPUT_OD));
 }
 ledc_timer_config_t t={.speed_mode=LEDC_LOW_SPEED_MODE,.duty_resolution=LEDC_TIMER_14_BIT,.timer_num=LEDC_TIMER_0,.freq_hz=50,.clk_cfg=LEDC_AUTO_CLK};
 ESP_ERROR_CHECK(ledc_timer_config(&t));
 const int pwm[]={ELBOW_L_PIN,ELBOW_R_PIN};
 for(int i=0;i<2;i++){ledc_channel_config_t c={.gpio_num=pwm[i],.speed_mode=LEDC_LOW_SPEED_MODE,.channel=i,.timer_sel=LEDC_TIMER_0,.duty=0};ESP_ERROR_CHECK(ledc_channel_config(&c));}
}
esp_err_t servo_goal(bool hands,unsigned id,unsigned ticks){
 if(!id||id>(hands?16:6)||ticks>(hands?1023:4095))return ESP_ERR_INVALID_ARG;
 uint8_t a[7]={42};a[1]=hands?(ticks>>8):ticks;a[2]=hands?ticks:(ticks>>8);
 return packet(hands?2:1,id,3,a,7); // goal position, time=0, speed=0; verify model table.
}
void elbow_goal(unsigned side,unsigned us){if(side>1||us<500||us>2500)return;
 ledc_set_duty(LEDC_LOW_SPEED_MODE,side,(uint32_t)((uint64_t)us*16384/20000));ledc_update_duty(LEDC_LOW_SPEED_MODE,side);}
// Sequential read polling: discard echo/read instructions, accept only checked status packets.
void servos_poll(void){
 static unsigned next=1;uint8_t a[]={56,4};packet(1,next,2,a,2);
 uint8_t buf[80];int n=uart_read_bytes(1,buf,sizeof(buf),pdMS_TO_TICKS(2));
 for(int k=0;k+10<=n;k++)if(buf[k]==255&&buf[k+1]==255&&buf[k+2]==next&&buf[k+3]==6&&buf[k+4]==0){
  unsigned sum=0;for(int j=2;j<10;j++)sum+=buf[k+j];if((sum&255)!=255)continue;
  int pos=buf[k+5]|(buf[k+6]<<8),vel=buf[k+7]|(buf[k+8]<<8);
  feedback[next]=(feedback_t){pos,(vel&32768)?-(vel&32767):vel,esp_timer_get_time(),true};
 }
 next=next%6+1;
}
bool servo_feedback(unsigned id,feedback_t *out){if(id<1||id>6)return false;*out=feedback[id];return out->valid;}
