import tkinter as tk
from tkinter import ttk
import mysql.connector
import subprocess
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize login window
login = tk.Tk()
style = ttk.Style(login)

login.configure(bg="#303030")
style.configure(
    'TLabel',
    background="#202020",
    foreground="#ffffff",
)

login.title("LibraEase - Smart Library Login")

# Center window on screen
window_width = 700
window_height = 800
screen_width = login.winfo_screenwidth()
screen_height = login.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

login.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# User input variable
username = tk.StringVar()

# Login screen image
login_pic = tk.PhotoImage(file="achetz/login_icon.png")

# Heading text
heading = ttk.Label(
    login,
    font=('Roboto', 40),
    text="Welcome to LibraEase 📚",
    image=login_pic,
    compound='top'
)

heading.pack(pady=50)

# Username input field
userText = ttk.Label(
    login,
    font=('Lato', 15),
    text='Enter your username: '
)

userText.pack(padx=50, anchor=tk.W)

userEntry = tk.Entry(
    login,
    textvariable=username,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0
)

userEntry.pack(padx=100, pady=10, fill=tk.X)

# Function to handle sign-in
def signIn():
    try:
        sqldatabase = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        login.quit()
        subprocess.call(['python', 'home.py'])
    except:
        subprocess.call(['python', 'popups/connect_error.py'])

# Login button
submit = tk.Button(
    login,
    text="Log in",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=signIn,
    cursor='dot',
    height=2,
    width=10,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

submit.pack(pady=10)

# Run the login window
login.mainloop()
