import tkinter as tk
from tkinter import messagebox
def make__but_dig(digit):
    return tk.Button(win, text=digit, bd=5, command=lambda: add__dig(digit), font=('Arial', 13))
def make__but_oper(oper):
    return tk.Button(win, text=oper, bd=5, command=lambda: add__oper(oper), font=('Arial', 13), fg ='red')
def make__but_calculate(oper):
    return tk.Button(win, text=oper, bd=5, command=calculate, font=('Arial', 13), fg ='red')
def make__but_clear(oper):
    return tk.Button(win, text=oper, bd=5, command=clear, font=('Arial', 13), fg ='red')
def add__dig(digit):
    value = calc.get()
    if value[0] == '0' and len(value)==1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)
def add__oper(oper):
    value = calc.get()
    if value[-1] in '+-*/':
       value = value[:1]
    #elif '+' in value or '-' in value or '*' in value or '/' in value:
    #    calculate()
    #    value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value+oper)
def calculate():
    value = calc.get()
    if value[-1] in '+-/*':
        oper = value[-1]
        value = value[:-1]+oper+value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', 'Нужно вводить цифры')
        calc.insert(0, 0)
    except ZeroDivisionError: 
        messagebox.showinfo('Внимание','На ноль делить нельзя')
def clear():
    calc.delete(0, tk.END)
    calc.insert(0, 0)
def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add__dig(event.char)
    elif event.char in '+-/*':
        add__oper(event.char)
    elif event.char == '\r':
        calculate()
win = tk.Tk()
win.title('Калькулятор')
win['bg']='#302BDB'
win.geometry(f'240x300+100+150')
win.resizable(False, False)
win.bind('<Key>', press_key)
calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial',15))
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4)
make__but_dig('1').grid (row = 1, column = 0, padx = 5, pady = 5, sticky = 'wens' )
make__but_dig('2').grid (row = 1, column = 1, padx = 5, pady = 5, sticky = 'wens' )
make__but_dig('3').grid (row = 1, column = 2, padx = 5, pady = 5, sticky = 'wens' )
make__but_dig('4').grid (row = 2, column = 0, padx = 5, pady = 5, sticky = 'wens' )
make__but_dig('5').grid (row = 2, column = 1, padx = 5, pady = 5, sticky = 'wens' )
make__but_dig('6').grid (row = 2, column = 2, padx = 5, pady = 5, sticky = 'wens' )
make__but_dig('7').grid (row = 3, column = 0, padx = 5, pady = 5, sticky = 'wens' )
make__but_dig('8').grid (row = 3, column = 1, padx = 5, pady = 5, sticky = 'wens' )
make__but_dig('9').grid (row = 3, column = 2, padx = 5, pady = 5, sticky = 'wens' )
make__but_dig('0').grid (row = 4, column = 0, padx = 5, pady = 5, sticky = 'wens' )
make__but_oper('+').grid (row = 1, column = 3, padx = 5, pady = 5, sticky = 'wens' )
make__but_oper('-').grid (row = 2, column = 3, padx = 5, pady = 5, sticky = 'wens' )
make__but_oper('*').grid (row = 3, column = 3, padx = 5, pady = 5, sticky = 'wens' )
make__but_oper('/').grid (row = 4, column = 3, padx = 5, pady = 5, sticky = 'wens' )
make__but_calculate('=').grid (row = 4, column = 2, padx = 5, pady = 5, sticky = 'wens' )
make__but_clear('C').grid (row = 4, column = 1, padx = 5, pady = 5, sticky = 'wens' )
win.grid_columnconfigure(0, minsize= 60)
win.grid_columnconfigure(1, minsize= 60)
win.grid_columnconfigure(2, minsize= 60)
win.grid_columnconfigure(3, minsize= 60)
win.grid_rowconfigure(0, minsize= 60)
win.grid_rowconfigure(1, minsize= 60)
win.grid_rowconfigure(2, minsize= 60)
win.grid_rowconfigure(3, minsize= 60)
win.grid_rowconfigure(4, minsize= 60)
win.mainloop()