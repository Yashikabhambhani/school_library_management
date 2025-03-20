import tkinter as tk
from tkinter import ttk
import mysql.connector
import subprocess
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve MySQL credentials from .env file
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")  # Now uses a dynamic database name

# Initialize main home window
home = tk.Tk()
home.title("LibraEase - Library Management System")
home.configure(bg="#303030")

# Set window size and position
window_width = 800
window_height = 600
screen_width = home.winfo_screenwidth()
screen_height = home.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

home.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Heading Label
heading = ttk.Label(
    home,
    font=('Roboto', 35),
    text="Welcome to LibraEase 📚",
    background="#303030",
    foreground="#ffffff"
)
heading.pack(pady=20)

# Function to connect to the database and show books
def show_books():
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name  # Now dynamic
        )
        cursor = connection.cursor()
        cursor.execute("SELECT title, author FROM books;")
        books = cursor.fetchall()
        book_list.delete(0, tk.END)
        for book in books:
            book_list.insert(tk.END, f"{book[0]} by {book[1]}")
        
        cursor.close()
        connection.close()
    except Exception as e:
        book_list.insert(tk.END, f"Error: {str(e)}")

# Book List Display
book_list = tk.Listbox(
    home,
    font=("Manrope", 14),
    background="#404040",
    foreground="#ffffff",
    width=50,
    height=10
)
book_list.pack(pady=10)

# Button to Fetch Books
fetch_button = ttk.Button(
    home,
    text="Show Available Books",
    command=show_books
)
fetch_button.pack(pady=10)

# Run the Tkinter window
home.mainloop()
