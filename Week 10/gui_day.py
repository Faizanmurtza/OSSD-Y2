import tkinter as tk

def convertor():
    
        calcius = float(entry.get())
        fori = (calcius-32)*5/9
        entry.delete(0,tk.END)
        entry.insert(tk.END,fori)
        
        entry.config(state="readonly")

def clear():
        entry.config(state="normal")
        entry.delete(0,tk.END)       

    
root = tk.Tk()
root.geometry("400x300")
root.title("temperature calculator")
label_1 = tk.Label(root,text = "enter calcius" , font =("Arial" , 20) , width = 20).pack(pady=5)
entry = tk.Entry(root, font = ("arial" , 20) , justify="center" , width=20)
entry.pack(pady=10)


tk.Button(root, text="convert" , width=10 , font= ("arial", 20) , command=convertor).pack(pady=10)
tk.Button(root, text=("clear") ,font=14 , width=5, bg="blue", command=clear, justify="center").pack(pady=10)

root.mainloop()
