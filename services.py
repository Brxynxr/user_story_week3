# services.py - Functions to handle inventory (CRUD and statistics)
def add_product(inventory, name, price, quantity):
    """Adds a new product to the inventory."""
    # Check if it already exists to avoid duplicates
    if find_product(inventory, name):
        print(f"Error: Product '{name}' already exists. Please use the update option.")
        return

    product = {"name": name, "price": price, "quantity": quantity}
    inventory.append(product)
    print(f"Product '{name}' added successfully.")


def show_inventory(inventory):
    """Displays all products in the console."""
    if not inventory:
        print("The inventory is empty.")
        return

    print("\n--- INVENTORY ---")
    for product in inventory:
        print(f"  Name: {product['name']} | Price: ${product['price']:.2f} | Quantity: {product['quantity']}")
    print("------------------\n")


def find_product(inventory, name):
    """Searches for a product by name (case-insensitive)."""
    for product in inventory:
        if product["name"].lower() == name.lower():
            return product
    return None


def update_product(inventory, name, new_price=None, new_quantity=None):
    """Updates price and/or quantity of an existing product."""
    product = find_product(inventory, name)

    if product is None:
        print(f"Product '{name}' not found.")
        return

    if new_price is not None:
        product["price"] = new_price
    if new_quantity is not None:
        product["quantity"] = new_quantity

    print(f"Product '{name}' updated successfully.")


def delete_product(inventory, name):
    """Removes a product from the inventory."""
    product = find_product(inventory, name)

    if product is None:
        print(f"Product '{name}' not found.")
        return

    inventory.remove(product)
    print(f"Product '{name}' deleted successfully.")


def calculate_statistics(inventory):
    """Calculates general inventory metrics."""
    if not inventory:
        print("No products available to calculate statistics.")
        return None

    subtotal = lambda p: p["price"] * p["quantity"]

    total_units = sum(p["quantity"] for p in inventory)
    total_value = sum(subtotal(p) for p in inventory)
    most_expensive = max(inventory, key=lambda p: p["price"])
    highest_stock = max(inventory, key=lambda p: p["quantity"])

    stats = {
        "total_units": total_units,
        "total_value": total_value,
        "most_expensive": most_expensive,
        "highest_stock": highest_stock,
    }

    print("\n--- STATISTICS ---")
    print(f"  Total Units:         {total_units}")
    print(f"  Total Inventory Value: ${total_value:.2f}")
    print(f"  Most Expensive:      {most_expensive['name']} (${most_expensive['price']:.2f})")
    print(f"  Highest Stock:       {highest_stock['name']} ({highest_stock['quantity']} units)")
    print("------------------\n")

    return stats
