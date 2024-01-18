from tkinter import *
import minor_windows
from logic2 import list_notes


def make_main_window():
    root = Tk()
    root.resizable(height=False, width=False)
    root['bg'] = '#4C1C24'
    root.title('Notes')
    root.geometry('350x400')

    def search_note_handler():
        print('search_note')

    def add_handler():
        minor_windows.make_add_window()
        print('make_add_window')

    def update_listbox():
        print('eeeeeeeeee')
        # show_entry.delete(0, END)
        dic = list_notes.get_list_note()
        lst = list(dic.keys())
        for x in range(len(lst)):
            show_entry.insert(END, lst[x])

    def del_note_handler():
        print('del_note')

    def change_note_handler():
        print('change_note')

    def show_note_handler():
        print('show_note')

    for a in range(3):
        root.grid_columnconfigure(index=a, weight=1)

    root.grid_rowconfigure(index=0, weight=1)
    root.grid_rowconfigure(index=1, weight=5)
    root.grid_rowconfigure(index=2, weight=1)

    input_entry = Entry()
    input_entry.grid(row=0, column=0, padx=6, pady=6, sticky=EW, ipady=3)

    search_note_button = Button(text="Search note", command=search_note_handler)
    search_note_button.grid(row=0, column=1, padx=6, pady=6,  sticky=EW)

    add_button = Button(text='Add Note', command=add_handler)
    add_button.grid(column=2, row=0, padx=6, pady=6,  sticky=EW)

    show_entry = Listbox(bg='#f4f5dc', selectbackground='#2c61c9', width=20, yscrollcommand='True')
    show_entry.grid(row=1, column=0, columnspan=3, sticky=NSEW, padx=3, pady=3)

    del_button = Button(text='Delite note', command=del_note_handler)
    del_button.grid(row=2, column=0, padx=6, pady=6,  sticky=EW)

    change_button = Button(text='Change note', command=change_note_handler)
    change_button.grid(row=2, column=1, padx=6, pady=6,  sticky=EW)

    show_button = Button(text='Show note', command=show_note_handler)
    show_button.grid(row=2, column=2, padx=6, pady=6,  sticky=EW)

    update_listbox()

    root.mainloop()


make_main_window()