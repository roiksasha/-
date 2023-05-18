
from tkinter import *
root = Tk()

# змінна для зв'язку між перемикачами та встановлення першого значення 
val = StringVar()
val.set("blue")

# функція для зміни кольору фону тексту
def color():
    label.config(bg=val.get())

# чотири перемикачі
blue = Radiobutton(root, text="Синій", variable=val, value="blue", command=color)
yellow = Radiobutton(root, text="Жовтий", variable=val, value="yellow", command=color)
red = Radiobutton(root, text="Червоний", variable=val, value="red", command=color)
green = Radiobutton(root, text="Зелений", variable=val, value="green", command=color)

# розміщення перемикачів на екрані
blue.pack()
yellow.pack()
red.pack()
green.pack()

# текстовий напис
label = Label(root, text="Tekcm")
label.pack()

# відображення вікна
root.mainloop() 
