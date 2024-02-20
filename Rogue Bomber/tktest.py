import tkinter as tk
import assets
import homepage
import loginpage
import os
import sys


root = tk.Tk()
root.title("Rogue Bomber")
root.config(bg="#000000")
asset = assets.Asset()

homepage.display(root, asset)
root.mainloop()
sys.exit()
loginpage.display(root, asset)

print("Control back")
sys.exit()
