from picamera import PiCamera
import numpy as np


class Camera():
    """ enclose PiCamera"""

    RESOLUTION_HIGH = 1
    RESOLUTION_LOW = 0

    def __init__(self, resolution=1):
        self.camera = PiCamera()
        
        if resolution == Camera.RESOLUTION_HIGH:
            self.camera.resolution = (1920, 1080)
        else:
            self.camera.resolution = (640, 480)

    def capture_img_file(self, path):
        self.camera.capture(path)

    def capture_img_array(self):
        output = np.empty((self.camera.resolution[1], self.camera.resolution[0], 3), dtype=np.uint8)
        self.camera.capture(output, 'rgb')
        return output


if __name__ == '__main__':
    c = Camera(Camera.RESOLUTION_LOW)
    img = c.capture_img_array()
    print(img.shape)
    c.capture_img_file('img0.png')
    c.capture_img_file('img1.png')
