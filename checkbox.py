import tkinter as tk     # Python3


def cb_checked():
    # remove text from label
    label['text'] = ''
    for ctr, int_var in enumerate(cb_intvar):
        if int_var.get():  # IntVar not zero==checked
            label['text'] += '%s is checked' % cb_list[ctr] + '\n'


root = tk.Tk()

cb_list = [
    'apple',
    'orange',
    'banana',
    'pear',
    'apricot'
]

# list of IntVar for each button
cb_intvar = []
for this_row, text in enumerate(cb_list):
    cb_intvar.append(tk.IntVar())
    tk.Checkbutton(root, text=text, variable=cb_intvar[-1],
                   command=cb_checked).grid(row=this_row,
                                            column=0, sticky='w')

label = tk.Label(root, width=20)
label.grid(row=20, column=0, sticky='w')

# you can preset check buttons (1=checked, 0=unchecked)
cb_intvar[3].set(1)
# show what is initially checked
cb_checked()

root.mainloop()
