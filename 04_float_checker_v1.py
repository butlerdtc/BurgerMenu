"""V1 of a component to check if user input is a float and react accordingly"""

import easygui


# Function to check if value entered is a float
def float_checker(question):
    # Loops until valid input is entered or user selects 'Cancel'
    while True:
        try:
            number = easygui.enterbox(question)
            # Checks if user selected 'cancel' on easygui box
            if number is None:
                return None
            # Converts entered number to a float
            float_number = float(number)
            return float_number
        except ValueError:
            easygui.msgbox("Please enter a valid price", "Error")


price = float_checker("Enter item price: ")
if price is not None:
    easygui.msgbox("Success")
else:
    easygui.msgbox("Cancelled")
