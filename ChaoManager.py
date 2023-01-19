import os
import ast
import PySimpleGUI as GUI

class Chao:
    relatives = {"Parents": [], "Siblings": [], "Children": [], "Grand Parents": [], "Great Grand Parents": []}
    ranks = ["S", "A", "B", "C", "D", "E"]
    stats = {"Swimming": [], "Flying": [], "Power": [], "Running": [], "Stamina": []}

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
        # Get user input for new chao's attributes
        name = GUI.PopupGetText("Enter the name of the new chao: ")
        garden = GUI.PopupGetText("Enter the garden the chao belongs to: ")
        for key in Chao.relatives.keys():
            relative = GUI.PopupGetText(f"Enter the {key} of the chao: ")
            Chao.relatives[key].append(relative)

        # Get user input for stats
        for key in Chao.stats.keys():
            rank = ""
            while rank not in Chao.ranks:
                rank = GUI.PopupGetText(f"Enter the rank of the chao in {key} (S, A, B, C, D, or E): ")
            Chao.stats[key].append(rank)

        age = GUI.PopupGetText("Enter the age of the chao: ")
        transformations = GUI.PopupGetText("Enter the transformations of the chao: ")
        personality = GUI.PopupGetText("Enter the personality of the chao: ")
        schooling = GUI.PopupGetText("Enter the schooling of the chao: ")
        color = GUI.PopupGetText("Enter the color of the chao: ")

        # Create a new Chao object with the inputted attributes
        new_chao = Chao(name, garden, chao.relatives, chao.stats, age,
                        transformations, personality, schooling, color)

        if not os.path.isdir(garden):
            # create the directory
            os.mkdir("{garden}/{name}.txt")
        else:
            print(f"{garden} already exists.")                
        
        # Check if the chao already exists
        if not chao.check_if_chao_exists(new_chao.name):
            # Check if the directory already exists
            print("Chao " + name + " has been added to the list.")
        else:
            print("A chao with that name already exists.")

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

    def get_garden(chao, name):
        return 

    def save_data(chao):
        return

    def load_data():
        return

    def check_if_chao_exists(name):
        for chao in chao_list:
            if chao.name == name:
                return True
        return False
