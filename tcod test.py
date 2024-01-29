import tcod

screen_width = 154
screen_height = 105
px = int(screen_width / 2)
py = int(screen_height / 2)

tileset = tcod.tileset.load_tilesheet("C:\\ps\\Project MazeBomb\\project-MazeBomb\\IBM437.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

with tcod.context.new_terminal(screen_width, screen_height, tileset=tileset, title="Rogue Bomber", vsync=True) as context:
     root_console = tcod.Console(screen_width, screen_height, order="F")
     while True:
          root_console.print(x=px, y=py, string="@")
          context.present(root_console)

          for event in tcod.event.wait():
               if event.type == "QUIT":
                    raise SystemExit()
