import tkinter as tk
from tkinter import messagebox

def save_credentials():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter username and password")
        return

    with open("credentials.txt", "a") as f:
        f.write(f"{username},{password}\n")

    messagebox.showinfo("Success", "Account created successfully!")

def check_credentials():
    username = username_entry.get()
    password = password_entry.get()

    try:
        with open("credentials.txt", "r") as f:
            users = f.readlines()

        for user in users:
            saved_username, saved_password = user.strip().split(",")

            if username == saved_username and password == saved_password:
                messagebox.showinfo("Success", "Login Successful!")
                return

        messagebox.showerror("Error", "Invalid Username or Password")

    except FileNotFoundError:
        messagebox.showerror("Error", "No account found. Please Sign Up first.")

def signin_window():
    global username_entry, password_entry

    tk.Label(root, text="Login", font=("Arial", 14)).pack(pady=10)

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    tk.Button(root, text="Sign In", command=check_credentials).pack(pady=5)

    tk.Button(root, text="Sign Up", command=save_credentials).pack()

root = tk.Tk()
root.title("Sign In System")
root.geometry("300x250")

signin_window()

root.mainloop()