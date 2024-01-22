import tcod as libtcodpy


def message_box(con, header, width, screen_width, screen_height):
	menu(con, header, [], width, screen_width, screen_height)

def level_up_menu(con, header, player, menu_width, screen_width, screen_height):
	options = [
		"Constitution (+20 HP, from {})".format(player.fighter.max_hp),
		"Strength (+1 attack, from {})".format(player.fighter.power),
		"Agility (+1 defense, from {})".format(player.fighter.defense)
	]
	
	menu(con, header, options, menu_width, screen_width, screen_height)

def main_menu(con, background_image, screen_width, screen_height):
	libtcodpy.image_blit_2x(background_image, 0, 0, 0)
	
	#libtcodpy.image_blit(background_image, con, 0, 0, 
	#	libtcodpy.BKGND_SET, 1.0, 1.0, 0)
	
	#libtcodpy.image_blit_rect(background_image, con, 0, 0, 
	#	-1, -1, libtcodpy.BKGND_SET)
	
	libtcodpy.console_set_default_foreground(0, libtcodpy.light_yellow)
	libtcodpy.console_print_ex(0, int(screen_width/2), int(screen_height/2) - 4,
		libtcodpy.BKGND_NONE, libtcodpy.CENTER,
		"Solar Rogue Redux")
	libtcodpy.console_print_ex(0, int(screen_width/2), int(screen_height - 2),
		libtcodpy.BKGND_NONE, libtcodpy.CENTER,
		"By Ombarus")
	menu(con, '', ["Play a new game", "Continue last game", "Quit"], 24,
		screen_width, screen_height)
		

def menu(con, header, options, width, screen_width, screen_height):
	if len(options) > 26: raise ValueError("Cannot have a menu with more than 26 options")
		
	header_height = libtcodpy.console_get_height_rect(con, 0, 0, width, screen_height, header)
	height = len(options) + header_height
	
	window = libtcodpy.console_new(width, height)
	
	libtcodpy.console_set_default_foreground(window, libtcodpy.white)
	libtcodpy.console_print_rect_ex(window, 0, 0, width, height, libtcodpy.BKGND_NONE, libtcodpy.LEFT, header)
	
	y = header_height
	letter_index = ord('a')
	for option_text in options:
		text = "(" + chr(letter_index) + ") " + option_text
		libtcodpy.console_print_ex(window, 0, y, libtcodpy.BKGND_NONE, libtcodpy.LEFT, text)
		y += 1
		letter_index += 1
		
	x = int(screen_width / 2 - width / 2)
	y = int(screen_height / 2 - height / 2)
	libtcodpy.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)
	
def inventory_menu(con, header, player, inventory, inventory_width, screen_width, screen_height):
	if len(inventory.items) == 0:
		options = ["Inventory is empty."]
	else:
		options = []
		for item in player.inventory.items:
			if player.equipment.main_hand == item:
				options.append("{} (on main hand)".format(item.name))
			elif player.equipment.off_hand == item:
				options.append("{} (on off hand)".format(item.name))
			else:
				options.append(item.name)
		
	menu(con, header, options, inventory_width, screen_width, screen_height)
	
def character_screen(player, char_screen_width, char_screen_height, 
	screen_width, screen_height):
	
	window = libtcodpy.console_new(char_screen_width, char_screen_height)
	
	libtcodpy.console_set_default_foreground(window, libtcodpy.white)
	libtcodpy.console_print_rect_ex(window, 0, 1, char_screen_width, char_screen_height,
		libtcodpy.BKGND_NONE, libtcodpy.LEFT, "Character Information")
	libtcodpy.console_print_rect_ex(window, 0, 2, char_screen_width, char_screen_height,
		libtcodpy.BKGND_NONE, libtcodpy.LEFT, "Level: {}".format(player.level.current_level))
	libtcodpy.console_print_rect_ex(window, 0, 3, char_screen_width, char_screen_height,
		libtcodpy.BKGND_NONE, libtcodpy.LEFT, "Experience: {}".format(player.level.current_xp))
	libtcodpy.console_print_rect_ex(window, 0, 4, char_screen_width, char_screen_height,
		libtcodpy.BKGND_NONE, libtcodpy.LEFT, "Experience to Level: {}".format(player.level.experience_to_next_level))
	libtcodpy.console_print_rect_ex(window, 0, 6, char_screen_width, char_screen_height,
		libtcodpy.BKGND_NONE, libtcodpy.LEFT, "Maximum HP: {}".format(player.fighter.max_hp))
	libtcodpy.console_print_rect_ex(window, 0, 7, char_screen_width, char_screen_height,
		libtcodpy.BKGND_NONE, libtcodpy.LEFT, "Attack: {}".format(player.fighter.power))
	libtcodpy.console_print_rect_ex(window, 0, 8, char_screen_width, char_screen_height,
		libtcodpy.BKGND_NONE, libtcodpy.LEFT, "Defense: {}".format(player.fighter.defense))
	
	x = screen_width // 2 - char_screen_width // 2
	y = screen_height // 2 - char_screen_height // 2
	libtcodpy.console_blit(window, 0, 0, char_screen_width, char_screen_height,
		0, x, y, 1.0, 0.7)
	
	
	
	
	
	
	
