#include <string.h>
#include <math.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/semphr.h"
#include "driver/i2c_master.h"
#include "driver/gpio.h"
#include "esp_timer.h"
#include "esp_log.h"
#include "robot.h"
#include "pins.h"
static i2c_master_dev_handle_t dev;static SemaphoreHandle_t lock;static imu_t state;static uint8_t seq[6];
static int16_t s16(const uint8_t *p){return (int16_t)(p[0]|p[1]<<8);}
static void enable_report(uint8_t report){
 uint8_t p[21]={21,0,2,0,0xfd,report};p[3]=seq[2]++;
 uint32_t us=10000;memcpy(p+9,&us,4);
 if(i2c_master_transmit(dev,p,sizeof(p),50)!=ESP_OK)ESP_LOGW("imu","report enable failed");
}
static void task(void *arg){(void)arg;
 vTaskDelay(pdMS_TO_TICKS(500));enable_report(5);enable_report(2);
 for(;;){
  if(gpio_get_level(IMU_INT)){vTaskDelay(pdMS_TO_TICKS(2));continue;}
  uint8_t h[4],p[512];
  if(i2c_master_receive(dev,h,4,20)!=ESP_OK){vTaskDelay(pdMS_TO_TICKS(10));continue;}
  unsigned len=(h[0]|h[1]<<8)&0x7fff;
  if(len<4||len>sizeof(p)){vTaskDelay(pdMS_TO_TICKS(10));continue;}
  // BNO08x repeats the four-byte SHTP header on each I2C read.
  if(i2c_master_receive(dev,p,len,20)!=ESP_OK)continue;
  if((p[1]&0x80)||p[2]!=3||len<9||p[4]!=0xfb)continue;
  unsigned k=9;
  xSemaphoreTake(lock,portMAX_DELAY);
  while(k+4<=len){
   if(p[k]==5&&k+14<=len){
    if((p[k+2]&3)>=1){for(int j=0;j<4;j++)state.quat[j]=s16(p+k+4+2*j)/16384.f;state.quat_time=esp_timer_get_time();}k+=14;
   }else if(p[k]==2&&k+10<=len){
    if((p[k+2]&3)>=1){for(int j=0;j<3;j++)state.gyro[j]=s16(p+k+4+2*j)/512.f;state.gyro_time=esp_timer_get_time();}k+=10;
   }else break;
  }
  xSemaphoreGive(lock);
 }
}
void imu_start(void){
 lock=xSemaphoreCreateMutex();
 gpio_config_t out={.pin_bit_mask=1ULL<<IMU_RST,.mode=GPIO_MODE_OUTPUT};ESP_ERROR_CHECK(gpio_config(&out));
 gpio_set_level(IMU_RST,0);vTaskDelay(pdMS_TO_TICKS(10));gpio_set_level(IMU_RST,1);
 gpio_config_t in={.pin_bit_mask=1ULL<<IMU_INT,.mode=GPIO_MODE_INPUT,.pull_up_en=GPIO_PULLUP_ENABLE};ESP_ERROR_CHECK(gpio_config(&in));
 i2c_master_bus_config_t b={.i2c_port=0,.sda_io_num=IMU_SDA,.scl_io_num=IMU_SCL,.clk_source=I2C_CLK_SRC_DEFAULT,.glitch_ignore_cnt=7,.flags.enable_internal_pullup=true};
 i2c_master_bus_handle_t bus;ESP_ERROR_CHECK(i2c_new_master_bus(&b,&bus));
 i2c_device_config_t d={.dev_addr_length=I2C_ADDR_BIT_LEN_7,.device_address=0x4a,.scl_speed_hz=400000};ESP_ERROR_CHECK(i2c_master_bus_add_device(bus,&d,&dev));
 xTaskCreate(task,"bno085",4096,NULL,5,NULL);
}
bool imu_snapshot(imu_t *out){xSemaphoreTake(lock,portMAX_DELAY);*out=state;xSemaphoreGive(lock);
 int64_t now=esp_timer_get_time();return out->quat_time&&out->gyro_time&&now-out->quat_time<100000&&now-out->gyro_time<100000;}
