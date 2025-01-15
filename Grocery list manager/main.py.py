# Shop inventory data
shop_inventory = {                                                                              # output: Enter your choice (1-8): 1
    "fruits": ["apple", "banana", "orange", "mango", "dragon fruit", "grape"],                  # output: Fruits: apple, banana, orange, mango, dragon fruit, grape
    "vegetables": ["carrot", "potato", "onion", "tomato", "fullkopi", "patakofi"],              # output: Vegetables: carrot, potato, onion, tomato, fullkopi, patakofi
    "dairy": ["milk", "cheese", "yogurt", "butter"],                                            # output: Dairy: milk, cheese, yogurt, butter
    "grains": ["rice", "wheat", "oats", "barley"],                                              # output: Grains: rice, wheat, oats, barley
    "beverages": ["tea", "coffee", "juice", "water", "MOJO"],                                   # output: Beverages: tea, coffee, juice, water, MOJO
    "snacks": ["oreo", "cookies", "noodles", "chips", "toast"],                                 # output: Snacks: oreo, cookies, noodles, chips, toast
    "meat & fish": ["chicken & poultry", "premium perishables", "meat", "dried fish"],          # output: Meat & fish: chicken & poultry, premium perishables, meat, dried fish
}

# Grocery list data
grocery_list = {}


# Functions for grocery list management
def add_item(grocery_list):                                                                                                                   # output: Enter your choice (1-8): 2
    category = input("Enter the category (e.g., fruits, vegetables, dairy, grains, beverages, snacks, meat & fish): ").strip().lower()        # output: Enter the category (e.g., fruits, vegetables, dairy, grains, beverages, snacks, meat & fish): fruits
    item = input("Enter the item to add: ").strip()                                                                                           # output: Enter the item to add: grape, orange, apple
    if item in [i for sublist in grocery_list.values() for i in sublist]:
        print(f"{item} is already in the list. Duplicate entries are not allowed.")                                                           # output: grape is already in the list. Duplicate entries are not allowed
    else:
        if category not in grocery_list:
            grocery_list[category] = []
        grocery_list[category].append(item)
        print(f"{item} has been added to the {category} category.")                                                                           # output: grape, orange, apple has been added to the fruits category


def remove_item(grocery_list):                                                                                # output: Enter your choice (1-8): 3
    category = input("Enter the category of the item to remove: ").strip().lower()                            # output: Enter the category of the item to remove: dairy
    item = input("Enter the item to remove: ").strip()                                                        # output: Enter the item to remove: yogurt / Enter the item to remove: milk
    if category in grocery_list and item in grocery_list[category]:
        grocery_list[category].remove(item)
        if not grocery_list[category]:  # Remove empty categories
            del grocery_list[category]
        print(f"{item} has been removed from the {category} category.")                                       # output: yogurt has been removed from the dairy category.
    else:
        print(f"{item} is not in the {category} category.")                                                   # output: milk is not in the dairy category.


def view_list(grocery_list):                                                        # output: Enter your choice (1-8): 4 
    if grocery_list:
        print("\nCurrent Grocery List:")                                            # output: Current Grocery List:
        for category, items in grocery_list.items():
            print(f"{category.capitalize()}:")                                      # output: Fruits:
            for item in items:                                                                
                print(f"  - {item}")                                                # output: - grape, orange, apple
    else:
        print("The grocery list is empty.")                                         # output: The grocery list is empty.

def check_item(grocery_list):                                                                   # output: Enter your choice (1-8): 5
    item = input("Enter the item to check: ").strip().lower()                                   # output: Enter the item to check: chicken / Enter the item to check: chips
    found = False
    for category, items in grocery_list.items():
        
        if item in [i.lower() for i in items]:  
            print(f"{item.capitalize()} is in the {category.capitalize()} category.")           # output: chicken is in the meat & fish category.
            found = True
            break
    if not found:
        print(f"{item.capitalize()} is not in the list.")                                       # output: chips is not in the list.             


