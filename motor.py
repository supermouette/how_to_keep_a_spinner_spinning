import time
from RPi import GPIO
import wiringpi


class MotorSoftPWM:
    """ enclose GPIO, to use servomoteur easily, deprecated"""


    HIGH = 90
    LOW = 10

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.pwm_gpio = 12
        self.frequence = 50
        GPIO.setup(self.pwm_gpio, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_gpio, self.frequence)
        self.pwm.start(self.angle_to_percent(MotorSoftPWM.LOW))
        self.high = False

    @classmethod
    def angle_to_percent(cls, angle):
        if angle > 180 or angle < 0:
            raise ValueError('must be between 0 and 180')
        start = 4
        end = 12.5
        ratio = (end - start)/180
        return start + angle*ratio

    def swing(self):
        if self.high:
            angle = MotorSoftPWM.LOW
        else:
            angle = MotorSoftPWM.HIGH
        self.pwm.ChangeDutyCycle(self.angle_to_percent(angle))
        self.high = not self.high
        time.sleep(0.5)

    def close(self):
        self.pwm.stop()
        GPIO.cleanup()


class MotorHardPWM:
    """ enclose wiringpi, to use servomoteur easily, deprecated"""

    def __init__(self, low=45, high=75):
        self.low = low
        self.high = high
        self.pin = 32
        self.is_high = False
        wiringpi.wiringPiSetupPhys()
        wiringpi.pinMode(self.pin, 2)
        wiringpi.pwmSetMode(0)
        wiringpi.pwmSetRange(1024)
        wiringpi.pwmSetClock(375)
        wiringpi.pwmWrite(self.pin, self.low)

    def swing(self):
        if self.is_high:
            angle = self.low
        else:
            angle = self.high
        wiringpi.pwmWrite(self.pin, angle)
        self.is_high = not self.is_high
        time.sleep(0.5)


if __name__ == "__main__":
    m = MotorHardPWM()
    time.sleep(1)
    m.swing()
    time.sleep(1)
    m.swing()
