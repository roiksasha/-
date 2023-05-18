inport tkinter as tk
import time

class Application(tk.Frame):
    def_init_(self, master-None):
        super()._init_(master)
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.hi_there- tk.Button(self, font="Verdana", bg="red", fg="black", width =7, height=4)
        self.hi_there["text"]= "Hello User\n(click me :))))"
        self.hi_there['command'] = self.self.say_hi
        self.hi_there.pack(side="top")
        self.quit - tk.button(self, text="Quit", font - "Arial",fg="red", bg="while", width=7, heght=4, command=root.destroy)
        self.quit.pack(side="buttom")
        self.button = tk.Button(self)
        self.button['text'] = time.strftime('%H:%M:%S')
        self.button['command'] = self.button_clicked
        self.button.pack(side="buttom")
    def say_hi(self):
        print("text after press the button")
    def button_clicked(self):
        self.button['text']= time.strftime('%H:%M:%S')
root = tk.Tk()
app = Application(master=root)
app.mainloop()
import tkinter as tk
import time

        
