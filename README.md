# ✅ focus_cli

**A terminal-based task manager built with Python OOP.**  
Add, complete, and list your tasks directly from the terminal.  
Simple. Fast. Local. CSV-backed.

---

## 🚀 Why focus_cli?

Built to help you learn:

- Python classes and objects
- `__init__`, `self`, and instance methods
- File I/O with CSV using `csv.DictWriter` and `csv.DictReader`
- Real-world thinking with priorities, categories, due dates

---

## 🧠 What It Can Do

- Add new tasks with title, due date, priority, and category
- List all tasks (with completion status)
- Filter incomplete tasks only
- Mark tasks as complete ✅
- Automatically save/load tasks from a CSV file

---

## 🛠️ How It Works

- All tasks are saved in `data/tasks.csv`
- Uses pure Python — no databases, no extra dependencies (yet)
- Modular structure with separate files for logic, data models, and CLI

---

## 🗂️ Project Structure

```
focus_cli/
├── data/
│   └── tasks.csv          # CSV file with all your tasks
├── src/
│   ├── main.py            # Main CLI app
│   ├── task.py            # Task class (OOP)
│   ├── task_manager.py    # Handles task operations (add, complete, save, load)
│   └── setup.py           # Optional script to generate dummy data
└── requirements.txt
```

---

## 📦 Installation

1. **Clone this repo:**

```bash
git clone https://github.com/your-username/focus_cli.git
cd focus_cli
```

2. **(Optional) Create a virtual environment:**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🧪 Usage

Run the app from the `src/` directory:

```bash
python main.py
```

You'll be prompted with:

```
--- TASK MANAGER ---
1. Add Task
2. List Tasks
3. List Incomplete Tasks
4. Complete Task
5. Exit
```

---

## 🧰 Tech Stack

- Python 3
- Standard Library:
  - `csv`
  - `os`
  - `datetime`
- (Optional) `pandas` for setting up sample tasks

---

## 📌 Future Ideas

- Add CSV import/export menu
- Add task search/filter by category or priority
- Add a GUI using `tkinter` or `PyQt5`
- Sync with Google Tasks or Notion via API

---

## 📄 License

MIT License. Free to use and extend.

---

Track your focus. Stay accountable. One task at a time. ✨