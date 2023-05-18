import tkinter

from tkinter import TOP, BOTTOM, RIGHT, LEFT

window=tkinter.Tk()

window.title("Four buttons")

window.geometry ("600x400+200+80")

Button1=tkinter.Button(window, text="yellow button", width=10,bg='yellow', height=1, font="Arial 14")

Button2=tkinter.Button(window, text="red button", width=20,bg='red', height=2, font="Arial 14")

Button3=tkinter.Button(window, text="green button", width=15,bg='green', height=3, font="Arial 14")

Button4=tkinter.Button(window, text="blue button", width=10,bg='blue', height=4, font="Arial 14")

Button1.pack(side=BOTTOM)

Button2.pack(side=TOP)

Button3.pack(side=RIGHT)

Button4.pack(side=LEFT)

window.mainloop()
