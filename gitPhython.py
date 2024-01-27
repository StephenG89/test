import pygame
import RPi.GPIO as GPIO
import time

# Set the path to your MP3 file
file_path = "gitRepos/test/Prelude.mp3"

# Set the GPIO pin for controlling audio
audio_control_pin = 18  # Replace with the actual GPIO pin number

GPIO.setmode(GPIO.BCM)
GPIO.setup(audio_control_pin, GPIO.OUT)

pygame.init()
pygame.mixer.init()

def play_audio():
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_audio():
    pygame.mixer.music.stop()

try:
    play_audio()
    time.sleep(30)  # Adjust the sleep time based on your MP3's duration
    stop_audio()

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    pygame.quit()
