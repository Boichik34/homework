from tkinter import *


def make_window():
    def add():
        print('add')

    root = Tk()
    root.resizable(height=False, width=False)
    root['bg'] = '#4C1C24'
    root.title('Notes')
    root.geometry('350x400')

    root.grid_columnconfigure(index=0, weight=2)
    root.grid_columnconfigure(index=1, weight=1)
    root.grid_rowconfigure(index=0, weight=1)
    root.grid_rowconfigure(index=1, weight=5)
    root.grid_rowconfigure(index=2, weight=1)

    input_1 = Entry()
    input_1.grid(row=0, column=0, padx=6, pady=6, ipady=3, sticky=EW)

    add_button = Button(text='Add Note', command=add).grid(column=1, row=0, padx=6, pady=6)

    show_entry = Listbox()
    show_entry.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=3, pady=3)

    root.mainloop()


make_window()
