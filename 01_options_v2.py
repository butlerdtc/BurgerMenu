"""V2 of options screen
Converts V1 to a function and all print statements to easygui
"""

import easygui


# Function to ask user what option they would like to choose
def options():
    # Welcome statement
    easygui.msgbox("Burger Menu Combos", "Menu")
    # Ask user to choose an option
    choice = easygui.buttonbox("What would you like to do?",
                               "Menu Options",
                               ["Add combo", "Find combo", "Delete combo",
                                "Show Combos", "Exit"])
    if choice == "Add combo":
        easygui.msgbox("Add Combo", "Chosen option")
    elif choice == "Find combo":
        easygui.msgbox("Find Combo", "Chosen option")
    elif choice == "Delete combo":
        easygui.msgbox("Delete Combo", "Chosen option")
    elif choice == "Show combos":
        easygui.msgbox("Show all combos", "Chosen option")
    else:
        exit()
    return choice


# Main routine
# Dictionary to store the existing menu combos
existing_menu = {"Value": {"Beef Burger": 5.69, "Fries": 1, "Fizzy drink": 1},
                 "Cheesy": {"Cheese Burger": 6.69, "Fries": 1,
                            "Fizzy drink": 1},
                 "Super": {"Cheese Burger": 6.69, "Large Fries": 2,
                           "Smoothie": 2}
                 }
options()
