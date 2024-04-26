"""V4 of Add combos
Uses V3 and converts the part of the program that asks and stores data the user
enters into a function. Makes progress on the editing part of the component.
Uses 05_float_checker to check if price added is a float or an integer.
"""

import easygui


# Function to format dictionaries
def dictionary_formatter(dictionary):
    # Temporary list to store each formatted dictionary item
    temporary_list = []
    # Sorts through each nested dictionary
    for combo, items in dictionary.items():
        temporary_list.append(f"{combo}:")
        # Sorts through each value in nested dictionary
        for item, price in items.items():
            temporary_list.append(f" - " + f"{item}: ${round(price, 2)}")
        # New line between each nested dictionary
        temporary_list.append("")

    # Removes unnecessary features from each value such as '(' or '['
    list_output = "\n".join(temporary_list)
    return list_output


# Function to check if value entered is a float
def float_checker(question, box_title):
    # Loops until valid input is entered or user selects 'Cancel'
    while True:
        try:
            number = easygui.enterbox(question, box_title)
            # Checks if user selected 'cancel' on easygui box
            if number is None:
                return None
            # Converts entered number to a float
            float_number = float(number)
            return float_number
        except ValueError:
            easygui.msgbox("Please enter a valid price", "Error")


# Function to let user add new combo details
def add_combo_details(menu):
    while True:
        # Dictionary to store entered data until user confirms its correct
        temporary_dict = {}
        new_combo = easygui.enterbox("Enter new combo name: ",
                                     "New Combo",).title()
        # Checks if combo entered is already on the menu
        if new_combo in menu:
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
            new_item_price = float_checker("Enter item price",
                                           "Add price")
            # Adds price and item to dictionary
            temporary_dict[new_combo][new_item_name] = float(new_item_price)
            combo_item_count += 1
        # Will not let user enter more than three items to combo
        if combo_item_count >= 3:
            break
    return temporary_dict


# Main routine
existing_menu = {"Value": {"Beef Burger": 5.69, "Fries": 1, "Fizzy drink": 1},
                 "Cheesy": {"Cheese Burger": 6.69, "Fries": 1,
                            "Fizzy drink": 1},
                 "Super": {"Cheese Burger": 6.69, "Large Fries": 2,
                           "Smoothie": 2}
                 }

# Runs the functions above
new_details = add_combo_details(existing_menu)
formatted_details = dictionary_formatter(new_details)

while True:
    user_choice = easygui.buttonbox(formatted_details, "New Combo",
                                    ["Confirm", "Edit", "Cancel"])
    if user_choice == "Confirm":
        easygui.msgbox("New combo has been added to menu", "New combo added")
        break
    elif user_choice == "Cancel":
        easygui.msgbox("New combo has not been added", "Combo cancelled")
        break
    else:
        search = easygui.enterbox(f"What would you like to change from "
                                  f"this combo?\n\n{formatted_details}",
                                  "Edit new combo").title()
        for combo_name, combo_details in new_details.items():
            if search == combo_name:
                print("Name")
                new_name = input("Enter new name for combo: ")
                new_details[new_name] = new_details.pop(combo_name)
            elif search in combo_details.keys():
                print("Key")
                new_item = input("Enter new item in combo")
            else:
                try:
                    if float(search) in combo_details.values():
                        print("Value")
                    else:
                        print("False")
                except ValueError:
                    print("Invalid input! Please enter a valid option.")
