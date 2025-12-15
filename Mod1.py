
#First I created a function to add two numbers.
def addTwoNumbers(number1, number2):
    return number1 + number2

#Same to divide two numbers. Making sure I check for 0 division.
def divideTwoNumbers(number1, number2):
    if number2 == 0:
        return "Cannot divide by zero."
    else:
        return number1 / number2

#Then another function to multiply two numbers.
def multiplyTwoNumbers(number1, number2):
    return number1 * number2

#I created a function to check for the input to add or divide and multiple.
def checkForValidFloat(valueImputed):
    while True:
        try:
            #Check for float.
            return float(input(valueImputed))
        except ValueError:
            #If not prompt again.
            print("Invalid input. Please enter a number.")

#Also created one to check that the operation is either 1 or 2.
def checkForValidOperation(prompt):
    while True:
        try:
            operationRequested = int(input(prompt))
            #Check for 1 or 2. If yes then return that.
            if operationRequested == 1 or operationRequested == 2:
                return operationRequested
            print("Invalid input. Please enter either 1 or 2.")
        except ValueError:
            #Otherwise ask for it again.
            print("Invalid input. Please enter either 1 to add or 2 to multiply and divide.")


if __name__ == '__main__':
    #Now the UI. Prompts for first number and second number.
    #Validates those with function above.
    number1 = checkForValidFloat("Please enter the first number: ")
    number2 = checkForValidFloat("Please enter the second number: ")

    #Now prompts for type of operation
    typeOfOperation = checkForValidOperation("Please enter 1 to add the two numbers, or 2 to divide and multiply the two numbers: ")

    #Use if statement and then run the correct function for the operation.
    if typeOfOperation == 1:
        print("The sum of the two numbers is: " + str(addTwoNumbers(number1, number2)))
    elif typeOfOperation == 2:
        print("The product of the two numbers is: " + str(multiplyTwoNumbers(number1, number2))
              + " and the quotient of the two numbers is: " + str(divideTwoNumbers(number1, number2)))