def display_total_items(grocery_list):                                                          # output: Enter your choice (1-8): 6
    total_items = sum(len(items) for items in grocery_list.values())
    print(f"\nThe total number of items in the grocery list is: {total_items}")                 # output: The total number of items in the grocery list is: 7


# Functions for shop inventory management
def display_shop_inventory():                                                                                                                            # output: Enter your choice (1-3): 1
    """Display all items available in the shop."""
    print("\nItems available in the shop:")                                                                                                              # output: Items available in the shop:
    for category, items in shop_inventory.items():
        print(f"{category.capitalize()}: {', '.join(items)}")                                                                                            # output: category: item, item, item (this will show shop_inventory)


def add_item_to_shop():                                                                                                                                  # output: Enter your choice (1-3): 2
    """Add a new item to the shop inventory."""
    category = input("Enter the category (e.g., fruits, vegetables, dairy, grains, beverages, snacks, meat & fish): ").strip().lower()                   # output: Enter the category (e.g., fruits, vegetables, dairy, grains, beverages, snacks, meat & fish): electronics / Enter the category (e.g., fruits, vegetables, dairy, grains, beverages, snacks, meat & fish): Dairy
    item = input("Enter the item to add: ").strip().lower()                                                                                              # output: Enter the item to add: RTX 4090, AMD ryzen 9900, corsair 64gb ddr5  / Enter the item to add: milk
    if category not in shop_inventory:
        shop_inventory[category] = []
    if item in shop_inventory[category]:
        print(f"{item.capitalize()} is already available in the {category} category.")                                                                    # output: Milk is already available in the dairy category.
    else:
        shop_inventory[category].append(item)
        print(f"{item.capitalize()} has been added to the {category} category.")                                                                          # output: Rtx 4090, amd ryzen 9900, corsair 64gb ddr5 has been added to the electronics category.


# Main Interface Function
def display_interface():
    print("\t\nGrocery List Manager")                       # output: Grocery List Manager
    print("1. Items available in the grocery shop")         # output: 1. Items available in the grocery shop
    print("2. Add item to the grocery list")                # output: 2. Add item to the grocery list
    print("3. Remove item from the grocery list")           # output: 3. Remove item from the grocery list
    print("4. View current grocery list")                   # output: 4. View current grocery list
    print("5. Check if an item is in the list")             # output: 5. Check if an item is in the list
    print("6. Display total number of items")               # output: 6. Display total number of items
    print("7. Exit")                                        # output: 7. Exit
    print("8. Admin Panel\n")                               # output: 8. Admin Panel


# Main Program
def main():
    while True:
        display_interface()
        choice = input("Enter your choice (1-8): ").strip()                                 # output: Enter your choice (1-8): []

        if choice == "1":
            display_shop_inventory()
        elif choice == "2":
            add_item(grocery_list)
        elif choice == "3":
            remove_item(grocery_list)
        elif choice == "4":
            view_list(grocery_list)
        elif choice == "5":
            check_item(grocery_list)
        elif choice == "6":
            display_total_items(grocery_list)
        elif choice == "7":
            print("Exiting Grocery List Manager. Goodbye!")                     # output: Exiting Grocery List Manager. Goodbye!
            break
        elif choice == "8":
            print("\nAdmin Panel")                                              # output: Admin Panel
            print("1. View shop inventory")                                     # output: 1. View shop inventory
            print("2. Add item to shop inventory")                              # output: 2. Add item to shop inventory
            print("3. Back to main menu")                                       # output: 3. Back to main menu
            admin_choice = input("Enter your choice (1-3): ").strip()           # output: Enter your choice (1-3): []
            if admin_choice == "1":
                display_shop_inventory()
            elif admin_choice == "2":
                add_item_to_shop()
            elif admin_choice == "3":
                continue
            else:
                print("Invalid choice in Admin Panel. Please try again.")           # output: Invalid choice in Admin Panel. Please try again.
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")         # output: Invalid choice. Please enter a number between 1 and 8.


if __name__ == "__main__":
    main()

