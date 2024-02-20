import assets
import tkinter as tk
import sys

def display(root, asset):
    try:
        bgpath = asset.homepage_bg
        root.title("HomePage")
        root.geometry("1000x600")
        bgimg = tk.PhotoImage(file=bgpath)
        # Rescale the image to fit the window
        window_width = root.winfo_reqwidth()
        window_height = root.winfo_reqheight()
        scale_factor_width = window_width / bgimg.width()
        scale_factor_height = window_height / bgimg.height()
        scale_factor = min(scale_factor_width, scale_factor_height)
        bgimg = bgimg.subsample(int(1/scale_factor), int(1/scale_factor))
        bglabel = tk.Label(root, image=bgimg)
        bglabel.place(x=0, y=0, relwidth=1, relheight=1)
        root.mainloop()
    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)