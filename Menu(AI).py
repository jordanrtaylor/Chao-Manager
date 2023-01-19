import PySimpleGUI as sg
import ChaoManager

def main():
    # Create the menu layout
    layout = [[sg.Text('Chao Manager')],
              [
                sg.Button('Add Chao'), 
                sg.Button('Modify Chao'), 
                sg.Button('Remove Chao'), 
                sg.Button('Declare Deceased'), 
                sg.Button('Show Chao'), 
                sg.Button('Quit')],
              [sg.Text(' ' * 10), sg.Output(size=(40, 20))]]

    # Create the window
    window = sg.Window('Chao Manager').Layout(layout)

    while True:
        event, values = window.Read()

        if event in (None, 'Quit'):
            break

        elif event == 'Add Chao':
            name = sg.PopupGetText('Enter the name of the Chao:')
            garden = ChaoManager.get_garden(name)
            parents = sg.PopupGetText('Enter the parents of the Chao:')
            children = sg.PopupGetText('Enter the children of the Chao:')
            grand_parents = sg.PopupGetText('Enter the grandparents of the Chao:')
            great_grand_parents = sg.PopupGetText('Enter the great grandparents of the Chao:')
            swimming = sg.PopupGetText('Enter the swimming stat of the Chao:')
            flying = sg.PopupGetText('Enter the flying stat of the Chao:')
            running = sg.PopupGetText('Enter the running stat of the Chao:')
            power = sg.PopupGetText('Enter the power stat of the Chao:')
            stamina = sg.PopupGetText('Enter the stamina stat of the Chao:')
            age = sg.PopupGetText('Enter the age of the Chao:')
            transformations = sg.PopupGetText('Enter the number of transformations of the Chao:')
            personality = sg.PopupGetText('Enter the personality of the Chao:')
            knowledge = sg.PopupGetText('Enter the knowledge of the Chao:')
            color = sg.PopupGetText('Enter the color of the Chao:')
            ChaoManager.add_chao(name, garden, parents, children, grand_parents, great_grand_parents, swimming,
                                 flying, running, power, stamina, age, transformations, personality, knowledge, color)

        elif event == 'Modify Chao':
            name = sg.PopupGetText('Enter the name of the Chao to modify:')
            if ChaoManager.chao_exists(name):
                garden = sg.PopupGetText('Enter the garden of the Chao:')
                parents = sg.PopupGetText('Enter the parents of the Chao:')
                children = sg.PopupGetText('Enter the children of the Chao:')
                grand_parents = sg.PopupGetText('Enter the grandparents of the Chao:')
                great_grand_parents = sg.PopupGetText('Enter the great grandparents of the Chao:')
                swimming = sg.PopupGetText('Enter the swimming stat of the Chao:')
                flying = sg.PopupGetText('Enter the flying stat of the Chao:')
                running = sg.PopupGetText('Enter the running stat of the Chao:')
                power = sg.PopupGetText('Enter the power stat of the Chao:')
                stamina = sg.PopupGetText('Enter the stamina stat of the Chao:')
                age = sg.PopupGetText('Enter the age of the Chao:')
                transformations = sg.PopupGetText('Enter the number of transformations of the Chao:')
                personality = sg.PopupGetText('Enter the personality of the Chao:')
                knowledge = sg.PopupGetText('Enter the knowledge of the Chao:')
                color = sg.PopupGetText('Enter the color of the Chao:')
                ChaoManager.modify_chao(name, garden, parents, children, grand_parents, great_grand_parents,
                                        swimming, flying, running, power, stamina, age, transformations, personality, knowledge, color)
            else:
                print(f"Chao {name} does not exist.")

        elif event == 'Remove Chao':
            name = sg.PopupGetText('Enter the name of the Chao to remove:')
            garden = ChaoManager.get_garden(name)
            if garden:
                ChaoManager.remove_chao(name)
            else:
                print(f"Chao {name} does not exist.")

        elif event == 'Declare Deceased':
            name = sg.PopupGetText('Enter the name of the Chao that died:')
            if ChaoManager.chao_exists(name):
                ChaoManager.declare_deceased(name)
            else:
                print(f"Chao {name} does not exist.")

        elif event == 'Show Chao':
            garden = sg.PopupGetText('Enter the garden to view:')
            ChaoManager.show_chao(garden)

if __name__ == '__main__':
    main()
