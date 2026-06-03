import tkinter as tk


def adder():
    num1 = int(entry_1.get())
    num2 = int(entry_2.get())
    result = num1+num2
    entry_3.delete(0, tk.END)
    entry_3.insert(tk.END, result)
    entry_3.config(state="readonly")


root = tk.Tk()
root.geometry("300x450")
root.title("addition calculator")
label = tk.Label(root, text="number 1:", font=("airal", 11)).pack(pady=10)
entry_1 = tk.Entry(root, font=("arail", 11),
                   justify="center", width=10, bg="lightblue")
entry_1.pack(pady=10)
label = tk.Label(root, text="number 2:", font=("arial", 11)).pack(pady=10)
entry_2 = tk.Entry(root, font=("arial", 11),
                   justify="center", width=10, bg="lightblue")
entry_2.pack(pady=10)
lable = tk.Label(root, text="result:", font=("arial", 11)).pack(pady=10)
entry_3 = tk.Entry(root, font=('arial', 14),
                   justify="center", width=10, bg="lightgreen")
entry_3.pack(pady=10)
tk.Button(root, text="add", font=("italic", 14),
          justify="center", width=5, command=adder).pack(pady=10)
root.mainloop()
