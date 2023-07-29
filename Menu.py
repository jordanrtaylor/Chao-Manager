import ChaoManager as Manager
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk

def MainMenu():
    chao = Manager.Chao("", "", {}, {}, 0, [], "")

    # create the main window
    window = tk.Tk()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    window_width = window.winfo_reqwidth()
    window_height = window.winfo_reqheight()

    x_offset = (screen_width - window_width) / 2
    y_offset = (screen_height - window_height) / 2

    window.geometry(f"{window_width}x{window_height}+{int(x_offset)}+{int(y_offset)}")
    window.geometry("954x477")
    window.title("Chao Manager")

    # Load the image file
    img = Image.open("sonic.png")
    background_image = ImageTk.PhotoImage(img)

    # Create the background label
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Function to resize the background image when the window is resized
    def resize_background(img, background_image, background_label):
        img = img.resize((window.winfo_width(), window.winfo_height()), Image.LANCZOS)
        background_image = ImageTk.PhotoImage(img)
        background_label.configure(image=background_image)
        background_label.image = background_image

    window.bind("<Configure>", lambda event: resize_background(img, background_image, background_label))

    add_chao_button = tk.Button(window, text="Add Chao", command=lambda: Manager.Chao.add_chao(chao, window))
    add_chao_button.grid(row=0, column=0, sticky="nsew")
    add_chao_button.config(width=2, height=2)

    modify_chao_button = tk.Button(window, text="Modify Chao", command=lambda: Manager.Chao.modify_chao(chao))
    modify_chao_button.grid(row=0, column=1, sticky="nsew")
    modify_chao_button.config(width=2, height=2)

    remove_chao_button = tk.Button(window, text="Remove Chao", command=lambda: Manager.Chao.remove_chao())
    remove_chao_button.grid(row=0, column=2, sticky="nsew")
    remove_chao_button.config(width=2, height=2)

    declare_deceased_button = tk.Button(window, text="Declare Deceased", command=lambda: Manager.Chao.declare_deceased())
    declare_deceased_button.grid(row=0, column=3, sticky="nsew")
    declare_deceased_button.config(width=2, height=2)

    show_garden_button = tk.Button(window, text="Show Chao Garden", command=lambda: Manager.Chao.show_garden(chao))
    show_garden_button.grid(row=0, column=4, sticky="nsew")
    show_garden_button.config(width=2, height=2)

    clear_button = tk.Button(window, text="Clear", command=lambda: Manager.Chao.clear())
    clear_button.grid(row=0, column=5, sticky="nsew")
    clear_button.config(width=2, height=2)

    quit_button = tk.Button(window, text="Quit", command=lambda: Manager.Chao.quit(window))
    quit_button.grid(row=0, column=6, sticky="nsew")
    quit_button.config(width=2, height=2)

    for i in range(7):
        window.columnconfigure(i, weight=1, minsize=100)
    window.rowconfigure(1, weight=1, minsize=50)

    window.mainloop()

if __name__ == '__main__':
    MainMenu()
