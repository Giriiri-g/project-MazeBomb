import sys
import pygame
import assets

# Move the declaration of user_text outside of the display_login_page function
user_text = ''

def display_login_page(screen):
    asset = assets.Asset()
    background_image = pygame.transform.scale(pygame.image.load(asset.homepage_bg), (asset.width, asset.height))

    font = asset.font
    text_color = asset.text_color
    background_color = asset.background_color

    word_to_display = "Login!"

    def drop_text_animation(word):
        text_surface = font.render(word, True, text_color)
        text_width, text_height = text_surface.get_size()
        x = (asset.width - text_width) // 2
        y = -text_height
        stop_y = asset.height // 8  # Adjust this value to control where the word stops dropping
        speed = 5  # Adjust the speed of dropping here
        while y < stop_y:
            screen.blit(background_image, (0, 0))  # Redraw background image
            screen.blit(text_surface, (x, y))
            y += speed
            pygame.display.flip()
            pygame.time.delay(50)
        
        # After animation, draw the text at the specified height
        x = (asset.width - text_width) // 2
        y = asset.height // 8  # Set the desired height
        screen.blit(background_image, (0, 0))  # Redraw background image
        screen.blit(text_surface, (x, y))
        pygame.display.flip()

    def create_login_surface():
        global user_text  # Declare user_text as global to modify it within this function
        login_surface = pygame.Surface((asset.width, asset.height))  # Create a surface with desired dimensions
        drop_text_animation(word_to_display)
        message_text = "Enter your username and press Space to Start the Game!"
       
        message_font = asset.font3  # Use the same font as word_to_display, can adjust size
        message_font_size = 36  # Adjust font size
        message_font = pygame.font.Font(None, message_font_size)
        message_surface = message_font.render(message_text, True, text_color)
        # Adjust position
        message_rect = message_surface.get_rect()
        message_rect.center = (asset.width // 2, asset.height - 100)  # Adjusted position
        
        # Create a text input box
        input_box = pygame.Rect(asset.width // 2 - 200, asset.height // 2 + 175, 400, 50)
        font2 = asset.font2
    
        login_surface.blit(background_image, (0, 0))  # Redraw background image
        login_surface.blit(message_surface, message_rect)
        
        font = asset.font
        text_surface = font.render(word_to_display, True, text_color)
        text_width, text_height = text_surface.get_size()
        login_surface.blit(text_surface, ((asset.width - text_width) // 2,  asset.height // 8))
        
        # Draw the input box
        pygame.draw.rect(login_surface, asset.text_input_box_color, input_box)  # Border for the input box
        pygame.draw.rect(login_surface, asset.text_input_bg_color, input_box)   # Background color for the input box
        
        return login_surface, input_box, user_text  # Return user_text from the function

    login_surface, input_box, user_text = create_login_surface()

    screen.blit(login_surface, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Enter key pressed! Starting the game...")
                    return 'game'
                elif event.key == pygame.K_BACKSPACE:
                    # Remove the last character from the user_text if backspace is pressed
                    user_text = user_text[:-1]
                else:
                    # Check if the length of user_text is less than 8 before adding a character
                    if len(user_text) < 8:
                        # Add the pressed character to user_text
                        user_text += event.unicode

        # Clear the input box before re-drawing
        pygame.draw.rect(login_surface, asset.text_input_bg_color, input_box)
        
        # Render the text on the input box surface
        font2 = asset.font2
        text_surface = font2.render(user_text, True, text_color)
        # Adjust position of the text
        text_rect = text_surface.get_rect()
        text_rect.center = input_box.center
        login_surface.blit(text_surface, text_rect)
        
        # Draw the input box
        pygame.draw.rect(login_surface, asset.text_input_box_color, input_box, 2)  # Border for the input box
        
        screen.blit(login_surface, (0, 0))
        pygame.display.flip()



bg = """
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║                                                                            ║
║                                                                            ║
║                                                                            ║
║                                                                            ║
║                                                                            ║
║                                                                            ║
║                                                                            ║
║                                                                            ║
╠════════════════════════════════════════════════════════════════════════════╣
║ Rogue's Name?                                                              ║
╚════════════════════════════════════════════════════════════════════════════╝
"""
