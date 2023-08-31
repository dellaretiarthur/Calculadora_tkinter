from tkinter import *
from tkinter import ttk
expression = ''


def mudar_cursor(event):
    event.widget.config(cursor="umbrella")

def keystroke(event):
    if event.char.isnumeric() or event.char in '-+/*%':
        press(event.char)


def press(num, event=None):
    global expression
    expression += str(num)
    equation.set(expression)
    

def clear():
    global expression
    expression = ''
    equation.set('')
    pass


def equalpress(event=None):
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        if len(total) < 10:
            equation.set(total)
        else:
            equation.set(total[:10])
        expression = total
    except:
        equation.set(' error ')
        expression = ''


def backspace(event):
    global expression
    expression = expression[:-1]
    equation.set(expression)


janela = Tk()
janela.title('Calculadora')
janela.resizable(False, False)

equation = StringVar()




tela = Entry(
    master=janela,
    state='normal',
    justify='right',
    font=('Arial', 70),
    width=5,
    fg='green',
    bg='#3B3936',
    relief='solid',
    borderwidth=18,
    textvariable=equation
    
)
tela.grid(row=0,column=0,columnspan=4)



janela.bind('<KeyPress>', keystroke)
janela.bind('<Return>', equalpress)
janela.bind('<BackSpace>', backspace)
janela.focus()

botao1 = Button(
    text='7',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#4D4D4D',
    activebackground='#3B3936',
    command=lambda: press(7)
    

)
botao1.grid(row=2, column=0, sticky=EW)

botao2 = Button(
    text='8',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#4D4D4D',
    activebackground='#3B3936',
    command=lambda: press(8)
    
)
botao2.grid(row=2, column=1, sticky=EW)

botao3 = Button(
    text='9',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#4D4D4D',
    activebackground='#3B3936',
    command=lambda: press(9)
    
    

)
botao3.grid(row=2, column=2, sticky=EW)

botao4 = Button(
    text='/',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#FE9708',
    activebackground='#3B3936',
    command=lambda: press('/')
    
)
botao4.grid(row=1, column=3, sticky=EW)

botao5 = Button(
    text='4',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#4D4D4D',
    activebackground='#3B3936',
    command=lambda: press(4)
    
)
botao5.grid(row=3, column=0, sticky=EW)

botao6 = Button(
    text='5',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#4D4D4D',
    activebackground='#3B3936',
    command=lambda: press(5)
    
)
botao6.grid(row=3, column=1, sticky=EW)

botao7 = Button(
    text='6',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#4D4D4D',
    activebackground='#3B3936',
    command=lambda: press(6)
    
)
botao7.grid(row=3, column=2, sticky=EW)

botao8 = Button(
    text='*',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#FE9708',
    activebackground='#3B3936',
    command=lambda: press('*')
    
)
botao8.grid(row=2, column=3, sticky=EW)

botao9 = Button(
    text='1',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#4D4D4D',
    activebackground='#3B3936',
    command=lambda: press(1)
    
)
botao9.grid(row=4, column=0, sticky=EW)

botao10 = Button(
    text='2',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#4D4D4D',
    activebackground='#3B3936',
    command=lambda: press(2)
    
)
botao10.grid(row=4, column=1, sticky=EW)

botao11 = Button(
    text='3',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#4D4D4D',
    activebackground='#3B3936',
    command=lambda: press(3)
    
)
botao11.grid(row=4, column=2, sticky=EW)

botao12 = Button(
    text='-',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#FE9708',
    activebackground='#3B3936',
    command=lambda: press('-')
    
)
botao12.grid(row=3, column=3, sticky=EW)

botao13 = Button(
    text='0',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#4D4D4D',
    activebackground='#3B3936',
    command=lambda: press(0)
    
)
botao13.grid(row=5, column=0, sticky=EW,columnspan=2)

botao14 = Button(
    text=',',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#4D4D4D',
    activebackground='#3B3936',
    
)
botao14.grid(row=5, column=2, sticky=EW)

botao15 = Button(
    text='+',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#FE9708',
    activebackground='#3B3936',
    command=lambda: press('+')
    
)
botao15.grid(row=4, column=3, sticky=EW)

botao16 = Button(
    text='=',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#FE9708',
    activebackground='#3B3936',
    command=equalpress
    
)
botao16.grid(row=5, column=3, sticky=EW)

botao17 = Button(
    text='C',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#FE9708',
    activebackground='#3B3936',
    command=clear
    
)
botao17.grid(row=1, column=0, sticky=EW)

botao18 = Button(
    text='+/-',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#FE9708',
    activebackground='#3B3936',
    
)
botao18.grid(row=1, column=1, sticky=EW)

botao19 = Button(
    text='%',
    font=('Trebuchet MS', 14),
    height=2,
    width=1,
    bg='#FE9708',
    activebackground='#3B3936',
    command=lambda: press('%')
    
)
botao19.grid(row=1, column=2, sticky=EW)


botao1.bind("<Enter>", mudar_cursor)
botao2.bind("<Enter>", mudar_cursor)
botao3.bind("<Enter>", mudar_cursor)
botao4.bind("<Enter>", mudar_cursor)
botao5.bind("<Enter>", mudar_cursor)
botao6.bind("<Enter>", mudar_cursor)
botao7.bind("<Enter>", mudar_cursor)
botao8.bind("<Enter>", mudar_cursor)
botao9.bind("<Enter>", mudar_cursor)
botao10.bind("<Enter>", mudar_cursor)
botao11.bind("<Enter>", mudar_cursor)
botao12.bind("<Enter>", mudar_cursor)
botao13.bind("<Enter>", mudar_cursor)
botao14.bind("<Enter>", mudar_cursor)
botao15.bind("<Enter>", mudar_cursor)
botao16.bind("<Enter>", mudar_cursor)
botao17.bind("<Enter>", mudar_cursor)
botao18.bind("<Enter>", mudar_cursor)
botao19.bind("<Enter>", mudar_cursor)


janela.mainloop()