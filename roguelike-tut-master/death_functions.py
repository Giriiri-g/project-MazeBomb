import tcod as libtcodpy

from game_states import GameStates
from render_functions import RenderOrder
from game_messages import Message

def kill_player(player):
	player.char = '%'
	player.color = libtcodpy.dark_red
	return Message("You died!", libtcodpy.red), GameStates.PLAYER_DEAD
	
def kill_monster(monster):
	death_message = Message("{} is dead!".format(monster.name.capitalize(), libtcodpy.orange))
	
	monster.char = '%'
	monster.color = libtcodpy.dark_red
	monster.blocks = False
	monster.fighter = None
	monster.ai = None
	monster.name = "remains of " + monster.name
	monster.render_order = RenderOrder.CORPSE
	
	return death_message
