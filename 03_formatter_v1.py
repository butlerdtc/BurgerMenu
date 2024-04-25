"""V1 of a program to format a dictionary to look aesthetically pleasing """

# Uses existing menu as a base to write program
existing_menu = {"Value": {"Beef Burger": 5.69, "Fries": 1, "Fizzy drink": 1},
                 "Cheesy": {"Cheese Burger": 6.69, "Fries": 1,
                            "Fizzy drink": 1},
                 "Super": {"Cheese Burger": 6.69, "Large Fries": 2,
                           "Smoothie": 2}
                 }

for combo, items in existing_menu.items():
    print(f"{combo}:")
    for item, price in items.items():
        print(f"  - {item}: ${price:.2f}")
    print()
