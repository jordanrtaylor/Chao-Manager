import os

def chao_exists(name):
    """
    Check if a Chao with the given name exists in any garden directory
    """
    for garden in ["Hero", "Neutral", "Dark"]:
        path = f"{garden}/{name}.txt"
        if os.path.exists(path):
            return True
    return False

def add_chao(name, garden, parents, children, grand_parents, great_grand_parents, swimming, flying, running, power, stamina, age, transformations, personality, knowledge, color):
    """
    Add a Chao to the specified garden directory
    """
    if not os.path.exists(garden):
        os.mkdir(garden)

    path = f"{garden}/{name}.txt"
    with open(path, "w") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Garden: {garden}\n")
        f.write(f"Parents: {parents}\n")
        f.write(f"Children: {children}\n")
        f.write(f"Grand Parents: {grand_parents}\n")
        f.write(f"Great Grand Parents: {great_grand_parents}\n")
        f.write(f"Swimming: {swimming}\n")
        f.write(f"Flying: {flying}\n")
        f.write(f"Running: {running}\n")
        f.write(f"Power: {power}\n")
        f.write(f"Stamina: {stamina}\n")
        f.write(f"Age: {age}\n")
        f.write(f"Transformations: {transformations}\n")
        f.write(f"Personality: {personality}\n")
        f.write(f"Knowledge: {knowledge}\n")
        f.write(f"Color: {color}\n")

def modify_chao(name, garden, parents, children, grand_parents, great_grand_parents, swimming, flying, running, power, stamina, age, transformations, personality, knowledge, color):
    """
    Modify a Chao in the specified garden directory
    """
    if not os.path.exists(garden):
        print(f"Garden {garden} does not exist.")
        return
    if not chao_exists(name):
        print(f"Chao {name} does not exist.")
        return
    path = f"{garden}/{name}.txt"
    with open(path, "r") as f:
        lines = f.readlines()
    with open(path, "w") as f:
        for line in lines:
            if "Garden:" in line:
                line = f"Garden: {garden}\n"
            if "Parents:" in line:
                line = f"Parents: {parents}\n"
            if "Children:" in line:
                line = f"Children: {children}\n"
            if "Grand Parents:" in line:
                line = f"Grand Parents: {grand_parents}\n"
            if "Great Grand Parents:" in line:
                line = f"Great Grand Parents: {great_grand_parents}\n"
            if "Swimming:" in line:
                line = f"Swimming: {swimming}\n"
            if "Flying:" in line:
                line = f"Flying: {flying}\n"
            if "Running:" in line:
                line = f"Running: {running}\n"
            if "Power:" in line:
                line = f"Power: {power}\n"
            if "Stamina:" in line:
                line = f"Stamina: {stamina}\n"
            if "Age:" in line:
                line = f"Age: {age}\n"
            if "Transformations:" in line:
                line = f"Transformations: {transformations}\n"
            if "Personality:" in line:
                line = f"Personality: {personality}\n"
            if "Knowledge:" in line:
                line = f"Knowledge: {knowledge}\n"
            if "Color:" in line:
                line = f"Color: {color}\n"
            f.write(line)

def remove_chao(name):
    """
    Remove a Chao from the specified garden directory
    """
    for garden in ["Hero", "Neutral", "Dark"]:
        path = f"{garden}/{name}.txt"
        if os.path.exists(path):
            os.remove(path)
            return
    print(f"Chao {name} does not exist.")

def declare_deceased(name):
    """
    Move a Chao from its garden directory to the 'Deceased' directory
    """
    for garden in ["Hero", "Neutral", "Dark"]:
        path = f"{garden}/{name}.txt"
        if os.path.exists(path):
            if not os.path.exists("Deceased"):
                os.mkdir("Deceased")
            os.rename(path, f"Deceased/{name}.txt")
            return
    print(f"Chao {name} does not exist.")

def show_chao(garden):
    """
    Print all Chao in the specified garden
    """
    if os.path.exists(garden):
        for chao in os.listdir(garden):
            path = f"{garden}/{chao}"
            with open(path, "r") as f:
                print(f.read())
    else:
        print(f"Garden {garden} does not exist.")

def get_garden(name):
    for garden in ["Hero", "Neutral", "Dark"]:
        path = f"{garden}/{name}.txt"
        if os.path.exists(path):
            return garden
    return None
