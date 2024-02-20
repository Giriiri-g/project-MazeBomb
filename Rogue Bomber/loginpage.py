import tkinter as tk
import os
import sys
import database

def display(root, asset):
    background = """
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║                                              ║
║                                              ║
║                                              ║
║                                              ║
║                                              ║
╠══════════════════════════════════════════════╣
║ Rogue's Name?                                ║
╚══════════════════════════════════════════════╝
"""
    bglabel = tk.Label(root, text=background, justify="left")
    bglabel.config(font=("Courier New", 12), bg="black", fg="white")
    bglabel.pack()
    event_loop = tk.Tk()
    event_loop.withdraw()  # Hide the unnecessary event loop window

    # Bind space key to exit callback
    def exit_callback():
        event_loop.destroy()  # Destroy the event loop to exit

    event_loop.bind("<space>", exit_callback)

    # Run the event loop to wait for space key press
    event_loop.mainloop()