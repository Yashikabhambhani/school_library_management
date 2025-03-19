# school_library_management
LibraEase - Smart Library Management System

Overview

LibraEase is a Python-based Library Management System that helps efficiently manage books, users, and transactions using a MySQL database. It allows users to add, issue, and return books, making library operations smooth and automated.

Features

✔ 📖 Manage Books – Add, update, delete book records✔ 🔍 Search & Filter – Find books quickly using search functionality✔ 🏠 User-Friendly Interface – Built with Tkinter GUI for smooth navigation✔ 🔑 Secure Login System – Admin authentication for security✔ 📊 MySQL Integration – Stores and manages all library data efficiently✔ 📅 Overdue Tracking – Keeps track of book return deadlines and fines✔ 📁 Report Generation – Export book records as CSV/Excel files

Tech Stack Used

Python (Tkinter for GUI, Pandas for data handling)

MySQL (Database storage)

MySQL Connector for Python

Seaborn & Matplotlib (For visualization)

Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/yourusername/library-management-system.git
cd library-management-system

2️⃣ Install Required Dependencies

pip install mysql-connector-python pandas tkinter

3️⃣ Set Up MySQL Database

Open MySQL Workbench or Command Line

Run schema.sql to create the database

CREATE DATABASE LibraryDB;
USE LibraryDB;
CREATE TABLE books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(255),
    Author VARCHAR(255),
    Status VARCHAR(50)
);

4️⃣ Run the Application

python app.py

Future Improvements

🚀 Implement barcode scanning for book tracking🚀 Add email notifications for due books🚀 Improve UI design with a modern theme
