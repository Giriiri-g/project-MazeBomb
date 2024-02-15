import assets
import pygame
import sys

def display_homepage(screen):
    asset = assets.Asset()
    width, height = asset.width, asset.height

    background_color = (5, 22, 26)

    font = asset.font
    text_color = asset.white

    image_path = asset.homepage_bg
    background_image = pygame.image.load(image_path)
    background_image = pygame.transform.scale(background_image, (width, height))

    screen.blit(background_image, (0, 0))
    pygame.display.flip()

    word_to_display = "Rogue Bomber"

    for i in range(len(word_to_display) + 1):
        partial_word = word_to_display[:i]
        text_surface = font.render(partial_word, True, text_color)
        screen.blit(background_image, (0, 0))
        x = (width - text_surface.get_width()) // 2
        y = (height - text_surface.get_height()) // 20
        screen.blit(text_surface, (x, y))
        pygame.display.flip()
        pygame.time.delay(100)

    message_font = asset.font3
    message_color = text_color

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
                    print("Shutting Down")
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    print("Space Pressed")
                    return "login"