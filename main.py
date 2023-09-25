from tkinter import *
from tkinter import ttk

# Первая кнопка
def red():
    styles = ttk.Style()
    styles.configure("BW.TLabel", background="red")
    btns['style'] = "BW.TLabel"

btns = ttk.Button(text='Покраска в красный', command=red) #Кнопкав нижнем левом углу
btns.place(relx=.0, rely=1, anchor='sw', width=120, height=25)