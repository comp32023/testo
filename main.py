from tkinter import *
from tkinter import ttk

# Первая кнопка
def red():
    styles = ttk.Style()
    styles.configure("BW.TLabel", background="red")
    btns['style'] = "BW.TLabel"

btns = ttk.Button(text='Покраска в красный', command=red) #Кнопкав нижнем левом углу
btns.place(relx=.0, rely=1, anchor='sw', width=120, height=25)


# Вторая кнопка :3
def purple():
    styles = ttk.Style()
    styles.configure("BW.TLabel", background="purple")
    btn['style'] = "BW.TLabel"

btn = ttk.Button(text='Покраска в фиолетовый', command=purple) #Кнопка внизу центра
btn.place(relx=0.5, rely=1, anchor='s', width=120, height=25)


# Третья кнопка кнопка :3
def black():
    style = ttk.Style()
    style.configure("BW.TLabel", foreground="white", background="black")
    buttonTTK['style'] = "BW.TLabel"