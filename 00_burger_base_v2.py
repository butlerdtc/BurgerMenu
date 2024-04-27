""" Burger menu base component V2
Each component gets added after creation and testing.
Based on 00_burger_base_v1, added function from component 5 and 6
Created by Robson Butler
27/04/24
"""

import easygui


# Function to ask user what option they would like to choose
def options(menu):
    # Welcome statement
    easygui.msgbox("Burger Menu Combos", "Menu")
    while True:
        # Ask user to choose an option
        choice = easygui.buttonbox("What would you like to do?",
                                   "Menu Options",
                                   ["Add combo", "Find combo", "Delete combo",
                                    "Show combos", "Exit"])
        if choice == "Add combo":
            new_details = add_combo_details(menu)
            formatted_details_1 = dictionary_formatter(new_details)
            edit_screen(new_details, formatted_details_1, menu)
        elif choice == "Find combo":
            combo_found = search_menu(menu)
            formatted_details_2 = dictionary_formatter(combo_found)
            edit_screen(combo_found, formatted_details_2, menu)
        elif choice == "Delete combo":
            easygui.msgbox("Delete Combo", "Chosen option")
        elif choice == "Show combos":
            whole_menu = dictionary_formatter(menu)
            easygui.msgbox(whole_menu, "Entire menu")
        else:
            exit()


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


# Function to let user choose if they want to edit the combo or not
def edit_screen(information, organized_combo, original_menu):
    while True:
        # Asks user what they want to choose
        user_choice = easygui.buttonbox(organized_combo, "Combo",
                                        ["Confirm", "Edit", "Cancel"])
        if user_choice == "Confirm":
            original_menu.update(information)
            easygui.msgbox("Combo has been confirmed", "Combo confirmed")
            break
        elif user_choice == "Cancel":
            easygui.msgbox("Combo has not been added/updated",
                           "Combo cancelled")
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
                return combo_info, formatted_combo
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
options(existing_menu)
