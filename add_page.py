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

# Initialize Add Book Window
add_page = tk.Tk()
add_page.title("LibraEase - Add New Book")
add_page.configure(bg="#303030")

# Set window size and position
window_width = 600
window_height = 400
screen_width = add_page.winfo_screenwidth()
screen_height = add_page.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

add_page.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Heading Label
heading = ttk.Label(
    add_page,
    font=('Roboto', 25),
    text="Add a New Book",
    background="#303030",
    foreground="#ffffff"
)
heading.pack(pady=20)

# Book Information Input Fields
title_var = tk.StringVar()
author_var = tk.StringVar()

title_label = ttk.Label(add_page, text="Book Title:", background="#303030", foreground="white")
title_label.pack(pady=5)
title_entry = ttk.Entry(add_page, textvariable=title_var, width=40)
title_entry.pack(pady=5)

author_label = ttk.Label(add_page, text="Author Name:", background="#303030", foreground="white")
author_label.pack(pady=5)
author_entry = ttk.Entry(add_page, textvariable=author_var, width=40)
author_entry.pack(pady=5)

# Function to Add Book to Database
def add_book():
    title = title_var.get().strip()
    author = author_var.get().strip()

    if not title or not author:
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name  # Now dynamic
        )
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
        connection.commit()

        messagebox.showinfo("Success", "Book added successfully!")
        title_var.set("")
        author_var.set("")

        cursor.close()
        connection.close()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add book: {str(e)}")

# Add Book Button
add_button = ttk.Button(add_page, text="Add Book", command=add_book)
add_button.pack(pady=20)

# Run the Tkinter window
add_page.mainloop()
