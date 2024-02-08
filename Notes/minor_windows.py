from tkinter import *
from logic2 import App


def make_add_window():

    root2 = Toplevel()
    root2.resizable(height=False, width=False)
    root2['bg'] = '#4C1C24'
    root2.title('Create note')
    root2.geometry('200x200')

    for i in range(5):
        root2.grid_rowconfigure(index=i, weight=1)
        root2.grid_columnconfigure(index=0, weight=1)
        root2.grid_columnconfigure(index=1, weight=1)

    def add():
        App.add_note(name_entry.get(), note_entry.get())
        root2.grab_release()

    def dismiss(window):
        root2.grab_release()
        root2.destroy()

    label_1 = Label(root2, text='Input name of note', bg='#4C1C24', font=40)
    label_1.grid(row=0, columnspan=2, sticky=NSEW, padx=6, pady=(10, 0))

    label_2 = Label(root2, text='Input note', bg='#4C1C24', font=40)
    label_2.grid(row=2, columnspan=2, sticky=NSEW, padx=6, pady=(0, 0))

    name_entry = Entry(root2)
    name_entry.grid(row=1, columnspan=2, sticky=NSEW, padx=6, pady=(0, 9), ipady=4)

    note_entry = Entry(root2)
    note_entry.grid(row=3, columnspan=2, sticky=NSEW, padx=6, pady=(0, 9), ipady=4)

    add_button1 = Button(root2, text='ADD NOTE', command=add)
    add_button1.grid(row=4, sticky=W, padx=20, pady=3, ipadx=5)

    return_button = Button(root2, text='Cancel', command=lambda: root2.grab_release())
    return_button.grid(row=4, column=1, sticky=E, padx=20, pady=3, ipadx=5)

    root2.mainloop()

