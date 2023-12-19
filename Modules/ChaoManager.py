import tkinter as tk
import os
from PIL import Image, ImageTk
from Classes.Chao import Chao
from .AddChao import add_chao
from .ModifyChao import open_modify_window
from .RemoveChao import remove_chao as external_remove_chao
#from .RemoveChao import remove_chao

def modify_chao(chao):
    open_modify_window(chao)

def remove_chao():
    external_remove_chao()

def declare_deceased():
    Chao.not_yet_implemented()

def show_garden(garden):
    Chao.not_yet_implemented()

def get_garden(chao):
    Chao.not_yet_implemented()

def save_to_file(chao):
    # Create the file name
    file_name = f"{chao.garden}/{chao.name}.txt"

    # Open the file for writing
    with open(file_name, "w") as file:
        # Write the information of the new Chao object to the file
        file.write(f"Name: {chao.name}\n")
        file.write(f"Garden: {chao.garden}\n")
        
        for key, value in chao.relatives.items():
            file.write(f"{key}: {value}\n")

        for key, value in chao.stats.items():
            file.write(f"{key}: {', '.join(value)}\n")

        file.write(f"Transformations: {chao.transformations}\n")
        file.write(f"Schooling: {chao.schooling}\n")
        file.write(f"Color: {chao.color}\n")
        print(f"Chao {chao.name} saved to {file_name}")

def load_data(name, garden):
    # Creating empty dict to store variables
    data = {}

    # Open the file
    with open(f"{garden}/{name}.txt", "r") as file:
        # Iterate over each line in the file
        for line in file:
            # Strip leading/trailing whitespace and split the line by colon
            key, value = line.strip().split(':')
            # Strip leading/trailing whitespace from value
            value = value.strip()
            # Add the key-value pair to the data dict
            data[key] = value

    return data

@classmethod
def check_if_chao_exists(cls, name):
    for garden in ['Hero', 'Dark', 'Neutral']:
        if os.path.isfile(f"{garden}/{name}.txt"):
            return True
    return False

def not_yet_implemented():
    # Create a new Toplevel window
    popup = tk.Toplevel()
    popup.geometry("400x100")
    popup.resizable(width=False, height=False)
    label = tk.Label(popup, text="Not yet implemented.")
    label.pack()
    # Create a button to close the window
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack()

def main():
    window = tk.Tk()
    window.title("Chao Manager")

    add_chao_button = tk.Button(window, text="Add Chao", command=add_chao)
    add_chao_button.pack()

    modify_chao_button = tk.Button(window, text="Modify Chao", command=modify_chao)
    modify_chao_button.pack()

    remove_chao_button = tk.Button(window, text="Remove Chao", command=remove_chao)
    remove_chao_button.pack()

    window.mainloop()

if __name__ == '__main__':
    main()