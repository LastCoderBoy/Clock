from tkinter import *
from datetime import date
from time import strftime

appear = Tk()
appear.title("My first Clock")
frame= Frame(appear,bg='black')
frame.pack()
appear.resizable(False,False)
today = date.today()
x = today.strftime("%B %d, %Y")
def date_time():
    clock = strftime("%H:%M:%S %p  \n%A")
    label.config(text=x)
    label1.config(text=clock)

    label.after(1000, date_time)

label = Label(frame, font=("ds_digital", 70), bg="black", fg=("cyan"))
label.pack(anchor='center')

label1 = Label(frame, font=("ds_digital", 70), bg="black", fg=("cyan"))
label1.pack(anchor='center')
date_time()

mainloop()
