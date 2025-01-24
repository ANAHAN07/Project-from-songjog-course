def calculator():
    while True:
        print("\nWelcome to the Advanced Calculator!!")                  # Output: Welcome to the Advanced Calculator!
        print("Select an operation:")                                   # Output: Select an operation:
        print("1. Addition (+)")                                        # Output: 1. Addition (+)
        print("2. Subtraction (-)")                                     # Output: 2. Subtraction (-)
        print("3. Multiplication (*)")                                  # Output: 3. Multiplication (*)
        print("4. Division (/)")                                        # Output: 4. Division (/)
        print("5. Square Root (√)")                                     # Output: 5. Square Root (√)
        print("Type 'exit' to quit the calculator.\n")                  # Output: Type 'exit' to quit the calculator.

        choice = input("Enter the number corresponding to the operation (1-5) or 'exit': ").strip().lower()     # Output: Enter the number corresponding to the operation (1-5) or 'exit':  []

        if choice == "exit":
            print("Exiting the calculator. Thank you for using it!")                # Output: Exiting the calculator. Thank you for using it!
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice. Please select a valid operation.")           # Output: Invalid choice. Please select a valid operation.
            continue

        if choice == "5":  
            num = float(input("Enter the number to find the square root: "))    # Output: Enter the number to find the square root: 420
            if num < 0:
                print("Square root of a negative number is not defined.")       # Output: Square root of a negative number is not defined.
            else:
                result = num ** 0.5
                print(f"The square root of {num} is {result:.2f}")          # Output: The square root of 420.0 is 20.49

        else:  
            num_1 = float(input("Enter the first number: "))         # Output: Enter the first number: 34
            num_2 = float(input("Enter the second number: "))           # Output: Enter the second number: 35

            if choice == "1":
                result = num_1 + num_2
                print(f"The result of {num_1} + {num_2} is {result}")       # Output: The result of 34.0 + 35.0 is 69.0
            elif choice == "2":
                result = num_1 - num_2
                print(f"The result of {num_1} - {num_2} is {result}")       # Output: The result of 99.0 - 33.0 is 66.0
            elif choice == "3":
                result = num_1 * num_2
                print(f"The result of {num_1} * {num_2} is {result}")       # Output: The result of 23.0 * 3.0 is 69.0
            elif choice == "4":
                if num_2 == 0:
                    print("Division by zero is not allowed.")           # Output: Division by zero is not allowed.
                else:
                    result = num_1 / num_2
                    print(f"The result of {num_1} / {num_2} is {result}")   # Output: The result of 44.0 / 6.0 is 7.333333333333333
    
    calculator()
