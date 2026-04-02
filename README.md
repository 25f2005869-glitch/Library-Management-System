📚 Library Management System (Console + GUI + PRO)

📌 Project Description

This project includes three versions of a Library Management System developed using Python:

🔹 Level 1 – Console-Based System

A simple menu-driven program using basic Python concepts.

🔹 Level 2 – GUI-Based System

An interactive version using Tkinter with buttons and list display.

🔹 Level 3 – PRO GUI System

An advanced version with:

- Book status (Available / Issued)
- Category system
- Search functionality
- Color-coded interface

---

🚀 Features

✅ Common Features

- Add Book
- View Books
- Search Book
- Delete Book
- Persistent Storage ("books.txt")

✅ Improvements

- Prevents empty book names
- Prevents duplicate books (case-insensitive)
- Case-insensitive search & delete

🖥️ GUI Features (Level 2)

- User-friendly interface
- Buttons for operations
- Input field
- List display

🚀 PRO Features (Level 3)

- Issue / Return Book
- Book Status (Available / Issued)
- Category (Study, Novel, Science, etc.)
- Color coding (Green = Available, Red = Issued)
- Partial search

---

🛠 Technologies Used

- Python
- Tkinter (GUI Development)
- File Handling
- Lists & Dictionaries
- Loops & Conditions
- Object-Oriented Programming (OOP)

---

📂 Project Structure

Library-Management-System/
│
├── library_management.py         # Console Version (Level 1)
├── library_management_gui.py     # GUI Version (Level 2)
├── library_pro_gui.py            # PRO Version (Level 3)
├── books.txt                     # Data storage
├── screenshots/
│   └── library_gui.png
└── README.md

---

▶️ How to Run

🔹 Console Version

python library_management.py

🔹 GUI Version

python library_management_gui.py

🔹 PRO Version

python library_pro_gui.py

---

💻 Example (Console Output)

===== Library Management System =====

1. Add Book
2. View Books
3. Search Book
4. Delete Book
5. Exit

Enter your choice: 1

Enter book name: Python Programming
Book added successfully!

---

🖥️ GUI Overview

🔹 Basic GUI

- Input box for book name
- Buttons:
  - Add Book
  - View Books
  - Search Book
  - Delete Book
- Output display area

🔹 PRO GUI

- Category dropdown
- Issue / Return buttons
- Color-coded books
- Search functionality
- Status display

---

📸 Screenshots

🖥 GUI Version

"Library GUI" (screenshots/library_gui.png)

---

🎯 Learning Purpose

This project helps in learning:

- Python Programming Basics
- File Handling
- Menu-driven programs
- GUI Development using Tkinter
- Object-Oriented Programming
- Real-world project design

---

🧠 Approach / Logic

🔹 Console

- Uses list to store books
- Reads file at start
- Writes file after update

🔹 GUI

- Same logic + Tkinter UI
- Listbox for display
- Button-based interaction

🔹 PRO

- Uses dictionary structure:

{"title": "Book", "status": "Available", "category": "Study"}

- File format:

Book Name|Status|Category

---

⚠️ Common Mistakes

- Forgetting to save file after update
- Not handling empty input
- Duplicate entries
- Incorrect file format (PRO version)
- Index errors in GUI selection

---

⚡ Complexity

Operation| Time Complexity
Add Book| O(1)
View Books| O(n)
Search Book| O(n)
Delete Book| O(n)

---

🚀 Future Improvements

- Add user login system
- Track issued books with student names
- Due date & fine system
- Database (SQLite/MySQL)
- Dark mode GUI

---

👩‍💻 Author

Saloni Tiwari
GitHub: 25f2005869-glitch
BS Data Science Student

---

⭐ Project Level

🟢 Level 1 → Beginner (Console)
🟡 Level 2 → Beginner+ (GUI)
🔵 Level 3 → Intermediate (PRO GUI)

---

⭐ This project is ideal for beginners progressing to real-world applications.
