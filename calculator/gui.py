from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
import logik


def show_error():
    mes = 'некорректный ввод'
    showinfo(title='', message=mes)


def clean():
    string_input.delete(0, END)


def make_window():
    root = Tk()
    root.resizable(width=False, height=False)
    # root['bg'] = '#4C1C24'
    root.title('Калькулятор')
    root.geometry('300x350')

    frame_entry = Frame(root, bg='#4C1C24', bd=5)
    frame_entry.place(relwidth=1, relheight=0.3)

    global string_input
    string_input = Entry(frame_entry, bg='white', bd=5, font=30)
    string_input.pack()

    global clean
    clean_button = Button(frame_entry, bg='white', bd=5, text='CLEAN', command=clean)
    clean_button.place(rely=0.5, relx=0.4)

    frame_but = Frame(root, bg='green', bd=5,)
    frame_but.place(rely=0.3, relwidth=1, relheight=0.7)

    for r in range(2):
        frame_but.rowconfigure(index=r, weight=1)
    for r in range(2):
        frame_but.columnconfigure(index=r, weight=1)

    button_add = Button(frame_but, text='+', font=40, command=logik.click_button_add)
    button_add.grid(column=0, row=0, sticky='nsew')

    button_min = Button(frame_but, text='-', font=1, command=logik.click_button_min)
    button_min.grid(column=1, row=0, sticky='nsew')

    button_ymn = Button(frame_but, text='*', font=1, command=logik.click_button_ymn)
    button_ymn.grid(column=0, row=1, sticky='nsew')

    button_del = Button(frame_but, text='/', font=1, command=logik.click_button_del)
    button_del.grid(column=1, row=1, sticky='nsew')

    root.mainloop()
