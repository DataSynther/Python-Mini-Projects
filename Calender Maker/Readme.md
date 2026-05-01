# 📅 Calendar Maker

> Generate printable monthly calendars using Python — clean, structured, and file-export ready.

---

## 🚀 Overview

**Calendar Maker** is a CLI-based Python application that generates a formatted monthly calendar for any given year and month, and saves it as a `.txt` file.

This project demonstrates:

* Date computation using Python’s built-in libraries
* Structured formatting for printable output
* Input validation and error handling
* File generation and persistence

---

## ✨ Features

* 📆 Generate calendar for any month/year
* 🧠 Handles leap years and date alignment automatically
* 🖨️ Printable text-based layout
* 💾 Saves output to a file
* ⚡ Lightweight and dependency-free

---

## 🛠️ Tech Stack

* Python 3.x
* Standard Library (`datetime`)

---

## 📂 Project Structure

```bash
.
├── calendar_maker.py
└── README.md
```

---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/calendar-maker.git
cd calendar-maker
```

### 2. Run the Application

```bash
python calendar_maker.py
```

### 3. Provide Input

* Enter a valid year (e.g., `2026`)
* Enter a month (`1`–`12`)

---

## 📤 Sample Output

```
                                  March 2026
...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..
+----------+----------+----------+----------+----------+----------+----------+
|  1       |  2       |  3       |  4       |  5       |  6       |  7       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
```

---

## 💾 Output File

The generated calendar is saved in the current directory:

```
calendar_<year>_<month>.txt
```

**Example:**

```
calendar_2026_3.txt
```

---

## 🧠 How It Works

* Uses `datetime.date()` to initialize the first day of the month
* Backtracks to the nearest Sunday to align the calendar grid
* Iterates week-by-week, formatting each row as a fixed-width string
* Stops when the month boundary is crossed

---

## ⚠️ Error Handling

* Validates numeric input for year and month
* Ensures month is within range (`1–12`)
* Wraps execution in a try-except block to handle unexpected errors

---

## 🔧 Possible Improvements

* Add CLI arguments using `argparse`
* Export calendars as PDF
* Add holiday annotations
* Convert to REST API using FastAPI
* Add web UI (React / HTML templates)

---

## 🧪 Future Scope (Advanced)

* Integrate with scheduling systems
* Build a calendar microservice
* Add timezone and locale support
* Store generated calendars in a database

---

## 👩‍💻 Author

**Samprita Das**

---

## ⭐ If You Found This Useful

Give it a ⭐ on GitHub — it helps visibility and motivates further improvements!
