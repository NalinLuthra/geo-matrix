import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(16, GPIO.OUT)

while True:
        if GPIO.input(10) == GPIO.HIGH:
                print("Button is pressed!")
                GPIO.output(16,1)
        if GPIO.input(10) == GPIO.LOW:
                print("Button is released!")
                GPIO.output(16,0)

