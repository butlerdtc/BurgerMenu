""" Burger menu base component V1
Each component gets added after creation and testing.
Functions from components 1, 2, 3 and 4
Created by Robson Butler
27/04/24
"""

import easygui


# Function to ask user what option they would like to choose
def options():
    # Welcome statement
    easygui.msgbox("Burger Menu Combos", "Menu")
    # Ask user to choose an option
    choice = easygui.buttonbox("What would you like to do?",
                               "Menu Options",
                               ["Add combo", "Find combo", "Delete combo",
                                "Show Combos", "Exit"])
    if choice == "Add combo":
        new_details = add_combo_details(existing_menu)
        formatted_details = dictionary_formatter(new_details)
        edit_screen(new_details, formatted_details, existing_menu)
    elif choice == "Find combo":
        easygui.msgbox("Find Combo", "Chosen option")
    elif choice == "Delete combo":
        easygui.msgbox("Delete Combo", "Chosen option")
    elif choice == "Show combos":
        easygui.msgbox("Show all combos", "Chosen option")
    else:
        exit()
    return choice


# Function to format dictionaries
def dictionary_formatter(dictionary):
    # Temporary list to store each formatted dictionary item
    temporary_list = []
    # Sorts through each nested dictionary
    for combo, items in dictionary.items():
        temporary_list.append(f"{combo}:")
        # Sorts through each value in nested dictionary
        for item, price_num in items.items():
            temporary_list.append(f" - " + f"{item}: ${round(price_num, 2)}")
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
            correct_number = round(float_number, 2)
            return correct_number
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


# Function to let user choose if they want to edit the combo or not
def edit_screen(information, organized_combo, original_menu):
    while True:
        # Asks user what they want to choose
        user_choice = easygui.buttonbox(organized_combo, "Combo",
                                        ["Confirm", "Edit", "Cancel"])
        if user_choice == "Confirm":
            original_menu.update(information)
            easygui.msgbox("Combo has been added to menu", "Combo added")
            break
        elif user_choice == "Cancel":
            easygui.msgbox("Combo has not been added", "Combo cancelled")
            break
        else:
            # Runs function to edit the combos details
            combo_info, formatted_combo = edit_details(information,
                                                       organized_combo)
            organized_combo = formatted_combo


# Function to allow user to edit the combos information if selected
def edit_details(combo_info, formatted_combo):
    # User enters what they would like changed
    search = easygui.enterbox(f"What would you like to change from "
                              f"this combo?\n\n{formatted_combo}",
                              "Edit combo").title()
    # Checks if it is the combo name instead of iterating through a list
    if search in combo_info:
        new_name = easygui.enterbox(f"Enter new name for {search} combo",
                                    "New combo name").title()
        combo_info[new_name] = combo_info.pop(search)
    else:
        # If not the combo name it will run through the keys and values inside
        for combo_name, combo_details in combo_info.items():
            # If search is a word it will check if it matches an item
            if search in combo_details:
                new_item = easygui.enterbox(f"Enter new item to replace "
                                            f"{search}").title()
                combo_details[new_item] = combo_details.pop(search)
                break
            # If search is a number it will ask for a new price
            elif search.replace('.', '').isdigit():
                rounded_search = round(float(search), 2)
                # Keeps track if price is found or not
                price_found = False
                # Runs through all pairs to check if it matches a price
                for item, price in combo_details.items():
                    if price == rounded_search:
                        new_price = float_checker(f"Enter new price for "
                                                  f"{rounded_search}",
                                                  "New price")
                        combo_details[item] = new_price
                        price_found = True
                        break
                if not price_found:
                    easygui.msgbox("Please enter a valid option", "Error")
                    return combo_info, formatted_combo
            # If search does not match anything in the combo prints error
            else:
                easygui.msgbox("Please enter a valid option", "Error")
    # Regenerates formatted_details
    formatted_combo = dictionary_formatter(combo_info)
    return combo_info, formatted_combo


# Main routine
existing_menu = {"Value": {"Beef Burger": 5.69, "Fries": 1, "Fizzy drink": 1},
                 "Cheesy": {"Cheese Burger": 6.69, "Fries": 1,
                            "Fizzy drink": 1},
                 "Super": {"Cheese Burger": 6.69, "Large Fries": 2,
                           "Smoothie": 2}
                 }
options()
