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
    # Asks user what they want to choose
    user_choice = easygui.buttonbox(formatted_details, "New Combo",
                                    ["Confirm", "Edit", "Cancel"])
    if user_choice == "Confirm":
        # Will actually add combo in next version
        easygui.msgbox("New combo has been added to menu", "New combo added")
        break
    elif user_choice == "Cancel":
        easygui.msgbox("New combo has not been added", "Combo cancelled")
        break
    else:
        # User enters what they would like changed
        search = easygui.enterbox(f"What would you like to change from "
                                  f"this combo?\n\n{formatted_details}",
                                  "Edit new combo").title()
        # Empty lists to store the new names or prices
        new_dict_list = []
        new_item_list = []
        new_price_list = []
        # Searches through all entries in dictionary
        for combo_name, combo_details in new_details.items():
            if search == combo_name:
                # Appends user input to list if found as dictionary key
                new_dict_list.append(search)
            elif search in combo_details.keys():
                # Appends user input to list if found as key in dictionary
                new_item_list.append(search)
            else:
                # Try except loop to check if user input is a value in
                # dictionary
                try:
                    if float(search) in combo_details.values():
                        new_price_list.append(float(search))
                    else:
                        print("Please enter an item or price in the combo.")
                except ValueError:
                    print("Invalid input! Please enter a valid option.")
        # Runs through all data in the list
        for combo_name in new_dict_list:
            # User enters new combo name and it replaces the old name
            new_name = (input(f"Enter new name for {combo_name} combo: ")
                        .title())
            new_details[new_name] = new_details.pop(combo_name)
        # Regenerates formatted_details
        formatted_details = dictionary_formatter(new_details)

        # Runs through all data in the list
        for combo_name in new_item_list:
            # Runs through all the pairs in the dictionary
            for combo_key, combo_details in new_details.items():
                if search in combo_details.keys():
                    # User enters new item and it replaces the old item
                    new_item = (input(f"Enter new item to replace {search}")
                                .title())
                    combo_details[new_item] = combo_details.pop(search)
        # Regenerates formatted_details
        formatted_details = dictionary_formatter(new_details)

        # Runs through all prices in the list
        for price in new_price_list:
            # Runs through all pairs in dictionary
            for combo_name, combo_details in new_details.items():
                # Checks the user input is a price in the dictionary
                if price in combo_details.values():
                    # Checks all pairs to find the item(key) the price is for
                    for key, value in combo_details.items():
                        if value == price:
                            # User enters new price and replaces old price
                            new_price = float(input(f"Enter new price for "
                                                    f"{key}: "))
                            combo_details[key] = new_price
                            # The break statements stop the loop from searching
                            # for the same price in other items and combos as
                            # it will only change the first instance of the
                            # price
                            break
                    break
        # Regenerates formatted_details
        formatted_details = dictionary_formatter(new_details)
