"""V2 of options screen
Converts V1 to a function
"""

import easygui


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
        easygui.msgbox("Exit", "Exit")
    return choice


# Dictionary to store the existing menu combos
existing_menu = {"Value": {"Beef Burger", "Fries", "Fizzy drink"},
                 "Cheesy": {"Cheese Burger", "Fries", "Fizzy drink"},
                 "Super": {"Cheese Burger", "Large Fries", "Smoothie"}
                 }
options()
