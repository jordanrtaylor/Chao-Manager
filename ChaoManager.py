import os
import PySimpleGUI as GUI

relatives = {"Parents": "", "Siblings": "", "Children": "", "Grand Parents": "", "Great Grand Parents": ""}
ranks = ["S", "A", "B", "C", "D", "E"]
stats = {"Swimming": [], "Flying": [], "Power": [], "Running": [], "Stamina": []}

class Chao:
    def __init__(chao, name, garden, relatives, stats, age, transformations, personality, schooling, color):
        chao.name = name
        chao.garden = garden
        chao.relatives = relatives
        chao.stats = stats
        chao.age = age
        chao.transformations = transformations
        chao.personality = personality
        chao.schooling = schooling
        chao.color = color
    
    # button used in Menu
    def add_chao(chao):
        # Create all directories
        if not os.path.exists("Dark"):
            os.mkdir("Dark")

        if not os.path.exists("Hero"):
            os.mkdir("Hero")

        if not os.path.exists("Neutral"):
            os.mkdir("Neutral")
        
        # Get user input for new chao's attributes
        name = GUI.PopupGetText("Enter the name of the new chao: ")
        while Chao.check_if_chao_exists(name):
            GUI.Popup("A Chao with this name already exists.")
            name = GUI.PopupGetText("Enter the name of the new chao: ")

        garden = GUI.PopupGetText("Enter the garden the chao belongs to: ")
        while garden not in ['Hero', 'Dark', 'Neutral']:
            GUI.Popup("Invalid garden. Please enter 'Hero', 'Dark', or 'Neutral'.")
            garden = GUI.PopupGetText("Enter the garden the chao belongs to: ")
        
        for key in relatives.keys():
            relative = GUI.PopupGetText(f"Enter the {key} of the chao: ") or None
            relatives[key] = relative
        
        for key in stats.keys():
            rank = ""
            while rank not in ranks:
                rank = GUI.PopupGetText(f"Enter the rank of the chao in {key} (S, A, B, C, D, or E): ").upper()
            stats[key].append(rank)

        while True:
            age = GUI.PopupGetText("Enter the age of the chao: ")
            if age.isdigit():
                age = int(age)
                break
            else:
                GUI.Popup("Please enter a valid integer.")
        
        while True:
            transformations = GUI.PopupGetText("Enter the transformations of the chao: ")
            if transformations.isdigit():
                transformations = int(transformations)
                break
            else:
                GUI.Popup("Please enter a valid integer.")

        personality = GUI.PopupGetText("Enter the personality of the chao: ") or None
        schooling = GUI.PopupGetText("Enter the schooling of the chao: ") or None
        color = GUI.PopupGetText("Enter the color of the chao: ") or None

        # Create a new Chao object with the inputted attributes
        new_chao = Chao(name, garden, relatives, stats, age, transformations, personality, schooling, color)

        Chao.save_to_file(new_chao)

    # button used in Menu
    def modify_chao():
        return
    
    # button used in Menu
    def remove_chao():
        return

    # button used in Menu
    def declare_deceased():
        return
    
    # button used in Menu
    def show_garden(garden):
        return

    # button used in Menu
    def clear():
        return

    def get_garden(chao):
        return 

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

            file.write(f"Age: {chao.age}\n")
            file.write(f"Transformations: {chao.transformations}\n")
            file.write(f"Personality: {chao.personality}\n")
            file.write(f"Schooling: {chao.schooling}\n")
            file.write(f"Color: {chao.color}\n")
            print(f"Chao {chao.name} saved to {file_name}")

    def load_data():
        return
    
    @classmethod
    def check_if_chao_exists(cls, name):
        for garden in ['Hero', 'Dark', 'Neutral']:
            if os.path.isfile(f"{garden}/{name}.txt"):
                return True
        return False
