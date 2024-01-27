import pygame
import RPi.GPIO as GPIO
import time

# Set the path to your MP3 file
file_path = "test/Prelude.mp3"

# Set the GPIO pin for the button
button_pin = 18  # Replace with the actual GPIO pin number

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pygame.init()
pygame.mixer.init()

def play_audio():
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_audio():
    pygame.mixer.music.stop()

try:
    while True:
        button_state = GPIO.input(button_pin)
        if button_state == GPIO.LOW:  # Button pressed
            play_audio()
            time.sleep(1)  # Debounce delay to prevent multiple triggers

except KeyboardInterrupt:
    pass

finally:
    stop_audio()
    GPIO.cleanup()
    pygame.quit()
