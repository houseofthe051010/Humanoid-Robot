idf_component_register(SRCS "main.c" "can_motors.c" "servos.c" "imu.c" "camera.c" "policy.c"
 INCLUDE_DIRS "." REQUIRES esp_driver_twai esp_driver_uart esp_driver_i2c esp_driver_gpio esp_driver_ledc esp_timer usb usb_host_uvc
 EMBED_FILES "actor.bin")
