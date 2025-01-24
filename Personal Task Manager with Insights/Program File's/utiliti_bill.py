def utility_bills():
    """Utility Bills Calculator: Handles electricity, water, and gas bills."""
    while True:
        print("\nUtility Bills Calculator")
        print("1. Electricity Bill")
        print("2. Water Bill")
        print("3. Gas Bill")
        print("4. Exit to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            electricity_bill()
        elif choice == "2":
            water_bill()
        elif choice == "3":
            gas_bill()
        elif choice == "4":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")


def electricity_bill():
    """Calculate the electricity bill based on usage."""
    units = int(input("Enter the number of electricity units used: "))
    bill = 0

    if units <= 100:
        bill = units * 0.5
    elif units <= 200:
        bill = 100 * 0.5 + (units - 100) * 0.75
    else:
        bill = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1

    print(f"Total electricity bill: ${bill:.2f}")
    print("Pay the bill as soon as possible to avoid service disruption.")


def water_bill():
    """Calculate the water bill based on usage in cubic meters."""
    units = int(input("Enter the number of cubic meters of water used: "))
    bill = 0

    if units <= 50:
        bill = units * 0.3
    elif units <= 100:
        bill = 50 * 0.3 + (units - 50) * 0.5
    else:
        bill = 50 * 0.3 + 50 * 0.5 + (units - 100) * 0.75

    print(f"Total water bill: ${bill:.2f}")
    print("Ensure timely payment to avoid any service issues.")


def gas_bill():
    """Calculate the gas bill based on usage in cubic meters."""
    units = int(input("Enter the number of cubic meters of gas used: "))
    bill = 0

    if units <= 30:
        bill = units * 1
    elif units <= 60:
        bill = 30 * 1 + (units - 30) * 1.5
    else:
        bill = 30 * 1 + 30 * 1.5 + (units - 60) * 2

    print(f"Total gas bill: ${bill:.2f}")
    print("Pay promptly to avoid disconnection.")
