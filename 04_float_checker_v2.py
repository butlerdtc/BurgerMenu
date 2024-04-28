"""V2 of the float checker
This is a case of trialling where instead of try, except it uses isnumeric()
to achieve the same result of checking if user input is a float
"""

import easygui


# Function to check if value entered is a float
def float_checker(question):
    while True:
        number = easygui.enterbox(question)
        # Checks if user selected 'cancel' on easygui box
        if number is None:
            return None
        # This checks if the characters are numbers and if there is only one
        # decimal point and if the decimal point is removed that only numbers
        # are left
        if number.isnumeric() or (number.count('.') == 1 and
                                  number.replace('.', '').isnumeric()):
            # Converts number to a rounded float
            float_number = round(float(number), 2)
            return float_number
        else:
            easygui.msgbox("Please enter a valid price", "Error")


# Main routine
result = float_checker("Enter a float value")
print("Result:", result)
