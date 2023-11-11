# Store Math Operator Functions in Dictionay
operators = {
    'add':
    lambda num1, num2: num1 + num2,
    'diff':
    lambda num1, num2: num1 - num2,
    'prod':
    lambda num1, num2: num1 * num2,
    'div':
    lambda num1, num2: num1 / num2
    if num2 != 0 else "Error: Cannot divide by zero"
}


# Display Choices Operator Function
def displayOperatorChoices():
    operations = ["Addition", "Subtraction",
                  "Multipication", "Division", "Exit"]
    print("Select Operation:")
    for i, operation in enumerate(operations, start=1):
        print(f"\n\t {i}: {operation}")


# Validate Numerical Input Function
def validateNumericInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("\nError: Please Enter a Valid Number\n")


# Display Result based on Choice
# def performOperation(choice, num1, num2, operator):
#   if choice == 1:
#     return f"\n {num1} + {num2} = {operator['add'](num1, num2)} \n"
#   elif choice == 2:
#     return f"\n {num1} - {num2} = {operator['diff'](num1, num2)} \n"
#   elif choice == 3:
#     return f"\n {num1} * {num2} = {operator['prod'](num1, num2)} \n"
#   elif choice == 4:
#     if num2 != 0:
#       return f"\n {num1} / {num2} = {operator['div'](num1, num2)} \n"
#     else:
#       return "\nError: Cannot divide by zero\n"


# Perform Operation and Return Result
def performOperation(choice, num1, num2, operator):
    format_num1 = f"{num1:.0f}" if num1.is_integer() else str(num1)
    format_num2 = f"{num2:.0f}" if num2.is_integer() else str(num2)

    if choice == 1:
        result = operator['add'](num1, num2)
        formatted_result = f"\n {format_num1} + {format_num2} = {result:.0f} \n" if result.is_integer(
        ) else f"\n {format_num1} + {format_num2} = {result} \n"
        return formatted_result
    elif choice == 2:
        result = operator['diff'](num1, num2)
        formatted_result = f"\n {format_num1} - {format_num2} = {result:.0f} \n" if result.is_integer(
        ) else f"\n {format_num1} - {format_num2} = {result} \n"
        return formatted_result
    elif choice == 3:
        result = operator['prod'](num1, num2)
        formatted_result = f"\n {format_num1} * {format_num2} = {result:.0f} \n" if result.is_integer(
        ) else f"\n {format_num1} * {format_num2} = {result} \n"
        return formatted_result
    elif choice == 4:
        if num2 != 0:
            result = operator['div'](num1, num2)
            formatted_result = f"\n {format_num1} / {format_num2} = {result:.0f} \n" if result.is_integer(
            ) else f"\n {format_num1} / {format_num2} = {result} \n"
            return formatted_result
        else:
            return "\nError: Cannot divide by zero\n"


# Calculator Main Function
def calculator():
    print("Simple Calculator \n")
    displayOperatorChoices()  # Displaying Operator Choices
    while True:

        choice = input("\nEnter Choice: 1 - 5: ")
        if choice == '5':  # If True exit Calculator
            print("\nExiting Calculator\n")
            break

        # Catching Error for Non-Numeric Inputs
        try:
            choice = int(choice)  # Convert String to Integer
            if choice in range(1, 5):  # Checking if Choice is in range 1 - 4
                num1 = validateNumericInput("\nEnter First Number: ")
                num2 = validateNumericInput("\nEnter Second Number: ")

                # Call performOperation() and store it to result
                result = performOperation(choice, num1, num2, operators)
                print(f"\n{result}\n")

            else:  # print if input not in range 1 - 4
                print("\nError: Please Enter Choices 1 - 5 \n")
        except ValueError:  # do this if Input is non-numeric
            print("\nError: Please Enter a Valid Number for Choices!\n")


calculator()
