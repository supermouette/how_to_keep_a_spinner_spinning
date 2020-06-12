from motor import MotorHardPWM
from camera import Camera
from image_processing import spinner_detect
import time
c = Camera(Camera.RESOLUTION_LOW)
m = MotorHardPWM()

while True:
    img = c.capture_img_array()
    if spinner_detect(img) is not None:
        m.swing()
    time.sleep(0.2)
