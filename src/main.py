import RPi.GPIO as GPIO
from time import sleep

class PIR():
    def __init__(self, pin:int):
        self.pin = pin
        self.val = GPIO.LOW
        GPIO.setup(pin, GPIO.IN)
        
    def setData(self):
        self.val = GPIO.input(self.pin)
    
    def getData(self)->int:
        return self.val
        
    
def setup():
    GPIO.setmode(GPIO.BOARD)

def main():
    setup()
    p = PIR(11)
    while(1):
        p.setData()
        print(p.getData())

if __name__ == "__main__":
    main()
    
    