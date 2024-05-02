from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler by Taha")
        self.window.config(bg=THEME_COLOR)

        photo1 = PhotoImage(file="images/true.png")
        photo2 = PhotoImage(file="images/false.png")

        self.button1 = Button(image=photo1)
        self.button2 = Button(image=photo2)

        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)






        self.window.mainloop()