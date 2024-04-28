"""V1 of delete combo
Asks for user input then deletes it from the menu if found
"""

existing_menu = {"Value": {"Beef Burger": 5.69, "Fries": 1, "Fizzy drink": 1},
                 "Cheesy": {"Cheese Burger": 6.69, "Fries": 1,
                            "Fizzy drink": 1},
                 "Super": {"Cheese Burger": 6.69, "Large Fries": 2,
                           "Smoothie": 2}
                 }

delete = input("Enter name of combo to delete: ").title()
if delete in existing_menu:
    existing_menu.pop(delete)
else:
    print("Not found")

print(existing_menu)
