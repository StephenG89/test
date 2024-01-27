import pygame
import RPi.GPIO as GPIO
import time

# Set the path to your MP3 file (relative to the script)
file_path = "Prelude.mp3"

# Set the GPIO pin for controlling audio
audio_control_pin = 18  # Replace with the actual GPIO pin number

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(audio_control_pin, GPIO.OUT)

# Set the initial volume (between 0.0 and 1.0)
initial_volume = 0.5

pygame.init()
pygame.mixer.init()

def play_audio():
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_audio():
    pygame.mixer.music.stop()

try:
    # Set the initial volume
    pygame.mixer.music.set_volume(initial_volume)

    # Play audio
    play_audio()

    # Allow time for testing (adjust as needed)
    time.sleep(60)  # Adjust the time in seconds based on your testing duration

    # Stop audio
    stop_audio()

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    pygame.quit()
