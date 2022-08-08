from tkinter import *
from tkinter import ttk

root = Tk()


def callback():
    key = var_person.get()
    try:  # To bypass the error when user chooses nothing
        value = my_dict[key]  # get the corresponding value from the given key
        print(value)  # print it
    except KeyError:
        print('Please choose an option')  # error message


my_list = [(1, 'Python'), (2, 'Curso de Python')]

my_dict = dict(map(reversed, my_list))

var_person = StringVar()
cb = ttk.Combobox(root, values=list(my_dict.keys()),  textvariable=var_person)
# setting the current value to index position 1 of the list(optional)
cb.current(1)
cb.pack(pady=10, padx=10)

b = Button(root, text='Click me', command=callback).pack(pady=10, padx=10)

root.mainloop()
