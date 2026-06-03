import tkinter as tk
from tkinter import messagebox
import os

USERS_FILE = "users.txt"

# ─────────────────────────────────────────
# File read – Sign In function
# ─────────────────────────────────────────
def sign_in():
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    if not username or not password:
        messagebox.showwarning("Khaali Fields", "Username aur Password dono likhein!")
        return

    if not os.path.exists(USERS_FILE):
        messagebox.showerror("Error", "Koi account nahi mila. Pehle Sign Up karein.")
        return

    with open(USERS_FILE, "r") as f:
        for line in f:
            saved_user, saved_pass = line.strip().split(",", 1)
            if saved_user == username and saved_pass == password:
                messagebox.showinfo("Kamyabi", f"Welcome, {username}!")
                main_menu()
                return

    messagebox.showerror("Galat", "Username ya Password galat hai!")


# ─────────────────────────────────────────
# File write – Sign Up function
# ─────────────────────────────────────────
def sign_up():
    username = entry_new_user.get().strip()
    password = entry_new_pass.get().strip()
    confirm  = entry_confirm.get().strip()

    if not username or not password or not confirm:
        messagebox.showwarning("Khaali Fields", "Saare fields bharein!")
        return

    if password != confirm:
        messagebox.showerror("Error", "Dono passwords match nahi kar rahe!")
        return

    # Check if username already exists
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            for line in f:
                saved_user, _ = line.strip().split(",", 1)
                if saved_user == username:
                    messagebox.showerror("Error", "Yeh username pehle se mawjood hai!")
                    return

    with open(USERS_FILE, "a") as f:
        f.write(f"{username},{password}\n")

    messagebox.showinfo("Kamyabi", "Account ban gaya! Ab Sign In karein.")
    sign_in_window()


# ─────────────────────────────────────────
# Sign In window
# ─────────────────────────────────────────
def sign_in_window():
    # Clear root window
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Sign In")
    root.geometry("300x220")

    global entry_username, entry_password

    tk.Label(root, text="── Sign In ──", font=("Arial", 14, "bold")).pack(pady=(15, 10))

    frame = tk.Frame(root)
    frame.pack()

    tk.Label(frame, text="Username:", anchor="w", width=10).grid(row=0, column=0, padx=5, pady=5)
    entry_username = tk.Entry(frame, width=20)
    entry_username.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame, text="Password:", anchor="w", width=10).grid(row=1, column=0, padx=5, pady=5)
    entry_password = tk.Entry(frame, show="*", width=20)
    entry_password.grid(row=1, column=1, padx=5, pady=5)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Sign In",  width=10, command=sign_in,        bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Sign Up",  width=10, command=sign_up_window, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5)


# ─────────────────────────────────────────
# Sign Up window
# ─────────────────────────────────────────
def sign_up_window():
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Sign Up")
    root.geometry("300x250")

    global entry_new_user, entry_new_pass, entry_confirm

    tk.Label(root, text="── Sign Up ──", font=("Arial", 14, "bold")).pack(pady=(15, 10))

    frame = tk.Frame(root)
    frame.pack()

    tk.Label(frame, text="Username:",  anchor="w", width=13).grid(row=0, column=0, padx=5, pady=5)
    entry_new_user = tk.Entry(frame, width=18)
    entry_new_user.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame, text="Password:",  anchor="w", width=13).grid(row=1, column=0, padx=5, pady=5)
    entry_new_pass = tk.Entry(frame, show="*", width=18)
    entry_new_pass.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame, text="Confirm Pass:", anchor="w", width=13).grid(row=2, column=0, padx=5, pady=5)
    entry_confirm = tk.Entry(frame, show="*", width=18)
    entry_confirm.grid(row=2, column=1, padx=5, pady=5)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Register", width=10, command=sign_up,        bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Back",     width=10, command=sign_in_window, bg="#f44336", fg="white").grid(row=0, column=1, padx=5)


# ─────────────────────────────────────────
# Main menu window  (login ke baad)
# ─────────────────────────────────────────
def main_menu():
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Main Menu")
    root.geometry("300x200")

    tk.Label(root, text="Main Menu", font=("Arial", 16, "bold")).pack(pady=(20, 10))
    tk.Label(root, text="Aap successfully login ho gaye!", fg="green").pack(pady=5)

    tk.Button(root, text="Logout", width=15, command=sign_in_window,
              bg="#f44336", fg="white").pack(pady=20)


# ─────────────────────────────────────────
# Root window
# ─────────────────────────────────────────
root = tk.Tk()
root.title("Application")
root.geometry("300x200")
sign_in_window()

root.mainloop()





