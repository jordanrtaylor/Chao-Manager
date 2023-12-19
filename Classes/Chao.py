import tkinter as tk

relatives = {"Parents": "", "Grand Parents": "", "Great Grand Parents": ""}
ranks = ["S", "A", "B", "C", "D", "E"]
stats = {"Swimming": [], "Flying": [], "Power": [], "Running": [], "Stamina": []}

class Chao:
    def __init__(self, name, garden, relatives, stats, transformations, schooling, color):
        self.name = name
        self.garden = garden
        self.relatives = relatives
        self.stats = stats
        self.transformations = transformations
        self.schooling = schooling
        self.color = color

    def save_to_file(self):
        # Create the file name
        file_name = f"{self.garden}/{self.name}.txt"

        # Open the file for writing
        with open(file_name, "w") as file:
            # Write the information of the Chao object to the file
            file.write(f"Name: {self.name}\n")
            file.write(f"Garden: {self.garden}\n")

            for key, value in self.relatives.items():
                file.write(f"{key}: {value}\n")

            for key, value in self.stats.items():
                file.write(f"{key}: {', '.join(value)}\n")

            file.write(f"Transformations: {self.transformations}\n")
            file.write(f"Schooling: {self.schooling}\n")
            file.write(f"Color: {self.color}\n")
            print(f"Chao {self.name} saved to {file_name}")

    @staticmethod
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

    @staticmethod
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