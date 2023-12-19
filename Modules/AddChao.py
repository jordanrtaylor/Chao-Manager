import tkinter as tk
import os

def add_chao(chao):
        # Create all directories
        if not os.path.exists("Dark"):
            os.mkdir("Dark")

        if not os.path.exists("Hero"):
            os.mkdir("Hero")

        if not os.path.exists("Neutral"):
            os.mkdir("Neutral")

        # Handles user input for Chao name. Creates a new window for user input.
        input_window = tk.Toplevel()
        input_window.resizable(width=False, height=False)
        input_window.configure(bg="lightblue")
        screen_width = input_window.winfo_screenwidth()
        screen_height = input_window.winfo_screenheight()

        window_width = input_window.winfo_reqwidth()
        window_height = input_window.winfo_reqheight()

        # Setting the fixed size before calculating the position
        window_width = 500
        window_height = 800

        input_window.update()

        # Calculate the center position
        x_offset = (screen_width - window_width) / 2
        y_offset = (screen_height - window_height) / 2

        input_window.geometry(f"{window_width}x{window_height}+{int(x_offset)}+{int(y_offset)}")
        input_window.title("Let's Add Your Chao!")

        # Name entry
        name = tk.StringVar()
        name_label = tk.Label(input_window, text="Chao Name",bg="lightblue", font=("Comic Sans MS", 10))
        name_label.place(relx=0.1, rely=0.05)

        name_entry = tk.Entry(input_window, textvariable=name, width=22)
        name_entry.place(relx=0.6, rely=0.05)

        # Garden entry
        garden_label = tk.Label(input_window, text="Garden", bg="lightblue", font=("Comic Sans MS", 10))
        garden_label.place(relx=0.1, rely=0.085)

        garden_options = ['Hero', 'Dark', 'Neutral']
        garden = tk.StringVar()
        garden.set(garden_options[0])  # default value
        garden_menu = tk.OptionMenu(input_window, garden, *garden_options)
        garden_menu.place(relx=0.6, rely=0.08)

        # Transformations entry
        transformations = tk.StringVar()
        transformations_label = tk.Label(input_window, text="Transformations Count", bg="lightblue", font=("Comic Sans MS", 10))
        transformations_label.place(relx=0.1, rely=0.125)

        transformations_entry = tk.Entry(input_window, textvariable=transformations, width=22)
        transformations_entry.place(relx=0.6, rely=0.125)

        # Color entry
        color_label = tk.Label(input_window, text="Color", bg="lightblue", font=("Comic Sans MS", 10))
        color_label.place(relx=0.1, rely=0.155)

        color_options = ['Regular', 'White', 'Red', 'Blue', 'Yellow', 'Pink', 'Purple', 'Sky Blue', 'Orange', 'Green', 'Brown', 'Grey', 'Lime Green', 'Black']
        color = tk.StringVar()
        color.set(color_options[0])  # default value
        color_menu = tk.OptionMenu(input_window, color, *color_options)
        color_menu.place(relx=0.6, rely=0.155)

        # Checkboxes for color types
        monotone_var = tk.BooleanVar()
        two_tone_var = tk.BooleanVar()
        shiny_var = tk.BooleanVar()

        # Toggle functions for checkboxes
        def toggle_monotone():
            if monotone_var.get():
                two_tone_var.set(False)

        def toggle_two_tone():
            if two_tone_var.get():
                monotone_var.set(False)

        monotone_check = tk.Checkbutton(input_window, text="Monotone", var=monotone_var, bg="lightblue", command=toggle_monotone)
        two_tone_check = tk.Checkbutton(input_window, text="Two-Tone", var=two_tone_var, bg="lightblue", command=toggle_two_tone)
        shiny_check = tk.Checkbutton(input_window, text="Shiny", var=shiny_var, bg="lightblue")

        monotone_check.place(relx=0.1, rely=0.2)
        two_tone_check.place(relx=0.4, rely=0.2)
        shiny_check.place(relx=0.7, rely=0.2)

        # School entry
        schooling_label = tk.Label(input_window, text="Select Lessons Learned", font=("Comic Sans MS", 10, "bold"), anchor="center")
        schooling_label.configure(bg="lightblue")
        schooling_label.place(relx=0.5, rely=0.25, anchor="center")

        # Lesson Information
        # Lesson label
        lesson_label = tk.Label(input_window, text="Lesson Name", font=("Comic Sans MS", 10, "bold"))
        lesson_label.config(background='lightblue', activebackground='lightblue')
        lesson_label.place(relx=0.2, rely=0.26)

        # Level label
        level_label = tk.Label(input_window, text="Levels 0 - 5 (0 for none)", font=("Comic Sans MS", 10, "bold"))
        level_label.config(background='lightblue', activebackground='lightblue')
        level_label.place(relx=0.5, rely=0.26)

        # Bell Lesson
        bell_label = tk.Label(input_window, text="Bell", font=("Comic Sans MS", 10))
        bell_label.config(background='lightblue', activebackground='lightblue')
        bell_label.place(relx=0.2, rely=0.29)

        bell_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=bell_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.29)  # modify positioning based on i

        bell_level.set(0)  # set default level to 0

        # Drum Lesson
        drum_label = tk.Label(input_window, text="Drum", font=("Comic Sans MS", 10))
        drum_label.config(background='lightblue', activebackground='lightblue')
        drum_label.place(relx=0.2, rely=0.33)

        drum_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=drum_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.33)  # modify positioning based on i

        drum_level.set(0)  # set default level to 0

        # Maracas Lesson
        maracas_label = tk.Label(input_window, text="Maracas", font=("Comic Sans MS", 10))
        maracas_label.config(background='lightblue', activebackground='lightblue')
        maracas_label.place(relx=0.2, rely=0.37)

        maracas_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=maracas_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.37)  # modify positioning based on i

        maracas_level.set(0)  # set default level to 0

        # Step Dance Lesson
        step_dance_label = tk.Label(input_window, text="Step Dance", font=("Comic Sans MS", 10))
        step_dance_label.config(background='lightblue', activebackground='lightblue')
        step_dance_label.place(relx=0.2, rely=0.41)

        step_dance_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=step_dance_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.41)  # modify positioning based on i

        step_dance_level.set(0)  # set default level to 0
        
        # Castanets Lesson
        castanets_label = tk.Label(input_window, text="Castanets", font=("Comic Sans MS", 10))
        castanets_label.config(background='lightblue', activebackground='lightblue')
        castanets_label.place(relx=0.2, rely=0.45)

        castanets_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=castanets_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.45)  # modify positioning based on i

        castanets_level.set(0)  # set default level to 0

        # Exercise Lesson
        exercise_label = tk.Label(input_window, text="Exercise", font=("Comic Sans MS", 10))
        exercise_label.config(background='lightblue', activebackground='lightblue')
        exercise_label.place(relx=0.2, rely=0.49)

        exercise_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=exercise_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.49)  # modify positioning based on i

        exercise_level.set(0)  # set default level to 0

        # Shake Dance Lesson
        shake_dance_label = tk.Label(input_window, text="Shake Dance", font=("Comic Sans MS", 10))
        shake_dance_label.config(background='lightblue', activebackground='lightblue')
        shake_dance_label.place(relx=0.2, rely=0.53)

        shake_dance_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=shake_dance_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.53)  # modify positioning based on i

        shake_dance_level.set(0)  # set default level to 0

        # Tambourine Lesson
        tambourine_label = tk.Label(input_window, text="Tambourine", font=("Comic Sans MS", 10))
        tambourine_label.config(background='lightblue', activebackground='lightblue')
        tambourine_label.place(relx=0.2, rely=0.57)

        tambourine_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=tambourine_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.57)  # modify positioning based on i

        tambourine_level.set(0)  # set default level to 0

        # Cymbals Lesson
        cymbals_label = tk.Label(input_window, text="Cymbals", font=("Comic Sans MS", 10))
        cymbals_label.config(background='lightblue', activebackground='lightblue')
        cymbals_label.place(relx=0.2, rely=0.61)

        cymbals_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=cymbals_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.61)  # modify positioning based on i

        cymbals_level.set(0)  # set default level to 0

        # Flute Lesson
        flute_label = tk.Label(input_window, text="Flute", font=("Comic Sans MS", 10))
        flute_label.config(background='lightblue', activebackground='lightblue')
        flute_label.place(relx=0.2, rely=0.65)

        flute_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=flute_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.65)  # modify positioning based on i

        flute_level.set(0)  # set default level to 0

        # Song Lesson
        song_label = tk.Label(input_window, text="Song", font=("Comic Sans MS", 10))
        song_label.config(background='lightblue', activebackground='lightblue')
        song_label.place(relx=0.2, rely=0.69)

        song_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=song_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.69)  # modify positioning based on i

        song_level.set(0)  # set default level to 0

        # Trumpet Lesson
        trumpet_label = tk.Label(input_window, text="Trumpet", font=("Comic Sans MS", 10))
        trumpet_label.config(background='lightblue', activebackground='lightblue')
        trumpet_label.place(relx=0.2, rely=0.73)

        trumpet_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=trumpet_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.73)  # modify positioning based on i

        trumpet_level.set(0)  # set default level to 0

        # Drawing Lesson
        drawing_label = tk.Label(input_window, text="Drawing", font=("Comic Sans MS", 10))
        drawing_label.config(background='lightblue', activebackground='lightblue')
        drawing_label.place(relx=0.2, rely=0.77)

        drawing_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=drawing_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.77)  # modify positioning based on i

        drawing_level.set(0)  # set default level to 0

        # Gogo Dance Lesson
        gogo_dance_label = tk.Label(input_window, text="Gogo Dance", font=("Comic Sans MS", 10))
        gogo_dance_label.config(background='lightblue', activebackground='lightblue')
        gogo_dance_label.place(relx=0.2, rely=0.81)

        gogo_dance_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=gogo_dance_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.81)  # modify positioning based on i

        gogo_dance_level.set(0)  # set default level to 0

        # Spin Dance Lesson
        spin_dance_label = tk.Label(input_window, text="Spin Dance", font=("Comic Sans MS", 10))
        spin_dance_label.config(background='lightblue', activebackground='lightblue')
        spin_dance_label.place(relx=0.2, rely=0.85)

        spin_dance_level = tk.IntVar()  # this will hold the level for the Bell lesson
        for i in range(6):  # we create a radio button for each level
            rad_button = tk.Radiobutton(input_window, variable=spin_dance_level, value=i, font=("Comic Sans MS", 10))
            rad_button.config(background='lightblue', activebackground='lightblue')
            rad_button.place(relx=0.5 + (i*0.03), rely=0.85)  # modify positioning based on i

        spin_dance_level.set(0)  # set default level to 0

        # Relatives button
        relatives_button = tk.Button(
            input_window, text="Add Relatives", command=lambda: open_relatives_window())
        relatives_button.place(relx=.1, rely=1, y=-10, width=100, anchor='sw')

        # Method to open the new window for entering relatives
        def open_relatives_window():
            relatives_window = tk.Toplevel()
            relatives_window.resizable(width=False, height=False)
            relatives_window.configure(bg="lightblue")
            screen_width = relatives_window.winfo_screenwidth()
            screen_height = relatives_window.winfo_screenheight()

            window_width = 636
            window_height = 200

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
                relatives_window.destroy()

            def on_relatives_cancel():
                relatives_window.destroy()

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
            stats_window = tk.Toplevel()  # Changed to Toplevel instead of Tk
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
            stats_window.geometry("400x350")
            stats_window.title("Add Stats!")

            # Stats entry
            stats = ["Swim", "Fly", "Run", "Power", "Stamina"]
            ranks = ["S", "A", "B", "C", "D", "E"]

            stats_vars = {stat: tk.StringVar(value="S") for stat in stats}

            for i, stat in enumerate(stats):
                label = tk.Label(stats_window, text=stat, bg="lightblue", font=("Comic Sans MS", 10))
                label.place(relx=0.1, rely=0.2 + i*0.1)
                
                radio_var = stats_vars[stat]  # Unique variable for each stat's radio buttons
                for j, rank in enumerate(ranks):
                    radio_button = tk.Radiobutton(stats_window, text=rank, variable=radio_var, value=rank, background='lightblue', activebackground='lightblue')
                    radio_button.place(relx=0.3 + j*0.1, rely=0.2 + i*0.1)
            # Confirm and Cancel buttons
            def on_stats_submit():
                # Update chao.stats with the new values
                for stat in stats:
                    chao.stats[stat] = stats_vars[stat].get()
                stats_window.destroy()

            def on_stats_cancel():
                # Your functionality for Cancel button
                stats_window.destroy()

            # Confirm and Cancel buttons.
            confirm_button = tk.Button(stats_window, text="Confirm", command=on_stats_submit)
            confirm_button.place(relx=.20, rely=1, y=-10, width=100, anchor='sw')

            cancel_button = tk.Button(stats_window, text="Cancel", command=on_stats_cancel)
            cancel_button.place(relx=.80, rely=1, y=-10, width=100, anchor='se')

            stats_window.mainloop()

        def on_submit():
            chao.name = name_entry.get().strip()  # .strip() to remove any leading/trailing spaces
            chao.garden = garden.get()
            chao.color = color.get()

            # Construct the color type string
            color_types = []
            if monotone_var.get():
                color_types.append("Monotone")
            if two_tone_var.get():
                color_types.append("Two-Tone")
            if shiny_var.get():
                color_types.append("Shiny")
            color_type_str = ', '.join(color_types)

            # Use the garden to determine the directory
            directory_path = os.path.join(chao.garden.capitalize())

            # Make sure the directory exists
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            
            try:
                transformations_value = int(transformations_entry.get())
                if transformations_value < 0:
                    raise ValueError("Negative value not allowed")
            except ValueError:
                tk.messagebox.showerror("Invalid Input", "Please enter a positive integer for transformations.")
                return
            
            chao.transformations = transformations_value

            lesson_levels = {
                'Bell Level': bell_level.get(),
                'Drum Level': drum_level.get(),
                'Maracas Level': maracas_level.get(),
                'Step Dance Level': step_dance_level.get(),
                'Castanets Level': castanets_level.get(),
                'Exercise Level': exercise_level.get(),
                'Shake Dance Level': shake_dance_level.get(),
                'Tambourine Level': tambourine_level.get(),
                'Cymbals Level': cymbals_level.get(),
                'Flute Level': flute_level.get(),
                'Song Level': song_level.get(),
                'Trumpet Level': trumpet_level.get(),
                'Drawing Level': drawing_level.get(),
                'Gogo Dance Level': gogo_dance_level.get(),
                'Spin Dance Level': spin_dance_level.get(),
            }

            # Now write the Chao's data to the file
            with open(os.path.join(directory_path, f"{chao.name}.txt"), 'w') as file:
                file.write(f"Name: {chao.name}\n")
                file.write(f"Garden: {chao.garden}\n")
                file.write(f"Color: {chao.color} ({color_type_str})\n")  # Include color types here
                for lesson, level in lesson_levels.items():
                    file.write(f"{lesson}: {level}\n")
                for relation, names in chao.relatives.items():
                    file.write(f"{relation}: {', '.join(names)}\n")
                for stat, value in chao.stats.items():
                    file.write(f"{stat}: {value}\n")
                file.write(f"Transformations: {chao.transformations}\n")

            input_window.destroy()

        def on_cancel():
            input_window.destroy()

        # Submit and Cancel buttons.
        submit_button = tk.Button(input_window, text="Submit", command=on_submit)
        submit_button.place(relx=.55, rely=1, y=-10, width=100, anchor='sw')

        cancel_button = tk.Button(input_window, text="Cancel", command=on_cancel)
        cancel_button.place(relx=.75, rely=1, y=-10, width=100, anchor='sw')

        input_window.mainloop()