def utility_bills():
    while True:
        print("\nUtility Bills Calculator")                                     # Output: Utility Bills Calculator
        print("1. Electricity Bill")                                            # Output: 1. Electricity Bill
        print("2. Water Bill")                                                  # Output: 2. Water Bill
        print("3. Gas Bill")                                                    # Output: 3. Gas Bill
        print("4. Exit to Main Menu")                                           # Output: 4. Exit to Main Menu

        choice = input("Enter your choice: ").strip()                           # Output: Enter your choice: []

        if choice == "1":
            electricity_bill()
        elif choice == "2":
            water_bill()
        elif choice == "3":
            gas_bill()
        elif choice == "4":
            print("Returning to Main Menu...")                                      # Output: Returning to Main Menu...
            break
        else:
            print("Invalid choice. Please try again.")                                      # Output: Invalid choice. Please try again.


def electricity_bill():
    units = int(input("Enter the number of electricity units used: "))              # Output: Enter the number of electricity units used: 69
    bill = 0

    if units <= 100:
        bill = units * 0.5
    elif units <= 200:
        bill = 100 * 0.5 + (units - 100) * 0.75
    else:
        bill = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1

    print(f"Total electricity bill: ${bill:.2f}")                                       # Output: Total electricity bill: $34.50
    print("Pay the bill as soon as possible to avoid service disruption.")              # Output: Pay the bill as soon as possible to avoid service disruption.

    electricity_bill()

def water_bill():
    units = int(input("Enter the number of cubic meters of water used: "))              # Output: Enter the number of cubic meters of water used: 150
    bill = 0

    if units <= 50:
        bill = units * 0.3
    elif units <= 100:
        bill = 50 * 0.3 + (units - 50) * 0.5
    else:
        bill = 50 * 0.3 + 50 * 0.5 + (units - 100) * 0.75

    print(f"Total water bill: ${bill:.2f}")                                         # Output: Total water bill: $77.50
    print("Ensure timely payment to avoid any service issues.")                     # Output: Ensure timely payment to avoid any service issues.

    water_bill()

def gas_bill():
    units = int(input("Enter the number of cubic meters of gas used: "))                # Output: Enter the number of cubic meters of gas used: 48
    bill = 0

    if units <= 30:
        bill = units * 1
    elif units <= 60:
        bill = 30 * 1 + (units - 30) * 1.5
    else:
        bill = 30 * 1 + 30 * 1.5 + (units - 60) * 2

    print(f"Total gas bill: ${bill:.2f}")                           # Output: Total gas bill: $57.00
    print("Pay promptly to avoid disconnection.")                   # Output: Pay promptly to avoid disconnection.

    gas_bill()

    utility_bills()