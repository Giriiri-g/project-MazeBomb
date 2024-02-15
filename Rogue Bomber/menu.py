import pygame
import assets
asset = assets.Asset()


desc = """Welcome to Rogue Bomber!
A    : Move West
S    : Move South
W    : Move North
D    : Move East
Q    : Quit
/    : Display Help
ESC  : Exit Help Menu
!    : Bomb
▒    : Passage
║    : A vertical wall
═    : A horizontal wall
╠    : Doorway"""

menu_lines = desc.split('\n')
menu_height = len(menu_lines) * asset.font.get_height()
menu = pygame.Surface((asset.font.size(max(menu_lines, key=len))[0], menu_height), pygame.SRCALPHA)
menu.fill(asset.black)  # Make the surface transparent

for i, line in enumerate(menu_lines):
    text_surface = asset.font.render(line, True, asset.grey)
    menu.blit(text_surface, (0, i * asset.font.get_height()))

menu_x = (asset.width - menu.get_width()) // 2
menu_y = (asset.height - menu.get_height()) // 2
