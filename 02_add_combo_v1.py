"""V1 of Add combos
Allows user to add a new combo if selected and three items - basic structure
"""

import easygui

# Dictionary from existing menu
existing_menu = {"Value": {"Beef Burger": 5.69, "Fries": 1, "Fizzy drink": 1},
                 "Cheesy": {"Cheese Burger": 6.69, "Fries": 1,
                            "Fizzy drink": 1},
                 "Super": {"Cheese Burger": 6.69, "Large Fries": 2,
                           "Smoothie": 2}
                 }

new_combo = easygui.enterbox("Enter new combo name: ", "New Combo", )
existing_menu[new_combo] = {"Items": []}

while True:
    combo_item_count = 0
    while combo_item_count != 3:
        new_item = easygui.enterbox("Enter combo item: ", "Add items")
        # Adds new item to dictionary
        existing_menu[new_combo] = new_item
        combo_item_count += 1
    if combo_item_count >= 3:
        break
print(existing_menu)
