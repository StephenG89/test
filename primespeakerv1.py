import pygame
import time

pygame.init()

# Set the audio device to ALSA
pygame.mixer.init()

# Set the path to a test MP3 file (replace with an actual file path)
file_path = "your_test_file.mp3"

try:
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

    # Allow time for testing (adjust as needed)
    time.sleep(10)  # Adjust the time in seconds based on your testing duration

    pygame.mixer.music.stop()

except KeyboardInterrupt:
    pass

finally:
    pygame.quit()
