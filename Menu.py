import ChaoManager as Manager
import PySimpleGUI as GUI

def main():
    chao = Manager.Chao("", "", {}, {}, 0, 0, "", [], "")

    # Create the menu layout, this is a list of lists which contains the elements that will be shown in the GUI window
    layout = [
        [
            # button element that when pressed will call the add_chao function from the ChaoManager module
            GUI.Button('Add Chao'),
            # button element that when pressed will call the modify_chao function from the ChaoManager module
            GUI.Button('Modify Chao'),
            # button element that when pressed will call the remove_chao function from the ChaoManager module
            GUI.Button('Remove Chao'),
            # button element that when pressed will call the declare_deceased function from the ChaoManager module
            GUI.Button('Declare Deceased'),
            # button element that when pressed will call the show_garden function from the ChaoManager module
            GUI.Button('Show Chao'),
            # button element that when pressed will call the clear function from the ChaoManager module
            GUI.Button('Clear'),
            # button element that when pressed will close the GUI window
            GUI.Button('Quit')
        ],
        # Output element that will display text or information
        [GUI.Output(size=(65, 30))]
    ]

    # Create the window, this will create a GUI window with the title "Chao Manager" and using the layout variable as the layout for the window
    # element_justification = "c" is used to center the elements in the window
    window = GUI.Window("Chao Manager", layout, element_justification="c", finalize = True)

    # Event loop to process the user input, this will run until the user closes the window or clicks the Quit button
    while True:
        event, values = window.Read()

        # if the event is None or the event is "Quit" then the loop will break
        if event in (None, "Quit"):
            break

        # if the event is "Add Chao" then the add_chao function from the ChaoManager module will be called
        if event == "Add Chao":
            Manager.Chao.add_chao(chao)

        # if the event is "Modify Chao" then the modify_chao function from the ChaoManager module will be called
        if event == "Modify Chao":
            Manager.modify_chao(chao.name)

        # if the event is "Remove Chao" then the remove_chao function from the ChaoManager module will be called
        if event == "Remove Chao":
            Manager.remove_chao(chao.name)

        # if the event is "Declare Deceased" then the declare_deceased function from the ChaoManager module will be called
        if event == "Declare Deceased":
            Manager.declare_deceased(chao.name)

        # if the event is "Show Chao" then the show_chao function from the ChaoManager module will be called
        if event == "Show Chao":
            Manager.show_chao(chao.garden)

    # Close the window, this will close the GUI window
    window.Close()

if __name__ == '__main__':
    main()
