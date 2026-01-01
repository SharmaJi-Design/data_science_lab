# 4. Inventory Tracker 
# Imagine a small store inventory like {"apple": 10, "banana": 5, "milk": 2}. Program should allow 
# adding new items, selling items (subtract quantity), and print items that are low in stock (<3).

inventory = {"apple": 10, "banana": 5, "milk": 2}
def display_inventory():
    print("\nCurrent Inventory:")
    for item, qty in inventory.items():
        print(f"{item}: {qty}")     
def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"Added {quantity} of {item}.")
def sell_item(item, quantity):
    if item in inventory:
        if inventory[item] >= quantity:
            inventory[item] -= quantity
            print(f"Sold {quantity} of {item}.")
        else:
            print(f"Not enough {item} in stock to sell {quantity}.")
    else:
        print(f"{item} not found in inventory.")
def low_stock_items():
    print("\nLow Stock Items (less than 3):")
    for item, qty in inventory.items():
        if qty < 3:
            print(f"{item}: {qty}")
while True:
    print("\nInventory Management System")
    print("1. Display Inventory")
    print("2. Add Item")
    print("3. Sell Item")
    print("4. Show Low Stock Items")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        display_inventory()
    elif choice == '2':
        item = input("Enter item name to add: ")
        quantity = int(input("Enter quantity to add: "))
        add_item(item, quantity)
    elif choice == '3':
        item = input("Enter item name to sell: ")
        quantity = int(input("Enter quantity to sell: "))
        sell_item(item, quantity)
    elif choice == '4':
        low_stock_items()
    elif choice == '5':
        print("Exiting Inventory Management System.")
        break
    else:
        print("Invalid choice. Please try again.")

        
           

   




