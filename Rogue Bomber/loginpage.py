import pygame
import sys
import os
from moviepy.editor import VideoFileClip

pygame.init()

width, height = 1200, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Login!")

# Load the video file
video_file = "Rogue Bomber\\Assets\\videoplayback.mp4"
video_path = os.path.join("Rogue Bomber\\Assets\\videoplayback.mp4")

# Load the video clip
video_clip = VideoFileClip(video_path)

clock = pygame.time.Clock()

word_to_display = "Login:"

def drop_text_animation(word, font, text_color, background_color, screen):
    text_surface = font.render(word, True, text_color)
    text_width, text_height = text_surface.get_size()
    x = (width - text_width) // 2
    y = height // 8  # Set the desired height
    screen.fill(background_color)  # Fill screen with background color
    screen.blit(text_surface, (x, y))
    pygame.display.flip()

def animated_text_display(word):
    font = pygame.font.Font(None, 64)
    text_color = (255, 255, 255)
    background_color = (0, 0, 0)
    drop_text_animation(word, font, text_color, background_color, screen)

def main():
    animated_text_display(word_to_display)
    
    # Create a text input box for username
    input_box = pygame.Rect(width // 2 - 200, height - 150, 400, 50)
    user_text = ''
    font = pygame.font.Font(None, 36)

    # Play the video loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Username entered:", user_text)
                    # Add code here to handle the username input

                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        # Capture a frame from the video
        frame = video_clip.get_frame(pygame.time.get_ticks() / 1000 % video_clip.duration)
        # Convert the frame to Pygame surface
        frame_surface = pygame.surfarray.make_surface(frame)
        # Scale the frame surface to fit the screen
        scaled_frame_surface = pygame.transform.scale(frame_surface, (width, height))
        # Blit the scaled frame onto the screen
        screen.blit(scaled_frame_surface, (0, 0))

        # Draw the text input box
        pygame.draw.rect(screen, (255, 255, 255), input_box, 2)  # Border for the input box
        pygame.draw.rect(screen, (200, 200, 200), input_box)     # Background color for the input box
        font_surface = font.render(user_text, True, (0, 0, 0))
        screen.blit(font_surface, (input_box.x + 10, input_box.y + 10))  # Adjust text position inside input box

        pygame.display.flip()
        clock.tick(30)  # Adjust the frame rate as needed

if __name__ == "__main__":
    main()
