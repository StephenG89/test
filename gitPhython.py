import pygame
import os

# Set the path to your MP3 file (relative to the script)
file_path = "Prelude.mp3"

pygame.init()
pygame.mixer.init()

try:
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Add a delay to ensure the MP3 plays for a certain duration
    pygame.time.wait(30000)  # Adjust the time in milliseconds based on your MP3's duration

except pygame.error as e:
    print("Error:", e)

finally:
    pygame.mixer.music.stop()
    pygame.quit()
