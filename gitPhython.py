
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Set the GPIO pin you are using
pwm_pin = 18

GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 640)  # 440 Hz frequency (adjust as needed)

try:
    pwm.start(50)  # 50% duty cycle (adjust as needed)

    # Run for a certain duration (e.g., 5 seconds)
    time.sleep(5)

finally:
    pwm.stop()
    GPIO.cleanup()
