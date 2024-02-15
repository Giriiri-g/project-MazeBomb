import pygame
import sys

pygame.init()

width, height = 1200, 750 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Algorithm Visualizer")

background_color = (5, 22, 26)
def animated_text_display(word):
    for i in range(len(word) + 1):    
        partial_word = word[:i]
        text_surface = font.render(partial_word, True, text_color)  
        screen.blit(background_image, (0, 0))   
        x = (width - text_surface.get_width()) // 2
        y = (height - text_surface.get_height()) // 20   
        screen.blit(text_surface, (x, y))  
        pygame.display.flip()
        pygame.time.delay(100) 

font_path = "C:\\Users\\ashwi\\Documents\\GitHub_Repos\\project-MazeBomb\\Assets\\fonts\\ttf - Mx (mixed outline+bitmap)\MxPlus_IBM_BIOS.ttf"
font = pygame.font.Font(font_path, 60) 
text_color = (255, 255, 255) 

image_path = "C:\\Users\\ashwi\\Documents\\GitHub_Repos\\project-MazeBomb\\Assets\\Bomber.png"
background_image = pygame.image.load(image_path) 
background_image = pygame.transform.scale(background_image, (width, height))

screen.blit(background_image, (0, 0))
pygame.display.flip()

word_to_display = "Rogue Bomber"

animated_text_display(word_to_display)

message_font_path = font_path
message_font = pygame.font.Font(message_font_path, 36)
message_color = (255, 255, 255)

message_text = "Press Space to Start the Game!"
message_surface = message_font.render(message_text, True, message_color)

message_rect = message_surface.get_rect()
message_rect.center = (width // 2, height - 50) 

screen.blit(message_surface, message_rect)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                screen = pygame.display.set_mode((1200,750))
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
        
            if pygame.Rect(0, 0, width, height).collidepoint(event.pos):
                import main

pygame.quit()
sys.exit()
