import tkinter as tk
from tkinter import messagebox
import os

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            entry_var.set("")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x450")
root.minsize(400,450)
root.maxsize(400,450)
root.config(bg="black")
current = os.path.dirname(__file__)
root.wm_iconbitmap(f"{current}/logo.ico")
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20 bold", justify='right', borderwidth=5)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=20, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

buttons = [
    ['7', '8', '9', 'C'],
    ['4', '5', '6', '+'],
    ['1', '2', '3', '-'],
    ['*', '0', '/', '=']
]

for row in buttons:
    frame = tk.Frame(button_frame,bg="black")
    frame.pack()
    for char in row:
        btn = tk.Button(frame, text=char, font="Arial 15 bold", height=2, width=6 ,borderwidth=5)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", on_click)

root.mainloop()
