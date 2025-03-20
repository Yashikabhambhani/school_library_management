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

# Initialize Show Books Window
show_page = tk.Tk()
show_page.title("LibraEase - View Books")
show_page.configure(bg="#303030")

# Set window size and position
window_width = 700
window_height = 500
screen_width = show_page.winfo_screenwidth()
screen_height = show_page.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

show_page.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Heading Label
heading = ttk.Label(
    show_page,
    font=('Roboto', 25),
    text="Library Books - LibraEase 📚",
    background="#303030",
    foreground="#ffffff"
)
heading.pack(pady=20)

# Function to Fetch and Display Books
def fetch_books():
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name  # Now dynamic
