# імпортуємо графічну бібліотеку
from tkinter import *

# створюємо головне вікно
window = Tk()

# функція для зміни тексту міток
def change_text():
    lab2.config(text="Учень буде навчатися у %d класі" % val.get())
    lab3.config(text="ПІБ учня - %s" % edit1.get())

# створюємо та розміщуємо мітку з текстом та пусте текстове поле
lab1 = Label(window, text='Введіть ПІБ учня та виберіть клас')
lab1.pack()
edit1 = Entry(window)
edit1.pack()

# створюємо змінну для зв'язку між перемикачами
val = IntVar()

# встановлюємо перше значення для змінної
val.set(1)

# створюємо та розміщуємо перемикачі за допомогою циклу
for i in range(11):
    Radiobutton(window, text='%d клас' % (i+1), variable=val, value=i+1, command=change_text).pack()

# створюємо та розміщуємо мітки
lab2 = Label(window, fg='red')
lab2.pack()
lab3 = Label(window, fg='red')
lab3.pack()

# відображення вікна при запуску
window.mainloop()
