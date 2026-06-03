import tkinter as tk

def increment():
    current = int(entry.get())
    entry.config(state="normal")      # Unlock karo
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + 1)
    entry.config(state="readonly")    # Wapas lock karo

def decrement():
    current = int(entry.get())
    entry.config(state="normal")      # Unlock karo
    entry.delete(0, tk.END)
    entry.insert(tk.END, current - 1)
    entry.config(state="readonly")    # Wapas lock karo
root = tk.Tk()
root.title("Counter")
root.geometry("300x200")

# Label
label = tk.Label(root, text="Counter", font=("Arial", 20))
label.pack(pady=10)

# Entry - number dikhane ke liye
entry = tk.Entry(root, font=("Arial", 20), justify="center", width=10)
entry.insert(tk.END, "0")  # Shuru mein 0
entry.pack(pady=5)

# Buttons
tk.Button(root, text="Increment", font=("Arial", 14),
          command=increment).pack(pady=5)
tk.Button(root, text="Decrement", font=("Arial", 14),
          command=decrement).pack(pady=5)

root.mainloop()