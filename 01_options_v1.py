"""Options screen so user can choose what they want to do """

import easygui
# Dictionary to store the existing menu combos
existing_menu = {"Value": {"Beef Burger", "Fries", "Fizzy drink"},
                 "Cheesy": {"Cheese Burger", "Fries", "Fizzy drink"},
                 "Super": {"Cheese Burger", "Large Fries", "Smoothie"}
                 }

# Welcome statement
easygui.msgbox("Burger Menu Combos", "Menu")
# Ask user to choose an option
choice = easygui.buttonbox("What would you like to do?",
                           "Menu Options",
                           ["Add combo", "Find combo", "Delete combo",
                            "Show Combos", "Exit"])
if choice == "Add combo":
    print("Add combo")
elif choice == "Find combo":
    print("Find combo")
elif choice == "Delete combo":
    print("Delete combo")
elif choice == "Show combos":
    print("Show all combos")
else:
    print("Exit")
