import tkinter as tk
import os
from tkinter import messagebox, scrolledtext
from Classes.Chao import Chao

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

def display_chao_data(name, garden):
    data_window = tk.Toplevel()
    data_window.title(f"{name}'s Data")
    center_window(data_window, 400, 600)
    
    # Create a main frame that holds everything
    main_frame = tk.Frame(data_window, bg="lightblue")
    main_frame.pack(fill="both", expand=True)
    
    # Create a canvas within the main frame
    canvas = tk.Canvas(main_frame, bg="lightblue")
    canvas.pack(side="left", fill="both", expand=True)

    # Create a scrollbar and set it to the canvas
    scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Bind the mousewheel to scroll the canvas
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # Create a frame that will contain all the entries
    scrollable_frame = tk.Frame(canvas, bg="lightblue")
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    
    # Update scrollregion in a callback
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=event.width-20)
    scrollable_frame.bind("<Configure>", on_configure)
    
    # Load data and create entry widgets with increased width
    data = Chao.load_data(name, garden)
    entries = {}
    for key, value in data.items():
        # Skip creating an entry for the 'Name' field
        if key == 'Name':
            continue
        frame = tk.Frame(scrollable_frame, bg="lightblue")
        frame.pack(fill=tk.X, padx=5, pady=5)
        label = tk.Label(frame, text=f"{key}: ", width=20, bg="lightblue", anchor="w")
        label.pack(side=tk.LEFT)
        
        if key == 'Garden':
            # Create a dropdown for garden selection
            garden_var = tk.StringVar(value=value)
            garden_dropdown = tk.OptionMenu(frame, garden_var, 'Hero', 'Neutral', 'Dark')
            garden_dropdown.pack(fill=tk.X, padx=5, expand=True)
            entries[key] = garden_var
        else:
            # Create a regular entry for other data points
            entry_text = tk.StringVar(value=value)
            entry = tk.Entry(frame, textvariable=entry_text, bg="lightblue", width=35)
            entry.pack(fill=tk.X, padx=5, expand=True)
            entries[key] = entry_text

    def save_data():
        # Get the updated garden from the dropdown
        new_garden = entries['Garden'].get()

        # Check if the new garden is one of the valid options
        valid_gardens = ['Hero', 'Neutral', 'Dark']
        if new_garden not in valid_gardens:
            messagebox.showerror("Error", "Invalid garden selected.")
            return

        # Check if the garden has changed and move the file if necessary
        if new_garden != garden:
            old_file_path = os.path.join(garden, f"{name}.txt")
            new_file_path = os.path.join(new_garden, f"{name}.txt")
            try:
                os.rename(old_file_path, new_file_path)  # This moves the file
            except OSError as e:
                messagebox.showerror("Error", f"Failed to move the file: {e}")
                return
            
        # Validate lessons and stats before saving
        lessons = ['Bell Level', 'Drum Level', 'Maracas Level', 'Step Dance Level', 'Castanets Level', 'Exercise Level', 'Shake Dance Level', 'Tambourine Level', 'Cymbals Level', 'Flute Level', 'Song Level', 'Trumpet Level', 'Drawing Level', 'Gogo Dance Level', 'Spin Dance Level']  # Add all other lesson names
        stats = ['Swim', 'Fly', 'Run', 'Power', 'Stamina']  # Add all other stat names
        valid_ranks = ['S', 'A', 'B', 'C', 'D', 'E']

        for key, entry_text in entries.items():
            value = entry_text.get().strip()
            if key in lessons:
                if not value.isdigit() or not 0 <= int(value) <= 5:
                    messagebox.showerror("Error", f"Invalid level for {key}. Please enter a number between 0 and 5.")
                    return
            elif key in stats:
                value = entries[key].get().strip().upper()  # Convert stat to uppercase
                if value not in valid_ranks:
                    messagebox.showerror("Error", f"Invalid rank for {key}. Please enter one of {valid_ranks}.")
                    return
                else:
                    entries[key].set(value)  # Update the entry with the uppercase value
            elif key == 'Transformations':
                if not value.isdigit() or int(value) < 0:
                    messagebox.showerror("Error", "Invalid number of transformations. Please enter a positive integer.")
                    return
                
        # Now write the Chao's data to the file in the new location
        try:
            with open(new_file_path if new_garden != garden else os.path.join(garden, f"{name}.txt"), 'w') as file:
                # Skip name and color as they should not be changed
                for key, value in entries.items():
                    if key not in ['Name', 'Color']:
                        file.write(f"{key}: {value.get()}\n")
        except OSError as e:
            messagebox.showerror("Error", f"Failed to save the file: {e}")
            return

        messagebox.showinfo("Success", f"Chao data updated successfully! Moved to {new_garden} garden." if new_garden != garden else "Chao data updated successfully!")
        data_window.destroy()

    # Update the command for the save_button
    save_button = tk.Button(scrollable_frame, text="Save", command=save_data)
    save_button.pack(side='bottom', pady=10, expand=True)

def open_modify_window(chao):
    modify_window = tk.Toplevel()
    modify_window.title("Modify Chao")
    center_window(modify_window, 600, 400)
    modify_window.configure(bg="lightblue")

    gardens = ['Hero', 'Dark', 'Neutral']
    garden_frames = {}

    # Create a frame for each garden and pack them side by side
    for garden in gardens:
        garden_frame = tk.Frame(modify_window, bg="lightblue")
        garden_frame.pack(side=tk.LEFT, expand=True, fill=tk.Y, padx=5, pady=5)
        garden_frames[garden] = garden_frame

        # Pack the garden label at the top of its frame
        label = tk.Label(garden_frame, text=garden.upper(), bg="lightblue", font=("Arial", 16))
        label.pack(pady=(0, 10))

        # Now iterate over the Chao files and pack them under the corresponding garden
        if os.path.exists(garden):
            for chao_file in os.listdir(garden):
                chao_name = chao_file.split('.')[0]
                button = tk.Button(garden_frame, text=chao_name,
                                   command=lambda name=chao_name, gd=garden: display_chao_data(name, gd))
                button.pack(pady=2)
                
def modify_chao(chao):
    from ChaoManager import Chao
    modify_window = tk.Toplevel()
    modify_window.title("Modify Chao")
    Chao.center_window(modify_window, 600, 400)

    gardens = ['Hero', 'Dark', 'Neutral']
    garden_labels = {garden: tk.Label(modify_window, bg="lightblue", font=("Comic Sans MS", 10), text=garden.upper()) for garden in gardens}
    chao_buttons = {garden: [] for garden in gardens}

    for garden, label in garden_labels.items():
        label.pack()
        if os.path.exists(garden):
            for chao_file in os.listdir(garden):
                chao.name = chao_file.split('.')[0]
                button = tk.Button(modify_window, text=chao.name, 
                                    command=lambda name=chao.name, garden=garden: Chao.display_chao_data(name, garden))
                button.pack()
                chao_buttons[garden].append(button)