# 📦 Inventory Manager

A simple, menu‑driven Python application for managing an inventory of items.  
This project began as a beginner exercise and was later refactored into a clean, modular, well‑documented, and error‑handled application suitable for a Python portfolio.

---

## 🚀 Features

### **Core Functionality**
- Add new items  
- Remove existing items  
- Update item quantities  
- View all inventory items  
- Save and load data using JSON  

### **Enhanced Features**
These improvements were added during the refactoring phase to make the project more realistic and professional:

- Search for items by keyword  
- Sort inventory (A–Z, Z–A, quantity low–high, quantity high–low)  
- Low‑stock alerts  
- Optional default quantity when adding items  
- Lambda‑based sorting  
- Input validation and error handling  
- Clean function‑based architecture  
- Professional docstrings  
- Graceful handling of corrupted or missing JSON files  

---

## 🧠 What I Learned

This project helped me practice and apply:

- Writing modular Python code  
- Designing reusable functions  
- Adding docstrings for clarity and maintainability  
- Handling errors with `try/except` and `raise`  
- Working with JSON files  
- Using lambda functions for sorting  
- Implementing user‑friendly CLI menus  
- Thinking like a developer: anticipating user mistakes and handling them gracefully  

---

## 📂 Project Structure

nventory-project/
│
├── inventory_app.py        # Main application file
├── inventory.json          # Saved inventory data (auto-generated)
├── README.md               # Project documentation
│
└── data/
└── sample_inventory.json   # Optional sample dataset


---

## ▶️ How to Run the App

1. Make sure you have Python installed.  
2. Download or clone the project folder.  
3. Open a terminal inside the folder.  
4. Run:

python inventory_app.py


The menu will appear, and you can interact with the inventory from there.

---

## 📝 Example Menu

Inventory Menu

Add item

Remove item

Update quantity

View inventory

Search items

Low-stock alert

Sort inventory

Exit


---

## 📦 Sample Inventory Data

A sample dataset is included to help you test the application:

```json
{
    "apple": 15,
    "banana": 3,
    "orange": 12,
    "pear": 7,
    "blueberries": 25,
    "kiwi": 4,
    "watermelon": 2,
    "dates": 18,
    "grapes": 10,
    "mango": 6,
    "pineapple": 1,
    "strawberries": 14,
    "papaya": 5,
    "lemon": 9,
    "lime": 8
}
```


## 🔮 Future Improvements
Here are some ideas for expanding the project:

Export inventory to CSV

Add categories for items

Add timestamps for updates

Build a simple GUI using Tkinter

Add unit tests

Add colorized terminal output

Add batch operations using *args or **kwargs

## 💡 Why This Project Matters
This project demonstrates:

Real Python fundamentals

Clean architecture

Error handling

Documentation

Problem‑solving

Practical application of Python skills

It’s a strong portfolio piece because it shows both technical ability and developer thinking.

## 📜 License
This project is open‑source and free to use for learning or personal development.