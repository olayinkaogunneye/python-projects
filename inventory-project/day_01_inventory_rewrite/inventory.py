import json

# Try to load inventory from a file.
try:
    with open("inventory.json", "r") as f:
        inventory = json.load(f)
        print("Inventory loaded from file.")
except FileNotFoundError:
    # If the file doesn't exist, use this default inventory.
    inventory = {
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
    print("No saved inventory found. Using default inventory.")

# This variable controls whether the program keeps running.
# True = keep looping, False = stop.
running = True

# Start a loop that will continue until running becomes False.
while running:

    # Print the menu options for the user.
    print("\nInventory Menu")
    print("1. Add item")
    print("2. Remove item")
    print("3. Update quantity")
    print("4. View inventory")
    print("5. Exit")

    # Ask the user to choose an option.
    # input() always returns a string.
    choice = input("Choose an option: ")

    # OPTION 1: Add a new item to the inventory.
    if choice == "1":
        # Ask for the item name.
        item = input("Enter item name: ")
        # Ask for the quantity and convert it to an integer.
        quantity = int(input("Enter quantity: "))
        # Add or update the item in the dictionary.
        inventory[item] = quantity
        print(item, "added to inventory.")

    # OPTION 2: Remove an item from the inventory.
    elif choice == "2":
        # Ask which item to remove.
        item = input("Enter item to remove: ")
        # Check if the item exists in the dictionary.
        if item in inventory:
            # Remove the item using pop(key).
            inventory.pop(item)
            print(item, "removed from inventory.")
        else:
            # If the item doesn't exist, show this message.
            print("Item not found.")

    # OPTION 3: Update the quantity of an existing item.
    elif choice == "3":
        # Ask which item to update.
        item = input("Enter item to update: ")
        # Check if the item exists.
        if item in inventory:
            # Ask for the new quantity.
            new_qty = int(input("Enter new quantity: "))
            # Update the dictionary value.
            inventory[item] = new_qty
            print(item, "updated to", new_qty)
        else:
            print("Item not found.")

    # OPTION 4: View all items in the inventory.
    elif choice == "4":
        print("\nCurrent Inventory:")
        # Loop through each key-value pair in the dictionary.
        for item, qty in inventory.items():
            print(item, ":", qty)

    # OPTION 5: Exit the program.
    elif choice == "5":
        # Save inventory to a file before exiting.
        with open("inventory.json", "w") as f:
            json.dump(inventory, f)
        print("Inventory saved. Exiting program...")
        running = False