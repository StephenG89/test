import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Set the GPIO pin you are using
pwm_pin = 18

GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 440)  # Initial frequency (adjust as needed)

# Define frequencies for "Mary Had a Little Lamb"
song_frequencies = [
    523, 493, 440, 493, 523, 523, 523,
    493, 493, 493, 523, 523, 523,
    523, 493, 440, 493, 523, 523, 523,
    523, 493, 493, 523, 493, 440
]

try:
    for frequency in song_frequencies:
        pwm.ChangeFrequency(frequency)
        pwm.start(50)  # 50% duty cycle (adjust as needed)
        time.sleep(0.5)  # Adjust the duration of each note as needed
        pwm.stop()
        time.sleep(0.1)  # Add a short pause between notes

finally:
    GPIO.cleanup()
