import tkinter as tk
import os
from Classes.Chao import Chao

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

def show_chao_stats(name, garden):
    data = Chao.load_data(name, garden)
    stats_window = tk.Toplevel()
    stats_window.title(f"{name}'s Stats")
    center_window(stats_window, 300, 570)
    stats_frame = tk.Frame(stats_window)
    stats_frame.pack(fill='both', expand=True)
    
    for key, value in data.items():
        tk.Label(stats_frame, text=f"{key}: {value}", anchor="w").pack(fill='x')

def show_chao():
    show_window = tk.Toplevel()
    show_window.title("Show Chao")

    window_width = 600
    window_height = 400
    center_window(show_window, window_width, window_height)
    show_window.configure(bg="lightblue")

    gardens = ['Hero', 'Dark', 'Neutral']
    garden_frames = {}
    chao_buttons = {}  # Dictionary to store references to chao buttons

    for garden in gardens:
        garden_frame = tk.Frame(show_window, bg="lightblue")
        garden_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)
        garden_frames[garden] = garden_frame

        label = tk.Label(garden_frame, text=garden.upper(), bg="lightblue", font=("Arial", 16))
        label.pack(pady=(0, 10))

        if os.path.exists(garden):
            chao_buttons[garden] = {}  # Initialize a dictionary for each garden
            for chao_file in os.listdir(garden):
                chao_name = chao_file.split('.')[0]
                chao_buttons[garden][chao_name] = tk.Button(garden_frame, text=chao_name,
                                                            command=lambda name=chao_name, gd=garden: show_chao_stats(name, gd))
                chao_buttons[garden][chao_name].pack(pady=2)
                
if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    show_chao()  # Show the Chao window instead
    root.mainloop()
