import tkinter as tk
import os
from tkinter import messagebox

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

def remove_chao_file(chao_name, garden):
    try:
        os.remove(os.path.join(garden, f"{chao_name}.txt"))
        messagebox.showinfo("Success", f"The Chao '{chao_name}' has been removed from the {garden} garden.")
    except FileNotFoundError:
        messagebox.showerror("Error", f"The Chao '{chao_name}' could not be found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def remove_chao():
    remove_window = tk.Toplevel()
    remove_window.title("Remove Chao")
    
    # Set the dimensions for the window
    window_width = 600
    window_height = 400
    center_window(remove_window, window_width, window_height)
    remove_window.configure(bg="lightblue")

    gardens = ['Hero', 'Dark', 'Neutral']
    garden_frames = {}
    buttons = {}  # Dictionary to store button references

    # Create a frame for each garden and pack them side by side
    for garden in gardens:
        garden_frame = tk.Frame(remove_window, bg="lightblue")
        garden_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)
        garden_frames[garden] = garden_frame

        # Pack the garden label at the top of its frame
        label = tk.Label(garden_frame, text=garden.upper(), bg="lightblue", font=("Arial", 16))
        label.pack(pady=(0, 10))

        # Now iterate over the Chao files and pack them under the corresponding garden
        if os.path.exists(garden):
            for chao_file in os.listdir(garden):
                chao_name = chao_file.split('.')[0]
                # Correct the reference to the button in the lambda function
                button_cmd = lambda name=chao_name, gd=garden, bt=buttons: (
                    remove_chao_file(name, gd),
                    bt[name].pack_forget() if name in bt else None
                )
                # Create the button and store the reference
                button = tk.Button(garden_frame, text=chao_name, command=button_cmd)
                button.pack(pady=2)
                buttons[chao_name] = button  # Store the button with chao_name as the key