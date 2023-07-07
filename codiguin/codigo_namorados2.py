import tkinter as tk
from tkinter import messagebox
import random

def move_button1(e):
    x = button1.winfo_x() + random.randint(-5, 5)
    y = button1.winfo_y() + random.randint(-5, 5)

    x = max(0, min(x, root.winfo_width() - button1.winfo_width()))
    y = max(0, min(y, root.winfo_height() - button1.winfo_height()))

    button1.place(x=x, y=y)

def move_button2(e):
    pass

def button1_clicked():
    messagebox.showinfo("Mensagem", "Eu te amo!")

def button2_clicked():
    messagebox.showinfo("Mensagem", "Mas eu te amo!")

root = tk.Tk()
root.geometry("300x200")

frame = tk.Frame(root, width=200, height=100, bg="gray")
frame.pack(pady=20)

button1 = tk.Button(frame, text="Me ama?", command=button1_clicked)
button1.pack(side='left')

button2 = tk.Button(frame, text="Não me ama!", command=button2_clicked)
button2.pack(side='left')

root.bind('<Motion>', move_button1)
button2.bind('<Button-1>', move_button2)

root.mainloop()
