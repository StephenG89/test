import pygame
import time

pygame.init()

# Set the path to your MP3 file
file_path = "Prelude.mp3"

try:
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Add a delay to ensure the MP3 plays
    time.sleep(30)  # Adjust the sleep time based on your MP3's duration

except pygame.error as e:
    print("Error:", e)

finally:
    pygame.mixer.music.stop()
    pygame.quit()
