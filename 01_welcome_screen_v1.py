"""Welcome screen V1
Runs the easygui message box to tell the user when the project starts
"""


import easygui
# Dictionary to store the existing menu combos
existing_menu = {"Value": {"Beef Burger", "Fries", "Fizzy drink"},
                 "Cheesy": {"Cheese Burger", "Fries", "Fizzy drink"},
                 "Super": {"Cheese Burger", "Large Fries", "Smoothie"}
                 }

# Welcome statement
easygui.msgbox("Burger Menu Combos", "Menu")
