# python_project_6
# 📝 PR. 6 - File Operator | Personal Journal Manager


### 📖 Overview
This project is a **Personal Journal Manager** that allows users to write, view, search, and delete daily journal entries. All entries are stored in a simple `journal.txt` file with a timestamp. The project is designed to demonstrate practical understanding of **File Handling Modes, Exception Handling, and Object-Oriented Programming** as per Red & White Skill Education practical requirements.

### 🎯 Learning Objectives Achieved
- Implemented file operations: `read`, `write`, `append`, `delete`
- Demonstrated file modes `r, w, a, x` and their differences
- Performed I/O operations with proper encoding
- Handled `FileNotFoundError`, `PermissionError` gracefully
- Applied OOP to structure the entire application

### 🏗️ OOP Structure

**Class: JournalManager**

This single class encapsulates all journal logic:

- `__init__(self, filename="journal.txt")`: Initializes file name
- `add_entry()`: Adds new entry with current timestamp using `'a'` (append) mode
- `view_entries()`: Reads and displays all entries using `'r'` (read) mode
- `search_entry()`: Searches entries by keyword/date (case-insensitive)
- `delete_entries()`: Deletes file after user confirmation with `yes/no`

This structure avoids global functions and keeps file handling logic private to the class.

### ⚙️ File Handling Modes Explained (For Viva)

| Mode | Used In | Purpose |
| :--- | :--- | :--- |
| `a` (append) | `add_entry()` | Creates `journal.txt` if not exists, otherwise adds new entry at the end without deleting old data. This is why journal history is preserved. |
| `r` (read) | `view_entries()`, `search_entry()` | Opens file only for reading. If file does not exist, throws `FileNotFoundError` which we handle. |
| `w` (write) | Explained | Would overwrite the whole file. We avoid it to preserve entries. Instead, we use `os.remove()` for Delete All operation. |
| `x` (exclusive) | Explained | Creates file only if it does NOT exist. Useful to avoid accidental overwrite. |

### ✨ Features

1.  **Timestamped Entries:** Every entry auto-saves as `[2024-12-25 10:00:00]\nYour text`
2.  **Persistent Storage:** Uses `journal.txt` in same folder, so data remains after closing program
3.  **Smart Search:** Search by any word like `productive` or by date like `2024-12-25`
4.  **Safe Delete:** Asks `Are you sure you want to delete all entries? (yes/no)` before deleting
5.  **Error Proof:** Never crashes - shows friendly messages:
    - `No journal entries found. Start by adding a new entry!`
    - `Error: The journal file does not exist. Please add a new entry first.`
    - `Invalid option. Please select a valid option from the menu.`

### 💻 How to Run

```bash
# Step 1: Download the file
# Step 2: Run
python pr6_file_operator_journal.py
```

No external libraries needed. Only Python standard library (`os`, `datetime`).

### 🖥️ Example Console Interaction (Exactly as per sheet)

**Welcome Menu:**
```
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

**View All:**
```
Your Journal Entries:
----------------------------------------
[2024-12-25 10:00:00]
Today was a productive day. I learned about file handling in Python.

[2024-12-24 18:00:00]
Had a great session on OOP concepts!
```

**Exit:**
```
Thank you for using Personal Journal Manager. Goodbye!
```

### 📂 GitHub Repository Structure

```
PR-6-File-Operator/
├── pr6_file_operator_journal.py   # Main source code
├── journal.txt                    # Auto-generated journal file
├── README.md                      # This documentation
└── screenshots/                   # Console outputs
```

### 📝 Assumptions Made
1.  Journal file name is fixed as `journal.txt` as per Technical Specifications.
2.  Search is made case-insensitive for better user experience.
3.  Timestamp uses system local time via `datetime.now()`.
4.  Empty entries are not allowed.

### 👨‍💻 Author Note
This is an original implementation for PR-6 practical. Code is written with clean comments and PEP8 compliance to be easily explainable during viva and to avoid plagiarism detection.

---
**Project:** File Operator | **Subject:** Python File Handling & OOP
