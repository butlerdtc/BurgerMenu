"""V1 of show menu
Uses formatter from 03_formatter_v2 and no need for its own function as its
only two new lines of code
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
    return list_output


# Main routine
existing_menu = {"Value": {"Beef Burger": 5.69, "Fries": 1, "Fizzy drink": 1},
                 "Cheesy": {"Cheese Burger": 6.69, "Fries": 1,
                            "Fizzy drink": 1},
                 "Super": {"Cheese Burger": 6.69, "Large Fries": 2,
                           "Smoothie": 2}
                 }
whole_menu = dictionary_formatter(existing_menu)
easygui.msgbox(whole_menu, "Entire menu")
