# inventory management system
# inetilize file
import os  

FILE_NAME = "Inventory mangement.txt"

def initialize_file():
    """Ensure the inventory file exists."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            file.write("Item ID,Name,Quantity,Price\n")
# add item
def add_item():          
    """Add a new item to the inventory."""
    item_id = input("Enter item ID: ")
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    with open(FILE_NAME, "a") as file:
        file.write(f"{item_id},{name},{quantity},{price}\n") 
    print("Item added successfully!\n")
# get item
def get_item(item_id):
    """Retrieve item details by item ID."""
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            data = line.strip().split(",")
            if data[0] == item_id:
                return data
    return None
# view item detail by id
def view_item():
    """View item details."""
    item_id = input("Enter item ID: ")
    item = get_item(item_id)
    if item:
        print("\nItem Details:")
        print(f"Item ID: {item[0]}")
        print(f"Name: {item[1]}")
        print(f"Quantity: {item[2]}")
        print(f"Price: {item[3]}\n")
    else:
        print("Item not found.\n")
# update item
def update_item():
    """Update item details."""
    item_id = input("Enter item ID: ")
    item = get_item(item_id)
    if item:
        new_quantity = int(input("Enter new quantity: "))
        new_price = float(input("Enter new price: "))
        
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
        
        with open(FILE_NAME, "w") as file:
            for line in lines:
                data = line.strip().split(",")
                if data[0] == item_id:
                    file.write(f"{item_id},{item[1]},{new_quantity},{new_price}\n")
                else:
                    file.write(line)
        print("Item updated successfully!\n")
    else:
        print("Item not found.\n")
# remove item from inventry
def remove_item():
    """Remove an item from the inventory."""
    item_id = input("Enter item ID to remove: ")
    item = get_item(item_id)
    if item:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
        
        with open(FILE_NAME, "w") as file:
            for line in lines:
                if line.strip().split(",")[0] != item_id:
                    file.write(line)
        print("Item removed successfully.\n")
    else:
        print("Item not found.\n")
# list of all inventory item
def list_all_items():
    """List all items in the inventory."""
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        if len(lines) <= 1:
            print("No items found.\n")
        else:
            print("\nList of All Items:")
            for line in lines[1:]:
                data = line.strip().split(",")
                print(f"Item ID: {data[0]}, Name: {data[1]}, Quantity: {data[2]}, Price: {data[3]}")
            print()
# main menu
def main_menu():
    """Display the main menu and handle user input."""
    while True:
        print("--- Inventory Management System ---")
        print("1. Add item")
        print("2. View item details")
        print("3. Update item")
        print("4. Remove item")
        print("5. List all items")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            list_all_items()
        elif choice == "6":
            print("Thank you for using the inventory management system!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Initialize the file and run the application
initialize_file()
main_menu()
