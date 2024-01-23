import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Font Sample Test")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Get the available fonts
available_fonts = pygame.font.get_fonts()

# Set the font size
font_size = 18

# Calculate rows and columns for the grid layout
columns = 8
rows = (len(available_fonts) // columns) + 1

# Main loop to display font samples
for index, font_name in enumerate(available_fonts):
    font = pygame.font.SysFont(font_name, font_size)
    sample_text = f"{font_name}"
    
    # Create a surface with the sample text
    text_surface = font.render(sample_text, True, white)
    
    # Calculate the position in the grid
    col = index % columns
    row = index // columns
    
    # Calculate the position on the screen
    text_x = col * (screen_width // columns)
    text_y = row * (screen_height // rows)
    
    # Blit the text surface onto the screen
    screen.blit(text_surface, (text_x, text_y))
    
# Update the display
pygame.display.flip()

# Main loop to handle events
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Close the window after handling events
pygame.quit()
sys.exit()
