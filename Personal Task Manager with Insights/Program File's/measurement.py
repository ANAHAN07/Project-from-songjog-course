def measurement ():
    while True:
        print("\nWelcome to the Ultimate Tool!")                        # Output: Welcome to the Ultimate Tool!
        print("1. Discount Calculator")                                 # Output: 1. Discount Calculator
        print("2. Percentage Calculator")                               # Output: 2. Percentage Calculator
        print("Type 'exit' to quit the program.\n")                     # Output: Type 'exit' to quit the program.

        choice = input("Enter your choice (1-2) or 'exit': ").strip().lower()           # Output: Enter your choice (1-2) or 'exit': []

        if choice == "exit":
            print("Exiting the program. Thank you for using it!")                   # Output: Exiting the program. Thank you for using it!
            break
        elif choice == "1":
            discount_calculator()
        elif choice == "2":
            percentage_calculator()
        else:
            print("Invalid choice. Please select a valid option.")              # Output: Invalid choice. Please select a valid option.

def discount_calculator():
    print("\nDiscount Calculator")                                                  # Output: Discount Calculator
    original_price = float(input("Enter the original price: "))                     # Output: Enter the original price: 50900
    discount_rate = float(input("Enter the discount percentage: "))                 # Output: Enter the discount percentage: 25.8
    discount_amount = (original_price * discount_rate) / 100
    final_price = original_price - discount_amount
    print(f"Discount Amount: {discount_amount:.2f}, Final Price: {final_price:.2f}")            # Output: Discount Amount: 13132.20, Final Price: 37767.80

    discount_calculator()

def percentage_calculator():
    print("\nPercentage Calculator")                                # Output: Percentage Calculator
    total = float(input("Enter the total value: "))                 # Output: Enter the total value: 4090
    part = float(input("Enter the part value: "))                   # Output: Enter the part value: 444
    percentage = (part / total) * 100
    print(f"The percentage is {percentage:.2f}%")                   # Output: The percentage is 10.86%

    percentage_calculator()

    measurement()