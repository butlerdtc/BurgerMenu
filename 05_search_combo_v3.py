"""V3 of search menu component
Converts V2 to a function and uses the formatter from 03_formatter_v2 to
display the combo found
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
            temporary_list.append(f" - " + f"{item}: ${price:.2f}")
        # New line between each nested dictionary
        temporary_list.append("")

    # Removes unnecessary features from each value such as '(' or '['
    list_output = "\n".join(temporary_list)
    easygui.msgbox(f"{list_output}")


# Function to search the menu for a combo
def search_menu(menu_):
    # Loops until a combo has been found
    while True:
        search = easygui.enterbox("Please enter the name of the combo",
                                  "Search menu").title()
        # Checks if combo is on the menu
        if search in menu_:
            easygui.msgbox("Combo has been found", "Combo found")
            found_combo = menu_[search]
            # Assigns the combo name as key to the items in the combo
            full_combo = {search: found_combo}
            break
        else:
            easygui.msgbox("That combo was not found\nPlease enter a "
                           "combo on the menu", "Combo not found")
    return full_combo


# Main routine
existing_menu = {"Value": {"Beef Burger": 5.69, "Fries": 1, "Fizzy drink": 1},
                 "Cheesy": {"Cheese Burger": 6.69, "Fries": 1,
                            "Fizzy drink": 1},
                 "Super": {"Cheese Burger": 6.69, "Large Fries": 2,
                           "Smoothie": 2}
                 }

combo_found = search_menu(existing_menu)
dictionary_formatter(combo_found)
