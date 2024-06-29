import RPi.GPIO as GPIO
from time import sleep
import cv2
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder

class PIR():
    def __init__(self, pin:int):
        self.pin = pin
        self.val = GPIO.LOW
        GPIO.setup(pin, GPIO.IN)
        
    def setData(self):
        self.val = GPIO.input(self.pin)
    
    def getData(self)->int:
        return self.val
        
class Camera():
    def __init__(self):
        self.picam2 = Picamera2()
    
    def take_video(self):
        video_config = self.picam2.create_video_configuration()
        self.picam2.configure(video_config)
        
        encoder = H264Encoder(10000000)
        
        self.picam2.start_recording(encoder, 'test.h264')
        sleep(5)
        self.picam2.stop_recording()
        
        
def setup():
    GPIO.setmode(GPIO.BOARD)

def main():
    setup()
    c = Camera()
    c.take_video()
    
    
    """ p = PIR(11)
    while(1):
        p.setData()
        print(p.getData()) """

if __name__ == "__main__":
    main()
    
    