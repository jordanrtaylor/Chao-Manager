from Modules import ChaoManager
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import random
import os

def MainMenu():
    chao = ChaoManager.Chao("", "", {}, {}, 0, [], "")

    # create the main window
    window = tk.Tk()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    window_width = window.winfo_reqwidth()
    window_height = window.winfo_reqheight()

    window.title("Chao Chao")

    # Setting the fixed size before calculating the position
    window_width = 954
    window_height = 477

    window.update()

    # Calculate the center position
    x_offset = (screen_width - window_width) / 2
    y_offset = (screen_height - window_height) / 2

    window.geometry(f"{window_width}x{window_height}+{int(x_offset)}+{int(y_offset)}")

    # Function to dynamically load image files into a dictionary
    def load_images_to_dict(directory):
        images_dict = {}
        index = 0
        for filename in os.listdir(directory):
            if filename.endswith(('.png', '.jpg', '.jpeg')):  # Add other image formats if needed
                images_dict[index] = os.path.join(directory, filename)
                index += 1
        return images_dict

    # Path to the directory containing images
    dir_path = "images\\"

    # Load images into a dictionary
    background_images = load_images_to_dict(dir_path)

    # Randomly select an image
    selected_image_key = random.choice(list(background_images.keys()))
    selected_image_path = background_images[selected_image_key]

    # Load the selected image file
    img = Image.open(selected_image_path)
    background_image = ImageTk.PhotoImage(img)

    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Function to resize the background image when the window is resized
    def resize_background(img, background_image, background_label):
        img = img.resize((window.winfo_width(), window.winfo_height()), Image.LANCZOS)
        background_image = ImageTk.PhotoImage(img)
        background_label.configure(image=background_image)
        background_label.image = background_image

    window.bind("<Configure>", lambda event: resize_background(img, background_image, background_label))

    add_chao_button = tk.Button(window, text="Add Chao", command=lambda: ChaoManager.add_chao(chao))
    add_chao_button.grid(row=0, column=0, sticky="nsew")
    add_chao_button.config(width=3, height=2)

    modify_chao_button = tk.Button(window, text="Modify Chao", command=lambda: ChaoManager.modify_chao(chao))
    modify_chao_button.grid(row=0, column=1, sticky="nsew")
    modify_chao_button.config(width=3, height=2)

    remove_chao_button = tk.Button(window, text="Remove Chao", command=lambda: ChaoManager.remove_chao())
    remove_chao_button.grid(row=0, column=2, sticky="nsew")
    remove_chao_button.config(width=3, height=2)

    declare_deceased_button = tk.Button(window, text="Declare Deceased", command=lambda: ChaoManager.declare_deceased())
    declare_deceased_button.grid(row=0, column=3, sticky="nsew")
    declare_deceased_button.config(width=3, height=2)

    show_garden_button = tk.Button(window, text="Show Chao Garden", command=lambda: ChaoManager.show_gardens())
    show_garden_button.grid(row=0, column=4, sticky="nsew")
    show_garden_button.config(width=3, height=2)

    quit_button = tk.Button(window, text="Quit", command=lambda: window.destroy())
    quit_button.grid(row=0, column=5, sticky="nsew")
    quit_button.config(width=3, height=2)

    for i in range(6):
        window.columnconfigure(i, weight=1, minsize=100)
    window.rowconfigure(1, weight=1, minsize=50)

    window.mainloop()

if __name__ == '__main__':
    MainMenu()
