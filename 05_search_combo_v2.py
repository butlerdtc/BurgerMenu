"""V2 of search menu component
Converts print statements to easygui and loops until user cancels or input is
found in existing menu
"""
import easygui

existing_menu = {"Value": {"Beef Burger": 5.69, "Fries": 1, "Fizzy drink": 1},
                 "Cheesy": {"Cheese Burger": 6.69, "Fries": 1,
                            "Fizzy drink": 1},
                 "Super": {"Cheese Burger": 6.69, "Large Fries": 2,
                           "Smoothie": 2}
                 }
# Loops until a combo has been found
while True:
    search = easygui.enterbox("Please enter the name of the combo",
                              "Search menu").title()
    # Checks if combo is on the menu
    if search in existing_menu:
        easygui.msgbox("Combo has been found", "Combo found")
        break
    else:
        easygui.msgbox("That combo was not found on the menu\nPlease "
                       "enter a combo on the menu", "Combo not found")
