"""V1 of Add combos
Allows user to add a new combo if selected
"""

import easygui

# Dictionary from existing menu
existing_menu = {"Value": {"Beef Burger": 5.69, "Fries": 1, "Fizzy drink": 1},
                 "Cheesy": {"Cheese Burger": 6.69, "Fries": 1,
                            "Fizzy drink": 1},
                 "Super": {"Cheese Burger": 6.69, "Large Fries": 2,
                           "Smoothie": 2}
                 }


while True:
    # Dictionary to store entered data until user confirms its correct
    empty_dict = {}
    new_combo = easygui.enterbox("Enter new combo name: ", "New Combo", )
    # Checks if combo entered is already on the menu
    if new_combo in existing_menu:
        easygui.msgbox("This combo is already on the menu\n "
                       "Please enter a new combo name")
        continue
    else:
        # Adds new combo name to menu (dictionary)
        empty_dict[new_combo] = {}
        break

while True:
    combo_item_count = 0
    while combo_item_count != 3:
        new_item = easygui.enterbox("Enter combo item: ", "Add items")
        # Adds new contact first name to dictionary
        empty_dict[new_combo][] = new_item.title()
        combo_item_count += 1
    if combo_item_count >= 3:
        break

