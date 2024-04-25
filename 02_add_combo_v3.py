"""V3 of Add combos
Uses V2 and function from 03_formatter_v2 to display new combo.
"""

import easygui


# Function to format dictionaries
def dictionary_formatter(menu):
    # Temporary list to store each formatted dictionary item
    temporary_list = []
    # Sorts through each nested dictionary
    for combo, items in menu.items():
        temporary_list.append(f"{combo}:")
        # Sorts through each value in nested dictionary
        for item, price in items.items():
            temporary_list.append(f" - " + f"{item}: ${round(price, 2)}")
        # New line between each nested dictionary
        temporary_list.append("")

    # Removes unnecessary features from each value such as '(' or '['
    list_output = "\n".join(temporary_list)
    return list_output


# Dictionary from existing menu
existing_menu = {"Value": {"Beef Burger": 5.69, "Fries": 1, "Fizzy drink": 1},
                 "Cheesy": {"Cheese Burger": 6.69, "Fries": 1,
                            "Fizzy drink": 1},
                 "Super": {"Cheese Burger": 6.69, "Large Fries": 2,
                           "Smoothie": 2}
                 }

while True:
    # Dictionary to store entered data until user confirms its correct
    temporary_dict = {}
    new_combo = easygui.enterbox("Enter new combo name: ",
                                 "New Combo",).title()
    # Checks if combo entered is already on the menu
    if new_combo in existing_menu:
        easygui.msgbox("This combo is already on the menu\n "
                       "Please enter a new combo name")
        continue
    else:
        # Adds new combo name to menu (dictionary)
        temporary_dict[new_combo] = {}
        break

while True:
    # Tracks how many items have been added
    combo_item_count = 0
    # Loops until three items have been added
    while combo_item_count != 3:
        new_item_name = easygui.enterbox("Enter combo item: ",
                                         "Add item").title()
        new_item_price = easygui.enterbox("Enter combo price: ",
                                          "Add price").title()
        # Adds price and item to dictionary
        temporary_dict[new_combo][new_item_name] = float(new_item_price)
        combo_item_count += 1
    # Will not let user enter more than three items to combo
    if combo_item_count >= 3:
        break

while True:
    user_choice = easygui.buttonbox(dictionary_formatter(temporary_dict),
                                    "New Combo",
                                    ["Confirm", "Edit", "Cancel"])
    if user_choice == "Confirm":
        easygui.msgbox("New combo has been added to menu", "New combo added")
        break
    elif user_choice == "Cancel":
        easygui.msgbox("New combo has not been added", "Combo cancelled")
        break
    else:
        # Temporary empty print statement until code has been brainstormed
        print()
