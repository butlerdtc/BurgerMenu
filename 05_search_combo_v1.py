"""V1 of search menu component
Asks user for input then says if it is found or not
"""

existing_menu = {"Value": {"Beef Burger": 5.69, "Fries": 1, "Fizzy drink": 1},
                 "Cheesy": {"Cheese Burger": 6.69, "Fries": 1,
                            "Fizzy drink": 1},
                 "Super": {"Cheese Burger": 6.69, "Large Fries": 2,
                           "Smoothie": 2}
                 }

# Asks user for combo to search for
search = input("Please enter the name of the combo: ").title()
# Checks if combo searched is on the menu
if search in existing_menu:
    print("Found")
else:
    print("False")
