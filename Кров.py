import tkinter
import tkinter.messagebox

# створення вікна програми
window = tkinter.Tk()
window.title('Кровоносна система')

# функції що викликуються при натисканні на кнопки
def button1_click():
    tkinter.messagebox.showinfo("Відповідь", "Молодець! У тебе добрі знання з біології!")

def button2_click():
    tkinter.messagebox.showerror("Відповідь", "Ти помилився!!!")

# створення кнопок та їх розміщення
button1 = tkinter.Button(window, text='Погоджуюсь', command=button1_click)
button1.pack()

button2 = tkinter.Button(window, text='Не погоджуюсь', command=button2_click)
button2.pack()

# запуск циклу подій обробки вікна
window.mainloop()
