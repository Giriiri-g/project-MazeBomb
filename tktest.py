import tkinter as tk

def move(d):
    global Player_pos, playermap, lines
    if d == "a":
        calcpos = [Player_pos[0], Player_pos[1] - 1]
        calcmappos = mapindexer(calcpos)
        if checkvalid(calcmappos):
            Player_pos = calcpos
            drawplayer(calcmappos)
    elif d == "s":
        calcpos = [Player_pos[0] + 1, Player_pos[1]]
        calcmappos = mapindexer(calcpos)
        if checkvalid(calcmappos):
            Player_pos = calcpos
            drawplayer(calcmappos)
    elif d == "w":
        calcpos = [Player_pos[0] - 1, Player_pos[1]]
        calcmappos = mapindexer(calcpos)
        if checkvalid(calcmappos):
            Player_pos = calcpos
            drawplayer(calcmappos)
    elif d == "d":
        calcpos = [Player_pos[0], Player_pos[1] + 1]
        calcmappos = mapindexer(calcpos)
        if checkvalid(calcmappos):
            Player_pos = calcpos
            drawplayer(calcmappos)

def checkvalid(mappos):
    if Map[mappos] in ['║', '═', '╗', '╝', '╚', '╔', " "]:
        return False
    return True

def mapindexer(pos):
    return pos[0] * 71 + pos[1] + 1

def drawplayer(mappos):
    global playermap, lines
    playermap = Map[:mappos] + "@" + Map[mappos + 1:]
    lines = playermap.split('\n')
    draw_map()

def draw_map():
    canvas.delete("all")
    canvas.config(bg=black)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            color = "black"
            if char in ['║', '═', '╗', '╝', '╚', '╔', '╦', '╣', '╠', '╩']:
                color = "#aa5500"  # wall_color
            elif char == "∙":
                color = "#50f050"  # movable_space_color
            elif char == "!":
                color = "#fbfb54"  # exclamation_color
            elif char == "▒":
                color = "#a7a7a7"  # passage_color
            elif char == "@":
                color = "#0000ff"  # player_color

            canvas.create_text(j * 18 +100, i * 25+100, text=char, fill=color, font=("Courier New", 22))

def key_pressed(event):
    global menu_active
    if event.keysym == 'q' and menu_active:
        print("Shutting Down")
        root.destroy()  # Close the Tkinter window
    elif not menu_active:
        if event.keysym == 'a':
            move("a")
            print("A")
        elif event.keysym == 's':
            move("s")
            print("S")
        elif event.keysym == 'w':
            move("w")
            print("W")
        elif event.keysym == 'd':
            move("d")
            print("D")
    if event.keysym == 'Escape':
        menu_active = False
    elif event.keysym == 'slash':
        menu_active = True
        # Perform actions to display menu

# Main
root = tk.Tk()
root.title("Rogue Bomber")
root.config(bg="#000000")

canvas = tk.Canvas(root, width=1400, height=840)
canvas.pack()

Map = """       ╔══════════╗                                                   
       ║∙∙∙∙∙∙∙∙∙∙║                               ╔══════════════════╗
       ║∙∙∙∙∙∙∙∙∙∙║                               ║∙∙∙∙∙∙∙∙!∙∙∙∙∙∙∙∙∙║
       ╚══════╦═══╝                            ▒▒▒╣∙∙∙∙∙∙∙∙∙∙∙∙∙!∙∙∙∙║
              ▒                         ▒▒▒▒▒▒▒▒  ╚╦═════════════════╝
              ▒                         ▒          ▒                  
        ▒▒▒▒▒▒▒                    ▒▒▒▒▒▒          ▒▒▒▒▒▒             
╔═══════╩══════════╗               ▒              ╔═════╩════════════╗
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙╠▒▒▒            ▒              ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║  ▒  ╔═════════╩═╗            ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║  ▒▒▒╣∙∙∙∙∙∙∙∙∙!∙║            ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙∙∙∙∙∙∙∙∙╠▒▒▒▒▒▒▒▒▒▒▒▒╣∙∙∙∙∙∙∙∙∙∙∙∙!∙∙∙∙∙║
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙∙!∙∙∙∙∙∙║            ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
╚═══════╦══════════╝     ╚═════════╦═╝            ╚══════════════════╝
        ▒                   ▒▒▒▒▒▒▒▒                                  
        ▒▒▒▒▒▒▒▒▒▒▒       ╔═╩═╗                                       
       ╔══════════╩═╗    ▒╣∙∙∙║                          ╔════╗       
       ║∙∙∙∙∙∙∙∙∙∙∙∙╠▒▒▒▒▒║∙∙∙║                          ║∙∙∙∙║       
       ║∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙║                          ║∙!∙∙║       
       ║∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙║  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╣∙∙∙∙║       
       ║∙∙∙∙∙!∙∙∙∙∙∙║     ║∙∙∙╠▒▒▒                       ║∙∙∙∙║       
       ╚════════════╝     ╚═══╝                          ╚════╝       
"""

black = "#000000"
player_color = "#0000ff"

Player_pos = [10, 9]
lines = []

# Initial variables
menu_active = False

root.bind("<Key>", key_pressed)
draw_map()

root.mainloop()
