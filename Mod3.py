def calculateTip(mealCost):
    """
    Calculates tip and tax for a meal and prints the total.
    """
    # Calculate tip and tax
    tip = mealCost * 0.18
    tax = mealCost * 0.07

    # Calculate total cost
    totalCost = mealCost + tip + tax

    # Print everything out
    print(f"Meal cost : {mealCost:.2f}")
    print(f"Tip       : {tip:.2f}")
    print(f"Tax       : {tax:.2f}")
    print("--------------------")
    print(f"Total cost: {totalCost:.2f}")


def calculateAlarmHour(currentHour, waitForAlarm):
    """
    Calculates the time on a 24-hour clock after a specific wait period.
    """
    # Calculate the new hour
    newHour = (currentHour + waitForAlarm) % 24

    # Print everything out
    print(f"Current hour  : {currentHour}")
    print(f"Wait for alarm: {waitForAlarm}")
    print(f"Alarm hour    : {newHour}")


def checkForValidFloat(prompt):
    """
    Prompts for a valid float input.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def checkForValidOperation(prompt):
    """
    Prompts for a valid operation selection (1 or 2).
    """
    while True:
        try:
            operationRequested = int(input(prompt))
            if operationRequested in (1, 2):
                return operationRequested
            print("Invalid input. Please enter either 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter either 1 or 2.")


def checkForValid24Hour(prompt):
    """
    Prompts for a valid hour between 0 and 23.
    """
    while True:
        try:
            valid24 = int(input(prompt))
            if 0 <= valid24 < 24:
                return valid24
            print("Invalid input. Please enter a value between 0 and 23.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def checkForValidHour(prompt):
    """
    Prompts for a valid non-negative integer for hours.
    """
    while True:
        try:
            hour = int(input(prompt))
            if hour >= 0:
                return hour
            print("Invalid input. Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == '__main__':
    operation = checkForValidOperation(
        "Enter 1 for tip/tax, or 2 for alarm clock: ")

    if operation == 1:
        mealCost = checkForValidFloat("Enter meal cost: ")

        # Call the calculateTip function
        calculateTip(mealCost)

    else:
        currentHour = checkForValid24Hour("Enter current hour (0–23): ")
        waitForAlarm = checkForValidHour("Enter hours to wait: ")

        # Call the calculateAlarmHour function
        calculateAlarmHour(currentHour, waitForAlarm)
