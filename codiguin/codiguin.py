import tkinter as tk
from tkinter import*
import random
from tkinter import messagebox


root = tk.tk()
root.tilte('Aceitas?')
root.geometry('600x600')
root.configure(background='#ffc8dd')



def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - buttom_1.winfo_width())
        y = random.randint(0, root.winfo_height() - buttom_1.winfo_width())
        buttom_1.place(x=x, y=y)


 def accepted():
    messagebox.showinfo(
        'Meu amor', 'Eu te amo meu amor, lanchinho mais tarde?')
    
    def denied():
        buttom_1.destroy()


        margin = Canvas(root, width=500, bg='#ffc8dd', heigth=100,
                        db=0, highlightthickness=0, relief='ridge')
        margin.pack()
        text_id = label(root, bg='#ffc8dd', text='Feliz 7 mesês meu amor, te amo muito',
                        fg='#590d22', font=('Montserrat', 24, 'bold'))
        text_id.pack()
        root.bind('<Motion>', move_button_1)
        button_2 = tk.Button(root, text='Sim', bg='#ffb3c1', relief=RIDGE,
                             bd=3, command=accepted, font=('Monteserrat', 14, 'bold'))
        buttom_2.pack()


        root.mainloop()