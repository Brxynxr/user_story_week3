# app.py - Program entry point.

from services import (
    add_product,
    show_inventory,
    find_product,
    update_product,
    delete_product,
    calculate_statistics,
)
from files import save_csv, load_csv, apply_load

# Main list
inventory = []

#Input Helper Functions

def ask_float(message):
    value = float(input(message))
    if value < 0:
        raise ValueError("Value cannot be negative.")
    return value

def ask_int(message):
    value = int(input(message))
    if value < 0:
        raise ValueError("Value cannot be negative.")
    return value

#Menu Option Functions

def option_add():
    name = input("Product name: ").strip()
    price = ask_float("Price: ")
    quantity = ask_int("Quantity: ")
    add_product(inventory, name, price, quantity)

def option_search():
    name = input("Search for: ").strip()
    product = find_product(inventory, name)
    if product:
        print(f"\nFound → Name: {product['name']} | Price: ${product['price']:.2f} | Quantity: {product['quantity']}\n")
    else:
        print(f"Product '{name}' not found.")

def option_update():
    name = input("Product to update: ").strip()
    new_price = None
    new_quantity = None

    if input("Update price? (Y/N): ").strip().upper() == "Y":
        new_price = ask_float("New price: ")
    if input("Update quantity? (Y/N): ").strip().upper() == "Y":
        new_quantity = ask_int("New quantity: ")

    update_product(inventory, name, new_price, new_quantity)

def option_delete():
    name = input("Product to delete: ").strip()
    delete_product(inventory, name)

def option_save():
    path = input("Enter file name (e.g., inventory.csv): ").strip()
    save_csv(inventory, path)

def option_load():
    path = input("Enter file name to load: ").strip()
    loaded_products = load_csv(path)
    if loaded_products:
        apply_load(inventory, loaded_products)

#Main Menu

OPTIONS = {
    "1": ("Add Product", option_add),
    "2": ("Show Inventory", lambda: show_inventory(inventory)),
    "3": ("Search Product", option_search),
    "4": ("Update Product", option_update),
    "5": ("Delete Product", option_delete),
    "6": ("Statistics", lambda: calculate_statistics(inventory)),
    "7": ("Save to CSV", option_save),
    "8": ("Load from CSV", option_load),
    "9": ("Exit", None),
}

def display_menu():
    print("\n========= INVENTORY SYSTEM =========")
    for key, (desc, _) in OPTIONS.items():
        print(f"  {key}. {desc}")
    print("====================================")

# -- Main Loop --

is_running = True

while is_running:
    display_menu()
    choice = input("Choose an option (1-9): ").strip()

    if choice not in OPTIONS:
        print("Invalid choice. Please select 1-9.")
        continue

    desc, action = OPTIONS[choice]

    if choice == "9":
        print("Exiting... Goodbye!")
        is_running = False
        continue

    try:
        action()
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"Something went wrong: {e}")
