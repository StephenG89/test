import RPi.GPIO as GPIO
import time
import pygame
from pydbus import SystemBus
import os

# Set the path to your MP3 file (replace with the actual path)
file_path = "Fanfare.mp3"

# Set the GPIO pin for controlling audio
audio_control_pin = 18  # Replace with the actual GPIO pin number

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(audio_control_pin, GPIO.OUT)

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set the initial volume (between 0.0 and 1.0)
initial_volume = 0.5

# Set Bluetooth sink name (replace with the actual Bluetooth sink name)
bluetooth_sink_name = "bluez_sink.93_D5_9D_9C_91_B6.a2dp_sink"

# Function to set the default audio sink
def set_audio_sink(sink_name):
    bus = SystemBus()
    manager = bus.get("org.PulseAudio1", "/org/pulseaudio/server_lookup1")
    core = bus.get("org.PulseAudio.Core1", manager.Lookup("org.PulseAudio.Core1"))

    # Replace "alsa_output.platform-bcm2835_audio.analog-stereo" with the default sink
    default_sink = core.sinks[bluetooth_sink_name]
    core.SetDefaultSink(default_sink)

pygame.init()

# Set the ALSA device environment variable
os.environ["SDL_AUDIODRIVER"] = "alsa"

pygame.mixer.init()

# Set up GPIO after initializing Pygame mixer
GPIO.setmode(GPIO.BCM)
GPIO.setup(audio_control_pin, GPIO.OUT)

def play_audio():
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_audio():
    pygame.mixer.music.stop()

try:
    # Set the initial volume
    pygame.mixer.music.set_volume(initial_volume)

    # Set Bluetooth sink as the default audio output
    set_audio_sink(bluetooth_sink_name)

    # Play audio
    play_audio()

    # Allow time for testing (adjust as needed)
    time.sleep(60)  # Adjust the time in seconds based on your testing duration

    # Stop audio
    stop_audio()

except KeyboardInterrupt:
    pass

finally:
    # Reset the default audio output to the original sink
    set_audio_sink("alsa_output.platform-bcm2835_audio.analog-stereo")

    GPIO.cleanup()
    pygame.quit()
