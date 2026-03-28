# Inventory Management System 🗂️

A console-based inventory management system built in Python. Supports full CRUD operations, statistics, and CSV file persistence.

---

## 📁 Project Structure

```
inventory-basics/
├── app.py          # Main entry point — runs the menu
├── servicios.py    # CRUD operations and statistics
└── archivos.py     # CSV save and load logic
```

---

## ▶️ How to Run

1. Place all three files in the same folder.
2. Open `app.py` in your Python environment (terminal, VS Code, Pydroid, etc.).
3. Run it:

```bash
python app.py
```

---

## 📋 Menu Options

| Option | Action |
|--------|--------|
| 1 | Add product |
| 2 | Show inventory |
| 3 | Search product |
| 4 | Update product |
| 5 | Delete product |
| 6 | View statistics |
| 7 | Save to CSV |
| 8 | Load from CSV |
| 9 | Exit |

---

## 💾 CSV Format

When saving or loading, the CSV file must follow this structure:

```
nombre,precio,cantidad
apple,1.50,100
banana,0.75,200
```

- **nombre** → product name (string)
- **precio** → price (float, non-negative)
- **cantidad** → quantity (integer, non-negative)

Invalid rows are skipped automatically and reported at the end.

---

## 🔀 Load Modes

When loading a CSV, the program asks:

- **Overwrite (S):** Replaces the entire current inventory.
- **Merge (N):** Combines with existing data.
  - If a product already exists → quantity is added, price is updated to the new one.
  - If it's a new product → it's added directly.

---

## 📊 Statistics

The statistics option calculates:

- Total units in stock
- Total inventory value
- Most expensive product
- Product with highest stock

---

## 🛠️ Requirements

- Python 3.6 or higher
- No external libraries needed — only the built-in `csv` module

---

## 👤 Author

**Breyner** — RIWI Software Development Student
