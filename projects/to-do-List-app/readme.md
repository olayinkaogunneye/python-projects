# 📝 To‑Do List Manager

A feature-rich, menu-driven Python application for managing personal tasks.  
This project started as a simple beginner script and was fully refactored into a modular, documented, and extensible productivity tool.

---

## 🚀 Features

### ✔ Core Functionality
- Add tasks  
- Mark tasks as completed  
- Delete tasks  
- View all tasks  
- Save and load tasks using JSON  

### ✔ Enhanced Features (Phase 4)
- Task priorities (High, Medium, Low)  
- Task categories (Work, Personal, etc.)  
- Optional due dates (YYYY‑MM‑DD)  
- Search tasks by keyword  
- Sort tasks by:
  - Priority  
  - Due date  
  - Alphabetically  
  - Completion status  

### ✔ Additional Advanced Features
- Edit existing tasks  
- Filter by category  
- Filter by priority  
- Mark all tasks as completed  
- Clear all completed tasks  

---

## 🧠 What I Learned

This project helped me practice:

- Modular Python design  
- Writing professional docstrings  
- Defensive programming and error handling  
- JSON-based persistence  
- Designing CLI user experiences  
- Adding realistic features to simple apps  
- Thinking like a software engineer, not just a coder  

---

## 📂 Project Structure

```
to-do-list-app/
│
├── todo_app.py
├── to-do-list.json
├── README.md
│
└── data/
    └── sample_tasks.json
```

---

## ▶️ How to Run the App

1. Install Python  
2. Download or clone the project  
3. Open a terminal inside the folder  
4. Run:

```
python todo_app.py
```

---

## 📦 Sample Task Data

A sample dataset is included to help you test the app:

```json
[
    {
        "task": "Buy groceries",
        "completed": false,
        "priority": "High",
        "category": "Errands",
        "due_date": "2025-02-10"
    },
    {
        "task": "Finish analytics project",
        "completed": false,
        "priority": "High",
        "category": "Work",
        "due_date": "2025-02-15"
    },
    {
        "task": "Call family",
        "completed": true,
        "priority": "Low",
        "category": "Personal",
        "due_date": null
    }
]
```

---

## 🔮 Future Improvements

- Colorized terminal output  
- Recurring tasks  
- Export tasks to CSV  
- Subtasks / checklists  
- GUI version (Tkinter or PyQt)  
- Web version (Flask or FastAPI)  

---

## 💡 Why This Project Matters

This project demonstrates:

- Clean architecture  
- Real-world features  
- Error handling  
- Documentation  
- Practical Python skills  

It’s a strong portfolio piece that shows both technical ability and thoughtful design.

---

## 📜 License

This project is open-source and free to use for learning or personal development.