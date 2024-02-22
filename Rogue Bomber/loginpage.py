import tkinter as tk
from PIL import Image, ImageTk
import database
import tkinter.font as font

def display_login(asset):
    global usernames
    usernames = []
    def validate_length(P):
        if len(P) > 10:
            return False
        return True
    
    def on_enter_pressed(event, entry):
        global usernames
        name = entry.get()
        entry.delete(0, 'end')
        print(f"User Name: {name}")
        database.load_user_data(name)
        usernames.append(name)
        if len(usernames) == 4:
            root.destroy()
            return

    root = tk.Tk()
    root.title("Login Page")
    root.configure(background='black')
    root.geometry("1000x800+250+19")  # height x width + x_offset + y_offset

    # Load and resize background image
    image = Image.open(asset.homepage_bg)  # Change "background_image.jpg" to your image file
    image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
    background_image = ImageTk.PhotoImage(image)

    # Create background label
    background_label = tk.Label(root, font=("Courier", 18), bg="black", fg="white", bd=2, relief="solid", image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Load the font file
    title_font = font.Font(family="AcPlus_IBM_BIOS", size=60)
    try:
        title_font = font.Font(family="AcPlus_IBM_BIOS", size=60)
    except tk.TclError:
        title_font = font.create_font("AcPlus_IBM_BIOS", 60, "normal", "normal", "normal", "normal", "normal", "normal", "normal", "normal", "mono", "normal")

    title = "ROGUE BOMBER"
    title_label = tk.Label(root, text=title, font=title_font, bg="black", fg="white", bd=2, relief="solid")
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    # Create entry widget
    frame = tk.Frame(root, bg="black", bd=2, highlightcolor="#CCCCCC", highlightthickness=2, relief="solid")
    frame.place(relx=0.5, rely=0.95, anchor="center")

    # Create label and entry widget inside frame
    label = tk.Label(frame, text="Rogue's Name?", font=("Arial", 28), bg="black", fg="white")
    label.pack(side="left")
    entry = tk.Entry(frame, bg="black", fg="white", font=("Arial", 28), width=10, validate="key", validatecommand=(root.register(validate_length), "%P"))
    entry.pack(padx=5, side="right", fill="x", expand=True)
    entry.focus()

    # Bind Enter key to entry widget
    entry.bind("<Return>", lambda event: on_enter_pressed(event, entry))
    root.mainloop()

    return "game", usernames