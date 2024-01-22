import tcod as libtcodpy
from enum import Enum
from game_states import GameStates
from menus import inventory_menu, level_up_menu, character_screen

class RenderOrder(Enum):
	STAIRS = 1
	CORPSE = 2
	ITEM = 3
	ACTOR = 4
	
def get_names_under_mouse(mouse, entities, fov_map):
	(x, y) = (mouse.cx, mouse.cy)
	names = [entity.name for entity in entities
		if entity.x == x and entity.y == y and fov_map.fov[entity.y][entity.x]]
	names = ", ".join(names)
	
	return names.capitalize()
	
def render_bar(panel, x, y, total_width, name, value, maximum, bar_color, back_color):
	bar_width = int(float(value) / maximum * total_width)
	
	libtcodpy.console_set_default_background(panel, back_color)
	libtcodpy.console_rect(panel, x, y, total_width, 1, False, libtcodpy.BKGND_SCREEN)
	libtcodpy.console_set_default_background(panel, bar_color)
	if bar_width > 0:
		libtcodpy.console_rect(panel, x, y, bar_width, 1, False, libtcodpy.BKGND_SCREEN)
		
	libtcodpy.console_set_default_foreground(panel, libtcodpy.white)
	libtcodpy.console_print_ex(panel, int(x + total_width/2), y, libtcodpy.BKGND_NONE, 
		libtcodpy.CENTER, "{}: {}/{}".format(name, value, maximum))

def render_all(con, panel, entities, player, game_map, fov_map, fov_recompute, message_log, screen_width, 
	screen_height, bar_width, panel_height, panel_y, mouse, colors, game_state):
	if fov_recompute:
		for y in range(game_map.height):
			for x in range(game_map.width):
				visible = fov_map.fov[y][x]
				wall = game_map.tiles[x][y].block_sight
				if visible:
					if wall:
						libtcodpy.console_set_char_background(con, x, y, colors.get("light_wall"), libtcodpy.BKGND_SET)
					else:
						libtcodpy.console_set_char_background(con, x, y, colors.get("light_ground"), libtcodpy.BKGND_SET)
					game_map.tiles[x][y].explored = True
				elif game_map.tiles[x][y].explored:
					if wall:
						libtcodpy.console_set_char_background(con, x, y, colors.get("dark_wall"), libtcodpy.BKGND_SET)
					else:
						libtcodpy.console_set_char_background(con, x, y, colors.get("dark_ground"), libtcodpy.BKGND_SET)
	
	entities_in_render_order = sorted(entities, key=lambda x: x.render_order.value)
	
	for entity in entities_in_render_order:
		if fov_map.fov[entity.y][entity.x] or (entity.stairs and game_map.tiles[entity.x][entity.y].explored):
			draw_entity(con, entity)
	
	libtcodpy.console_set_default_background(panel, libtcodpy.black)
	libtcodpy.console_clear(panel)
	
	render_bar(panel, 1, 1, bar_width, "HP", player.fighter.hp, player.fighter.max_hp,
		libtcodpy.light_red, libtcodpy.darker_red)
		
	libtcodpy.console_print_ex(panel, 1, 3, libtcodpy.BKGND_NONE, libtcodpy.LEFT,
		"Dungeon level: {}".format(game_map.dungeon_level))
		
	libtcodpy.console_set_default_foreground(panel, libtcodpy.light_gray)
	libtcodpy.console_print_ex(panel, 1, 0, libtcodpy.BKGND_NONE, libtcodpy.LEFT, 
		get_names_under_mouse(mouse, entities, fov_map))
		
	y = 1
	for message in message_log.messages:
		libtcodpy.console_set_default_foreground(panel, message.color)
		libtcodpy.console_print_ex(panel, message_log.x, y, libtcodpy.BKGND_NONE, libtcodpy.LEFT, message.text)
		y += 1
		
	libtcodpy.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
	libtcodpy.console_blit(panel, 0, 0, screen_width, panel_height, 0, 0, panel_y)
	
	inventory_title = None
	if game_state == GameStates.SHOW_INVENTORY:
		inventory_title = "Press the key next to an item to use it, or Esc to cancel.\n"
	elif game_state == GameStates.DROP_INVENTORY:
		inventory_title = "Press the key next to an item to drop it, or Esc to cancel.\n"
	
	if inventory_title != None:
		inventory_menu(con, inventory_title, player,
			player.inventory, 50, screen_width, screen_height)
			
	if game_state == GameStates.LEVEL_UP:
		level_up_menu(con, "Level up! Choose a stat to raise:", player, 40,
			screen_width, screen_height)
			
	if game_state == GameStates.CHARACTER_SCREEN:
		character_screen(player, 30, 10, screen_width, screen_height)
	
def clear_all(con, entities):
	for entity in entities:
		clear_entity(con, entity)
		
def draw_entity(con, entity):
	libtcodpy.console_set_default_foreground(con, entity.color)
	libtcodpy.console_put_char(con, entity.x, entity.y, entity.char, libtcodpy.BKGND_NONE)
	
def clear_entity(con, entity):
	libtcodpy.console_put_char(con, entity.x, entity.y, ' ', libtcodpy.BKGND_NONE)
