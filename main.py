import os
import tkinter
import tkinter as tk

root = tk.Tk()
root.title('Data mining project')

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Find out the stats')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 30, window=label1)

label2 = tk.Label(root, text='Type the year:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 150, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 180, window=entry1)


def getSquareRoot():
    x1 = entry1.get()

    if variable.get() == 'Nationality':
        os.system('python nacionalitetipred.py ' + x1)
    elif variable.get() == 'Gender':
        os.system('python gjiniapred.py ' + x1)
    elif variable.get() == 'Violent deaths':
        os.system('python vdekjetedhunshmepred.py ' + x1)


OPTIONS = [
    "Nationality",
    "Gender",
    "Violent deaths"
]

variable = tkinter.StringVar(root)
variable.set(OPTIONS[0])
select = tkinter.OptionMenu(root, variable, *OPTIONS).place(relx=0.5, rely=0.3, anchor='center')

button1 = tk.Button(text='Show the graph', command=getSquareRoot, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 240, window=button1)

root.mainloop()
