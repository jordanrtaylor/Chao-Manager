import tkinter as tk
from tkinter import messagebox
import os
from enum import Enum
from PIL import Image, ImageTk
import Menu as Menu

relatives = {"Parents": "", "Grand Parents": "", "Great Grand Parents": ""}
ranks = ["S", "A", "B", "C", "D", "E"]
stats = {"Swimming": [], "Flying": [],
         "Power": [], "Running": [], "Stamina": []}

class Chao:
    def __init__(chao, name, garden, relatives, stats, transformations, schooling, color):
        chao.name = name
        chao.garden = garden
        chao.relatives = relatives
        chao.stats = stats
        chao.transformations = transformations
        chao.schooling = schooling
        chao.color = color

    def add_chao(chao, window):
        window.destroy()

        # Create all directories
        if not os.path.exists("Dark"):
            os.mkdir("Dark")

        if not os.path.exists("Hero"):
            os.mkdir("Hero")

        if not os.path.exists("Neutral"):
            os.mkdir("Neutral")

        # Handles user input for Chao name. Creates a new window for user input.
        input_window = tk.Tk()
        #input_window.resizable(width=False, height=False)
        input_window.configure(bg="lightblue")
        screen_width = input_window.winfo_screenwidth()
        screen_height = input_window.winfo_screenheight()

        window_width = input_window.winfo_reqwidth()
        window_height = input_window.winfo_reqheight()

        x_offset = (screen_width - window_width) / 2
        y_offset = (screen_height - window_height) / 2

        input_window.geometry(
            f"{window_width}x{window_height}+{int(x_offset)}+{int(y_offset)}")
        input_window.geometry("500x650")
        input_window.title("Let's Add Your Chao!")

        # Name entry
        name = tk.StringVar()
        name_label = tk.Label(input_window, text="Chao Name",bg="lightblue", font=("Comic Sans MS", 10))
        name_label.place(relx=0.1, rely=0.05)

        name_entry = tk.Entry(input_window, textvariable=name, width=22)
        name_entry.place(relx=0.6, rely=0.05)

        # Garden entry
        garden = tk.StringVar()
        garden_label = tk.Label(input_window, text="Home Garden (Hero, Dark, Neutral)", bg="lightblue", font=("Comic Sans MS", 10))
        garden_label.place(relx=0.1, rely=0.08)

        garden_entry = tk.Entry(input_window, textvariable=garden, width=22)
        garden_entry.place(relx=0.6, rely=0.08)

        # Transformations entry
        transformations = tk.StringVar()
        transformations_label = tk.Label(input_window, text="Transformations Count", bg="lightblue", font=("Comic Sans MS", 10))
        transformations_label.place(relx=0.1, rely=0.11)

        transformations_entry = tk.Entry(input_window, textvariable=transformations, width=22)
        transformations_entry.place(relx=0.6, rely=0.11)

        # Color entry
        color = tk.StringVar()
        color_label = tk.Label(input_window, text="Color", font=("Comic Sans MS", 10))
        color_label.configure(bg="lightblue")
        color_label.place(relx=0.1, rely=0.14)

        color_entry = tk.Entry(input_window, textvariable=color, width=22)
        color_entry.place(relx=0.6, rely=0.14)

        # School entry
        schooling_label = tk.Label(input_window, text="Select Lessons Learned", font=("Comic Sans MS", 10, "bold"), anchor="center")
        schooling_label.configure(bg="lightblue")
        schooling_label.place(relx=0.5, rely=0.2, anchor="center")

        # Lesson Information
        # Lesson label
        lesson_label = tk.Label(input_window, text="Lesson Name", font=("Comic Sans MS", 10, "bold"))
        lesson_label.config(background='lightblue', activebackground='lightblue')
        lesson_label.place(relx=0.2, rely=0.22)

        # Level label
        level_label = tk.Label(input_window, text="Levels 0 - 5 (0 for none)", font=("Comic Sans MS", 10, "bold"))
        level_label.config(background='lightblue', activebackground='lightblue')
        level_label.place(relx=0.5, rely=0.22)

        # Bell Lesson
        bell_label = tk.Label(input_window, text="Bell", font=("Comic Sans MS", 10))
        bell_label.config(background='lightblue', activebackground='lightblue')
        bell_label.place(relx=0.2, rely=0.26)

        bell_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=bell_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.26)  # modify positioning based on i

        bell_level.set(0)  # set default level to 0

        # Drum Lesson
        drum_label = tk.Label(input_window, text="Drum", font=("Comic Sans MS", 10))
        drum_label.config(background='lightblue', activebackground='lightblue')
        drum_label.place(relx=0.2, rely=0.3)

        drum_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=drum_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.3)  # modify positioning based on i

        drum_level.set(0)  # set default level to 0

        # Maracas Lesson
        maracas_label = tk.Label(input_window, text="Maracas", font=("Comic Sans MS", 10))
        maracas_label.config(background='lightblue', activebackground='lightblue')
        maracas_label.place(relx=0.2, rely=0.34)

        maracas_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=maracas_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.34)  # modify positioning based on i

        maracas_level.set(0)  # set default level to 0

        # Step Dance Lesson
        step_dance_label = tk.Label(input_window, text="Step Dance", font=("Comic Sans MS", 10))
        step_dance_label.config(background='lightblue', activebackground='lightblue')
        step_dance_label.place(relx=0.2, rely=0.38)

        step_dance_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=step_dance_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.38)  # modify positioning based on i

        step_dance_level.set(0)  # set default level to 0
        
        # Castanets Lesson
        castanets_label = tk.Label(input_window, text="Castanets", font=("Comic Sans MS", 10))
        castanets_label.config(background='lightblue', activebackground='lightblue')
        castanets_label.place(relx=0.2, rely=0.42)

        castanets_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=castanets_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.42)  # modify positioning based on i

        castanets_level.set(0)  # set default level to 0

        # Exercise Lesson
        exercise_label = tk.Label(input_window, text="Exercise", font=("Comic Sans MS", 10))
        exercise_label.config(background='lightblue', activebackground='lightblue')
        exercise_label.place(relx=0.2, rely=0.46)

        exercise_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=exercise_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.46)  # modify positioning based on i

        exercise_level.set(0)  # set default level to 0

        # Shake Dance Lesson
        shake_dance_label = tk.Label(input_window, text="Shake Dance", font=("Comic Sans MS", 10))
        shake_dance_label.config(background='lightblue', activebackground='lightblue')
        shake_dance_label.place(relx=0.2, rely=0.5)

        shake_dance_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=shake_dance_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.5)  # modify positioning based on i

        shake_dance_level.set(0)  # set default level to 0

        # Tambourine Lesson
        tambourine_label = tk.Label(input_window, text="Tambourine", font=("Comic Sans MS", 10))
        tambourine_label.config(background='lightblue', activebackground='lightblue')
        tambourine_label.place(relx=0.2, rely=0.54)

        tambourine_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=tambourine_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.54)  # modify positioning based on i

        tambourine_level.set(0)  # set default level to 0

        # Cymbals Lesson
        cymbals_label = tk.Label(input_window, text="Cymbals", font=("Comic Sans MS", 10))
        cymbals_label.config(background='lightblue', activebackground='lightblue')
        cymbals_label.place(relx=0.2, rely=0.58)

        cymbals_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=cymbals_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.58)  # modify positioning based on i

        cymbals_level.set(0)  # set default level to 0

        # Flute Lesson
        flute_label = tk.Label(input_window, text="Flute", font=("Comic Sans MS", 10))
        flute_label.config(background='lightblue', activebackground='lightblue')
        flute_label.place(relx=0.2, rely=0.62)

        flute_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=flute_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.62)  # modify positioning based on i

        flute_level.set(0)  # set default level to 0

        # Song Lesson
        song_label = tk.Label(input_window, text="Song", font=("Comic Sans MS", 10))
        song_label.config(background='lightblue', activebackground='lightblue')
        song_label.place(relx=0.2, rely=0.66)

        song_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=song_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.66)  # modify positioning based on i

        song_level.set(0)  # set default level to 0

        # Trumpet Lesson
        trumpet_label = tk.Label(input_window, text="Trumpet", font=("Comic Sans MS", 10))
        trumpet_label.config(background='lightblue', activebackground='lightblue')
        trumpet_label.place(relx=0.2, rely=0.7)

        trumpet_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=trumpet_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.7)  # modify positioning based on i

        trumpet_level.set(0)  # set default level to 0

        # Drawing Lesson
        drawing_label = tk.Label(input_window, text="Drawing", font=("Comic Sans MS", 10))
        drawing_label.config(background='lightblue', activebackground='lightblue')
        drawing_label.place(relx=0.2, rely=0.74)

        drawing_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=drawing_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.74)  # modify positioning based on i

        drawing_level.set(0)  # set default level to 0

        # Gogo Dance Lesson
        gogo_dance_label = tk.Label(input_window, text="Gogo Dance", font=("Comic Sans MS", 10))
        gogo_dance_label.config(background='lightblue', activebackground='lightblue')
        gogo_dance_label.place(relx=0.2, rely=0.78)

        gogo_dance_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=gogo_dance_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.78)  # modify positioning based on i

        gogo_dance_level.set(0)  # set default level to 0

        # Spin Dance Lesson
        spin_dance_label = tk.Label(input_window, text="Spin Dance", font=("Comic Sans MS", 10))
        spin_dance_label.config(background='lightblue', activebackground='lightblue')
        spin_dance_label.place(relx=0.2, rely=0.82)

        spin_dance_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=spin_dance_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.82)  # modify positioning based on i

        spin_dance_level.set(0)  # set default level to 0

        # Relatives button
        relatives_button = tk.Button(
            input_window, text="Add Relatives", command=lambda: open_relatives_window())
        relatives_button.place(relx=.1, rely=1, y=-10, width=100, anchor='sw')

        # Method to open the new window for entering relatives
        def open_relatives_window():
            input_window.destroy()

            relatives_window = tk.Tk()
            relatives_window.resizable(width=False, height=False)
            relatives_window.configure(bg="lightblue")
            screen_width = relatives_window.winfo_screenwidth()
            screen_height = relatives_window.winfo_screenheight()

            window_width = relatives_window.winfo_reqwidth()
            window_height = relatives_window.winfo_reqheight()

            x_offset = (screen_width - window_width) / 2
            y_offset = (screen_height - window_height) / 2

            relatives_window.geometry(
                f"{window_width}x{window_height}+{int(x_offset)}+{int(y_offset)}")
            relatives_window.geometry("636x200")
            relatives_window.title("Add Relatives!")

            # Parents entry
            parent1 = tk.StringVar()
            parent2 = tk.StringVar()
            parents_label = tk.Label(relatives_window, text="Parents", bg="lightblue", font=("Comic Sans MS", 10))
            parents_label.place(relx=0.1, rely=0.15)

            parent1_label = tk.Label(relatives_window, text="Parent 1", bg="lightblue", font=("Comic Sans MS", 10))
            parent1_label.place(relx=0.4, rely=0.06)

            parent2_label = tk.Label(relatives_window, text="Parent 2", bg="lightblue", font=("Comic Sans MS", 10))
            parent2_label.place(relx=0.65, rely=0.06)

            parents1_entry = tk.Entry(relatives_window, textvariable=parent1, width=21)
            parents1_entry.place(relx=0.4, rely=0.15)

            parents2_entry = tk.Entry(relatives_window, textvariable=parent2, width=21)
            parents2_entry.place(relx=0.65, rely=0.15)

            # GrandParents entry
            grand_parent1 = tk.StringVar()
            grand_parent2 = tk.StringVar()
            grand_parent_label = tk.Label(relatives_window, text="Grand Parents", bg="lightblue", font=("Comic Sans MS", 10))
            grand_parent_label.place(relx=0.1, rely=0.34)

            grand_parent1_label = tk.Label(relatives_window, text="Grand Parent 1", bg="lightblue", font=("Comic Sans MS", 10))
            grand_parent1_label.place(relx=0.4, rely=0.25)

            grand_parent2_label = tk.Label(relatives_window, text="Grand Parent 2", bg="lightblue", font=("Comic Sans MS", 10))
            grand_parent2_label.place(relx=0.65, rely=0.25)

            grand_parent1_entry = tk.Entry(relatives_window, textvariable=grand_parent1, width=21)
            grand_parent1_entry.place(relx=0.4, rely=0.34)

            grand_parent2_entry = tk.Entry(relatives_window, textvariable=grand_parent2, width=21)
            grand_parent2_entry.place(relx=0.65, rely=0.34)

            # Great GrandParents entry
            great_grand_parent1 = tk.StringVar()
            great_grand_parent2 = tk.StringVar()
            great_grand_parent_label = tk.Label(relatives_window, text="Great Grand Parents", bg="lightblue", font=("Comic Sans MS", 10))
            great_grand_parent_label.place(relx=0.1, rely=0.53)

            great_grand_parent1_label = tk.Label(relatives_window, text="Great Grand Parent 1", bg="lightblue", font=("Comic Sans MS", 10))
            great_grand_parent1_label.place(relx=0.4, rely=0.44)

            great_grand_parent2_label = tk.Label(relatives_window, text="Great Grand Parent 2", bg="lightblue", font=("Comic Sans MS", 10))
            great_grand_parent2_label.place(relx=0.65, rely=0.44)

            great_grand_parent1_entry = tk.Entry(relatives_window, textvariable=great_grand_parent1, width=21)
            great_grand_parent1_entry.place(relx=0.4, rely=0.53)

            great_grand_parent2_entry = tk.Entry(relatives_window, textvariable=great_grand_parent2, width=21)
            great_grand_parent2_entry.place(relx=0.65, rely=0.53)

            def on_relatives_submit():
                chao.relatives["Parents"] = (parent1.get(), parent2.get())
                chao.relatives["Grand Parents"] = (grand_parent1.get(), grand_parent2.get())
                chao.relatives["Great Grand Parents"] = (great_grand_parent1.get(), great_grand_parent2.get())

                Chao.add_chao(chao, relatives_window)
                relatives_window.destroy()

            def on_relatives_cancel():
                Chao.add_chao(chao, relatives_window)

            # Confirm and Cancel buttons.
            confirm_button = tk.Button(relatives_window, text="Confirm", command=on_relatives_submit)
            confirm_button.place(relx=.55, rely=1, y=-10,
                                width=100, anchor='sw')

            cancel_button = tk.Button(relatives_window, text="Cancel", command=on_relatives_cancel)
            cancel_button.place(relx=.75, rely=1, y=-10, width=100, anchor='sw')

            relatives_window.mainloop()

        # Stats button
        stats_button = tk.Button(
            input_window, text="Add Stats", command=lambda: open_stats_window())
        stats_button.place(relx=.3, rely=1, y=-10, width=100, anchor='sw')

        # Method to open the new window for entering stats
        def open_stats_window():
            stats_window = tk.Tk()
            stats_window.resizable(width=False, height=False)
            stats_window.configure(bg="lightblue")
            screen_width = stats_window.winfo_screenwidth()
            screen_height = stats_window.winfo_screenheight()

            window_width = stats_window.winfo_reqwidth()
            window_height = stats_window.winfo_reqheight()

            x_offset = (screen_width - window_width) / 2
            y_offset = (screen_height - window_height) / 2

            stats_window.geometry(
                f"{window_width}x{window_height}+{int(x_offset)}+{int(y_offset)}")
            stats_window.geometry("636x318")
            stats_window.title("Add Stats!")

            # Parents entry
            parent1 = tk.StringVar()
            parent2 = tk.StringVar()
            parents_label = tk.Label(
                stats_window, text="Parents", bg="lightblue", font=("Comic Sans MS", 10))
            parents_label.place(relx=0.1, rely=0.1)

            parent1_label = tk.Label(
                stats_window, text="Parent 1", bg="lightblue", font=("Comic Sans MS", 10))
            parent1_label.place(relx=0.4, rely=0.03)

            parent2_label = tk.Label(
                stats_window, text="Parent 2", bg="lightblue", font=("Comic Sans MS", 10))
            parent2_label.place(relx=0.65, rely=0.03)

            parents1_entry = tk.Entry(
                stats_window, textvariable=parent1, width=21)
            parents1_entry.place(relx=0.4, rely=0.1)

            parents2_entry = tk.Entry(
                stats_window, textvariable=parent2, width=21)
            parents2_entry.place(relx=0.65, rely=0.1)

            stats_window.mainloop()

        def on_submit():
            chao.name = name_entry.get()
            
            valid_values = ['dark', 'neutral', 'hero']
            chao.garden = garden_entry.get().lower()
            if chao.garden not in valid_values:
                tk.messagebox.showerror("Invalid garden", "Please enter 'Dark', 'Neutral', or 'Hero'.")
            else:
                tk.messagebox.showinfo(
                    "Chao Added!", f"Chao name: {chao.name}\nChao garden: {chao.garden}")
            input_window.destroy()

            chao.garden = relatives

        def on_cancel():
            input_window.destroy()
            Menu.MainMenu()

        # Submit and Cancel buttons.
        submit_button = tk.Button(input_window, text="Submit", command=on_submit)
        submit_button.place(relx=.55, rely=1, y=-10, width=100, anchor='sw')

        cancel_button = tk.Button(input_window, text="Cancel", command=on_cancel)
        cancel_button.place(relx=.75, rely=1, y=-10, width=100, anchor='sw')

        input_window.mainloop()

        # Create a new Chao object with the inputted attributes
        # new_chao = Chao(name, garden, relatives, stats, transformations, schooling, color)

        #Chao.save_to_file(new_chao)

    def modify_chao(chao):
        Chao.not_yet_implemented()

    def remove_chao():
        Chao.not_yet_implemented()

    def declare_deceased():
        Chao.not_yet_implemented()
    
    def show_garden(garden):
        Chao.not_yet_implemented()
    
    def clear():
        Chao.not_yet_implemented()
    
    def quit(window):
        window.destroy()
    
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
            
            for key, value in relatives.items():
                file.write(f"{key}: {value}\n")

            for key, value in stats.items():
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