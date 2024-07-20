def calculator():
    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2 if num2 != 0 else "Error! Division by zero."
        else:
            print("Invalid operation choice. Please try again.")
            continue

        print(f"The result is: {result}")

        play_again = input("Do you want to perform another calculation? (yes/no): ").lower()
        if play_again == 'yes':
            continue
        elif play_again=="no":
            break
        else:
            print("Invalid choice")
            break

    print("Thanks for using the calculator!")

calculator()
