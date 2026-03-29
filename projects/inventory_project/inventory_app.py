import json


# -----------------------------
# Inventory Loading & Saving
# -----------------------------

def load_inventory(filename ="inventory.json"):
    """
    Load the inventory from a JSON file.

    If the file does not exist, a default inventory is returned instead.
    This keeps the program usable even on the first run.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        dict: A dictionary representing the inventory.
    """
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            print("Inventory loaded from file.")
            return data
    except FileNotFoundError:
        print("No saved inventory found. Using default inventory.")
        return {
            "apple": 10,
            "banana": 5,
            "orange": 8,
            "pear": 9,
            "blueberries": 7,
            "kiwi": 10,
            "water_melon": 4,
            "dates": 12,
            "grapes": 11,
            "pawpaw": 6
        }
    except json.JSONDecodeError:
        print("Inventory file is corrupted. Starting with an empty inventory.")
        return {}


def save_inventory(inventory, filename="inventory.json"):
    """
    Save the current inventory to a JSON file.

    Args:
        inventory (dict): The inventory data to save.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    try:
        with open(filename, "w") as f:
            json.dump(inventory, f, indent=4)
        print("Inventory saved.")
    except Exception as e:
        print("Something went wrong while saving the inventory:", e)


# -----------------------------
# Inventory Operations
# -----------------------------

def add_item(inventory, item, quantity=1):
    """
    Add a new item to the inventory or update an existing one.

    Args:
        inventory (dict): The current inventory.
        item (str): The item name.
        quantity (int): The quantity to assign to the item.

    Returns:
        dict: The updated inventory.
    """
    if not isinstance(item, str):
        raise TypeError("Item name must be a string.")

    if not isinstance(quantity, int):
        raise TypeError("Quantity must be an integer.")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    inventory[item] = quantity
    print(f"{item} added/updated with quantity {quantity}.")
    return inventory


def remove_item(inventory, item):
    """
    Remove an item from the inventory if it exists.

    Args:
        inventory (dict): The current inventory.
        item (str): The item to remove.

    Returns:
        dict: The updated inventory.
    """
    if item in inventory:
        inventory.pop(item)
        print(f"{item} removed from inventory.")
    else:
        print("Item not found.")
    return inventory


def update_quantity(inventory, item, quantity):
    """
    Update the quantity of an existing item.

    Args:
        inventory (dict): The current inventory.
        item (str): The item to update.
        quantity (int): The new quantity.

    Returns:
        dict: The updated inventory.
    """
    if item not in inventory:
        print("Item not found.")
        return inventory

    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    inventory[item] = quantity
    print(f"{item} updated to {quantity}.")
    return inventory


def view_inventory(inventory):
    """
    Display all items and their quantities.

    Args:
        inventory (dict): The current inventory.

    Returns:
        None
    """
    print("\nCurrent Inventory:")
    if not inventory:
        print("Inventory is empty.")
        return

    for item, qty in inventory.items():
        print(f"{item}: {qty}")


def search_item(inventory, keyword):
    """
    Search for items containing the keyword.

    Args:
        inventory (dict): The current inventory.
        keyword (str): The search term.

    Returns:
        None
    """
    print(f"\nSearch results for '{keyword}':")
    results = {
        item: qty 
        for item, qty in inventory.items() 
        
        if keyword.lower() in item.lower()}

    if results:
        for item, qty in results.items():
            print(f"{item}: {qty}")
    else:
        print("No matching items found.")


def low_stock_alert(inventory, threshold=5):
    """
    Display items with quantities below a given threshold.

    Args:
        inventory (dict): The current inventory.
        threshold (int): The low-stock cutoff.

    Returns:
        None
    """
    print(f"\nItems below stock level {threshold}:")
    low_items = {item: qty for item, qty in inventory.items() if qty < threshold}

    if low_items:
        for item, qty in low_items.items():
            print(f"{item}: {qty}")
    else:
        print("No low-stock items.")


def sort_inventory(inventory, mode="name_asc"):
    """
    Sort the inventory based on the selected mode.

    Args:
        inventory (dict): The current inventory.
        mode (str): Sorting mode.

    Returns:
        None
    """
    print("\nSorted Inventory:")

    if mode == "name_asc":
        sorted_items = sorted(inventory.items(), key=lambda x: x[0])
    elif mode == "name_desc":
        sorted_items = sorted(inventory.items(), key=lambda x: x[0], reverse=True)
    elif mode == "qty_asc":
        sorted_items = sorted(inventory.items(), key=lambda x: x[1])
    elif mode == "qty_desc":
        sorted_items = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    else:
        print("Invalid sorting mode.")
        return

    for item, qty in sorted_items:
        print(f"{item}: {qty}")


# -----------------------------
# Menu + App Controller
# -----------------------------

def display_menu():
    """Show the menu options."""
    print("\nInventory Menu")
    print("1. Add item")
    print("2. Remove item")
    print("3. Update quantity")
    print("4. View inventory")
    print("5. Search items")
    print("6. Low-stock alert")
    print("7. Sort inventory")
    print("8. Exit")


def run_inventory_app():
    """Main loop for the inventory application."""
    inventory = load_inventory()
    running = True

    while running:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            item = input("Enter item name: ")
            try:
                quantity = int(input("Enter quantity: "))
                add_item(inventory, item, quantity)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            item = input("Enter item to remove: ")
            remove_item(inventory, item)

        elif choice == "3":
            item = input("Enter item to update: ")
            try:
                quantity = int(input("Enter new quantity: "))
                update_quantity(inventory, item, quantity)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            sort_choice = input("Sort before viewing? (y/n): ").lower()
            if sort_choice == "y":
                sort_inventory(inventory, "name_asc")
            view_inventory(inventory)

        elif choice == "5":
            keyword = input("Enter search keyword: ")
            search_item(inventory, keyword)

        elif choice == "6":
            low_stock_alert(inventory)

        elif choice == "7":
            print("\nSorting Options:")
            print("1. Name A–Z")
            print("2. Name Z–A")
            print("3. Quantity Low–High")
            print("4. Quantity High–Low")

            mode_choice = input("Choose sorting mode: ")

            modes = {
                "1": "name_asc",
                "2": "name_desc",
                "3": "qty_asc",
                "4": "qty_desc"
            }

            sort_inventory(inventory, modes.get(mode_choice, "name_asc"))

        elif choice == "8":
            save_inventory(inventory)
            print("Exiting program...")
            running = False

        else:
            print("Invalid choice. Please try again.")


# Run the app
if __name__ == "__main__":
    run_inventory_app()