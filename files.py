# files.py - Save and load inventory in CSV files

import csv

# Standard CSV Header
HEADER = ["name", "price", "quantity"]

def save_csv(inventory, path, include_header=True):
    """Saves the inventory to a CSV file."""
    if not inventory:
        print("Inventory is empty. Nothing to save.")
        return

    try:
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=HEADER)
            if include_header:
                writer.writeheader()
            writer.writerows(inventory)
        print(f"Inventory saved to: {path}")
    except Exception as e:
        print(f"Error saving file: {e}")


def load_csv(path):
    """Loads products from a CSV file with validation."""
    products = []
    bad_rows = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            # Check if header matches
            if reader.fieldnames != HEADER:
                print(f"Error: Invalid header. Expected: {HEADER}")
                return []

            for row in reader:
                try:
                    price = float(row["price"])
                    quantity = int(row["quantity"])
                    if price < 0 or quantity < 0:
                        bad_rows += 1
                        continue

                    products.append({
                        "name": row["name"].strip(),
                        "price": price,
                        "quantity": quantity,
                    })
                except ValueError:
                    bad_rows += 1
                    continue
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

    if bad_rows > 0:
        print(f"Warning: {bad_rows} invalid row(s) were skipped.")

    return products


def apply_load(inventory, loaded_products):
    """Merges loaded products into the current inventory."""
    choice = input("Overwrite current inventory? (Y/N): ").strip().upper()

    if choice == "Y":
        inventory.clear()
        inventory.extend(loaded_products)
        print(f"Inventory replaced. {len(loaded_products)} product(s) loaded.")
    else:
        print("Merging: Quantities will be added, and prices updated.")
        merged_count = 0
        for new_p in loaded_products:
            exists = False
            for current_p in inventory:
                if current_p["name"].lower() == new_p["name"].lower():
                    current_p["quantity"] += new_p["quantity"]
                    current_p["price"] = new_p["price"]
                    merged_count += 1
                    exists = True
                    break
            if not exists:
                inventory.append(new_p)
        print(f"Merge complete. {len(loaded_products)} processed, {merged_count} merged.")
