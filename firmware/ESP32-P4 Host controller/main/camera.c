#include <stdatomic.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_log.h"
#include "esp_heap_caps.h"
#include "usb/usb_host.h"
#include "usb/uvc_host.h"
#include "robot.h"
static atomic_uint frames;static atomic_bool disconnected;
static bool frame(const uvc_host_frame_t *f,void *ctx){(void)ctx;
 // Count completed, nonempty UVC frames only. No depth decoding or vision processing.
 if(f&&f->data_len>0){atomic_fetch_add(&frames,1);}
 return true;}
static void event(const uvc_host_stream_event_data_t *e,void *ctx){(void)ctx;
 if(e->type==UVC_HOST_DEVICE_DISCONNECTED)atomic_store(&disconnected,true);
 if(e->type==UVC_HOST_TRANSFER_ERROR)ESP_LOGW("camera","UVC transfer error");}
static void host(void *arg){(void)arg;for(;;){uint32_t flags;usb_host_lib_handle_events(portMAX_DELAY,&flags);}}
static void capture(void *arg){(void)arg;
 uvc_host_stream_config_t c={.event_cb=event,.frame_cb=frame,
  .usb={.vid=UVC_HOST_ANY_VID,.pid=UVC_HOST_ANY_PID,.uvc_stream_index=0},
  .vs_format={.h_res=320,.v_res=240,.fps=15,.format=UVC_VS_FORMAT_MJPEG},
  .advanced={.number_of_frame_buffers=2,.number_of_urbs=3,.urb_size=10*1024,.frame_heap_caps=MALLOC_CAP_SPIRAM}};
 for(;;){
  uvc_host_stream_hdl_t stream=NULL;atomic_store(&disconnected,false);
  esp_err_t e=uvc_host_stream_open(&c,pdMS_TO_TICKS(5000),&stream);
  if(e!=ESP_OK){ESP_LOGW("camera","No matching UVC MJPEG stream (%s); camera may require vendor protocol",esp_err_to_name(e));vTaskDelay(pdMS_TO_TICKS(5000));continue;}
  e=uvc_host_stream_start(stream);
  if(e==ESP_OK)while(!atomic_load(&disconnected))vTaskDelay(pdMS_TO_TICKS(100));
  uvc_host_stream_stop(stream);uvc_host_stream_close(stream);vTaskDelay(pdMS_TO_TICKS(1000));
 }
}
void camera_start(void){usb_host_config_t h={.skip_phy_setup=false,.intr_flags=0};
 ESP_ERROR_CHECK(usb_host_install(&h));xTaskCreate(host,"usb_host",4096,NULL,8,NULL);
 uvc_host_driver_config_t d={.driver_task_stack_size=6144,.driver_task_priority=6,.xCoreID=tskNO_AFFINITY,.create_background_task=true};
 ESP_ERROR_CHECK(uvc_host_install(&d));xTaskCreate(capture,"camera",6144,NULL,4,NULL);}
unsigned camera_frames(void){return atomic_load(&frames);}
