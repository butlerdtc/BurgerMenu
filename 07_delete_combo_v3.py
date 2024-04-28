"""V3 of delete combo
Converts V2 to a function
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


# Function to search the menu for a combo
def search_menu(menu_, box_title_2):
    # Loops until a combo has been found
    while True:
        search = easygui.enterbox("Please enter the name of the combo",
                                  box_title_2).title()
        # Checks if combo is on the menu
        if search in menu_:
            found_combo = menu_[search]
            # Assigns the combo name as key to the items in the combo
            full_combo = {search: found_combo}
            break
        else:
            easygui.msgbox("That combo was not found\nPlease enter a "
                           "combo on the menu", "Combo not found")
    return full_combo, search


# Function to confirm combo deletion
def delete_combo(full_menu):
    delete, name = search_menu(full_menu, "Delete combo")
    present = dictionary_formatter(delete)
    if name in full_menu:
        choice = easygui.buttonbox(f"This is the combo you want to delete\n\n"
                                   f"{present}", "Delete combo",
                                   ["Yes", "No"])
        if choice == "Yes":
            confirm = easygui.buttonbox(f"Confirm you want to delete {name}",
                                        "Confirmation",
                                        ["Delete", "Cancel"])
            if confirm == "Delete":
                full_menu.pop(name)
            else:
                easygui.msgbox(f"{name} was not deleted",
                               "Deletion cancelled")
        else:
            easygui.msgbox(f"{name} was not deleted",
                           "Deletion cancelled")
    else:
        easygui.msgbox("That combo was not found\nPlease enter a combo on "
                       "the menu", "Combo not found")


# Main routine
existing_menu = {"Value": {"Beef Burger": 5.69, "Fries": 1, "Fizzy drink": 1},
                 "Cheesy": {"Cheese Burger": 6.69, "Fries": 1,
                            "Fizzy drink": 1},
                 "Super": {"Cheese Burger": 6.69, "Large Fries": 2,
                           "Smoothie": 2}
                 }
delete_combo(existing_menu)
