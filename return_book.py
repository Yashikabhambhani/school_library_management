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

# Initialize Return Book Window
return_book = tk.Tk()
return_book.title("LibraEase - Return a Book")
return_book.configure(bg="#303030")

# Set window size and position
window_width = 600
window_height = 400
screen_width = return_book.winfo_screenwidth()
screen_height = return_book.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

return_book.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Heading Label
heading = ttk.Label(
    return_book,
    font=('Roboto', 25),
    text="Return a Book",
    background="#303030",
    foreground="#ffffff"
)
heading.pack(pady=20)

# Book ID Input Field
book_id_var = tk.StringVar()

book_id_label = ttk.Label(return_book, text="Enter Book ID:", background="#303030", foreground="white")
book_id_label.pack(pady=5)
book_id_entry = ttk.Entry(return_book, textvariable=book_id_var, width=40)
book_id_entry.pack(pady=5)

# Function to Return a Book
def return_book_action():
    book_id = book_id_var.get().strip()

    if not book_id:
        messagebox.showwarning("Warning", "Please enter a Book ID.")
        return

    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name  # Now dynamic
        )
        cursor = connection.cursor()

        # Check if the book exists and is currently issued
        cursor.execute("SELECT * FROM issued_books WHERE book_id = %s", (book_id,))
        book = cursor.fetchone()

        if book:
            # Remove book from issued_books and update status in books table
            cursor.execute("DELETE FROM issued_books WHERE book_id = %s", (book_id,))
            cursor.execute("UPDATE books SET status = 'Available' WHERE id = %s", (book_id,))
            connection.commit()
            messagebox.showinfo("Success", "Book returned successfully!")
        else:
            messagebox.showwarning("Warning", "Book ID not found or not issued.")

        cursor.close()
        connection.close()
        book_id_var.set("")  # Clear input field

    except Exception as e:
        messagebox.showerror("Error", f"Failed to return book: {str(e)}")

# Return Book Button
return_button = ttk.Button(return_book, text="Return Book", command=return_book_action)
return_button.pack(pady=20)

# Run the Tkinter window
return_book.mainloop()
