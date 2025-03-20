import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve MySQL credentials from .env file
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")  # Now uses a dynamic database name

# Initialize Issue Book Window
issue_page = tk.Tk()
issue_page.title("LibraEase - Issue a Book")
issue_page.configure(bg="#303030")

# Set window size and position
window_width = 600
window_height = 400
screen_width = issue_page.winfo_screenwidth()
screen_height = issue_page.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

issue_page.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Heading Label
heading = ttk.Label(
    issue_page,
    font=('Roboto', 25),
    text="Issue a Book",
    background="#303030",
    foreground="#ffffff"
)
heading.pack(pady=20)

# Input Fields
book_id_var = tk.StringVar()
user_id_var = tk.StringVar()

book_id_label = ttk.Label(issue_page, text="Enter Book ID:", background="#303030", foreground="white")
book_id_label.pack(pady=5)
book_id_entry = ttk.Entry(issue_page, textvariable=book_id_var, width=40)
book_id_entry.pack(pady=5)

user_id_label = ttk.Label(issue_page, text="Enter User ID:", background="#303030", foreground="white")
user_id_label.pack(pady=5)
user_id_entry = ttk.Entry(issue_page, textvariable=user_id_var, width=40)
user_id_entry.pack(pady=5)

# Function to Issue a Book
def issue_book():
    book_id = book_id_var.get().strip()
    user_id = user_id_var.get().strip()

    if not book_id or not user_id:
        messagebox.showwarning("Warning", "Please enter both Book ID and User ID.")
        return

    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name  # Now dynamic
        )
        cursor = connection.cursor()

        # Check if book is available
        cursor.execute("SELECT * FROM books WHERE id = %s AND status = 'Available'", (book_id,))
        book = cursor.fetchone()

        if book:
            # Update book status and insert record into issued_books
            cursor.execute("UPDATE books SET status = 'Issued' WHERE id = %s", (book_id,))
            cursor.execute("INSERT INTO issued_books (book_id, user_id) VALUES (%s, %s)", (book_id, user_id))
            connection.commit()
            messagebox.showinfo("Success", "Book issued successfully!")
        else:
            messagebox.showwarning("Warning", "Book is not available for issue.")

        cursor.close()
        connection.close()
        book_id_var.set("")
        user_id_var.set("")  # Clear input fields

    except Exception as e:
        messagebox.showerror("Error", f"Failed to issue book: {str(e)}")

# Issue Book Button
issue_button = ttk.But
