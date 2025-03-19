 LibraEase - Smart Library Management System

Overview

LibraEase is a Python-based Library Management System that provides an efficient way to manage books, users, and transactions using a MySQL database. It is designed to help libraries automate book tracking, lending, and returns.

Features

✔ 📖 Add, issue, and return books efficiently✔ 🔍 Search functionality to find books quickly✔ 🏠 User-friendly Tkinter GUI for easy navigation✔ 🔑 Secure Admin Login System✔ 📊 Database integration using MySQL✔ 🛠 Custom error handling with pop-ups✔ 📅 Track overdue books and fines✔ 📁 Export book records as reports (CSV, Excel)

Tech Stack Used

Python (Tkinter for GUI, Pandas for data handling)

MySQL (Database storage)

MySQL Connector for Python

Seaborn & Matplotlib (For visualization)

Installation & Setup

Clone the Repository

git clone https://github.com/yourusername/library-management-system.git
cd library-management-system

Install Required Dependencies

pip install mysql-connector-python pandas tkinter

Set Up MySQL Database

Open MySQL Workbench or Command Line

Run schema.sql to create the database

CREATE DATABASE LibraryDB;
USE LibraryDB;
CREATE TABLE books (BookID INT PRIMARY KEY, Title VARCHAR(255), Author VARCHAR(255), Status VARCHAR(50));

Run the Application

python app.py

Future Improvements

🚀 Implement barcode scanning for book tracking🚀 Add email notifications for due books🚀 Improve UI design with a modern theme
