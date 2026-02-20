import json

#Load inventory from a file if it exits, otherwise start with an empty inventory.

try:
    with open("inventory.json", "r") as f:
        inventory = load.json(f)
        print("inventory loaded from file.")
except FileNotFoundError:
    # if file doesnt exist, use this default inventory
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
    print("No saved inventory found, using the default inventory.")

    running = True

    while running:
        print("\n Inventory Menu")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update quantity")
        print("4. View Inventory")
        print("5. Exit")

        # Ask the user to choose an option.

        choice = input("Choose an option: ")

        if choice == "1":
            # Ask for an item name
            item = input("enter item name: ")
            # Ask for quantity and convert to an integer
            quantity = int(input("Enter quantity: "))
            inventory[item] = quantity
            print(item, "added to inventory.")

        elif choice == "2":
            # Ask which item to remove
            item = input("Enter item to remove: ")
            if item in inventory:
                inventory.pop(item)
                print(item, "removed from inventory.")
            else:
                print(item, "not found in nventory.")

        elif choice == "3":
            # Ask which item to update
            item = input("Enter item to update:")
            # check if item is in inventory
            if item in inventory:
                new_quantity = int(input("Enter new quantity: "))
                inventory[item] = new_quantity
                print(item, "quantity upadted")
            else:
                print(item, "not found in inventory.")

        elif choice == "4":
            print("\nCurrent Inventory:")
            for item, qty in inventory.items():
                print(item, ":", qty)
        
        elif choice == "5":
            # save inventory to a file before exiting
            with open("inventory.json", "w") as f:
                json.dump(inventory, f)
                print("inventory saved. Exiting program...")
                running = False