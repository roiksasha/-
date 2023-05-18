import tkinter as tk

from tkinter import messagebox

class MathQuiz:

   def __init__(self, master):

       self.master = master

       master.title("Math Quiz")

       # Create question and answer dictionary

       self.questions = {

           "What is 2 + 2?": "yes",

           "What is 10 - 5?": "yes",

           "What is 7 * 3?": "no",

           "What is 12 / 4?": "yes",

           "What is the square root of 64?": "yes"

       }

       # Create question label

       self.question_label = tk.Label(master, text="Answer Yes or No:")

       self.question_label.pack()

       # Loop through questions and create question buttons

       for question, answer in self.questions.items():

           question_button = tk.Button(

               master,

               text=question,

               command=lambda answer=answer: self.check_answer(answer)

           )

           question_button.pack()

   def check_answer(self, answer):

       if answer == "yes":

           messagebox.showinfo("Correct", "Correct!")

       else:

           messagebox.showerror("Incorrect", "Incorrect! The answer is Yes.")

root = tk.Tk()

quiz = MathQuiz(root)

root.mainloop()
