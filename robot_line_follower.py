import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
#Mendefinisikan pin output
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
#Mendefinisikan pin input
GPIO.setup(2, GPIO.IN)# sensor kiri
GPIO.setup(3, GPIO.IN)# sensor kanan
while True:
    i=GPIO.input(2)
    j=GPIO.input(3)
    # Kondisi HIGH = hitam, dan LOW = putih
    if i==1 and j==0:
        GPIO.output(14,1)  
        GPIO.output(15,0) 
        GPIO.output(23,0) 
        GPIO.output(24,1)
        print('BELOK KIRI')
        
    elif i==0 and j==1:
        GPIO.output(14,0) 
        GPIO.output(15,1)
        GPIO.output(23,1)  
        GPIO.output(24,0)
        print('BELOK KANAN')
        
    elif i==1 and j==1:
        GPIO.output(14,1)  
        GPIO.output(15,0)  
        GPIO.output(23,1) 
        GPIO.output(24,0)
        print('MUNDUR')
        
    else:
        GPIO.output(14,0)  
        GPIO.output(15,1)  
        GPIO.output(23,0)  
        GPIO.output(24,1)
        print('MAJU')
