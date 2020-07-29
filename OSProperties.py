import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter.ttk import Combobox
import os

#get options
options = [option for option in vars(os) if not callable(getattr(os, option))]

#build main window form
window = tk.Tk()
window.iconbitmap("dog.ico")
window.title("Python Object Peek")
window.resizable(False, False)
window.geometry('450x250')

#labels
lbl = tk.Label(window, text="OS property", foreground="blue")
lbl.grid(column=0, row=1, padx=(10,10), pady=(10,10), sticky=tk.E)

lbl2 = tk.Label(window, text="Value", foreground="blue")
lbl2.grid(column=0, row=2, padx=(10,10), pady=(10,10), sticky=tk.E)

#scrolling text area
txtarea = ScrolledText(window, width=40, height=10)
txtarea.grid(column=1, row=2)

#combobox for selection
combo = Combobox(window, text="Choose")
combo['values'] = options
combo.current(1)
combo.grid(column=1, row=1, sticky=tk.W)

#handler for button clicked event
def clicked():
    option_chosen = combo.get()

    result = str(getattr(os, option_chosen))
    if not len(result):
        messagebox.showwarning('Warning', 'Property has no value')

    txtarea.delete(1.0, tk.END)
    txtarea.insert(tk.INSERT, result)

# button and handler declaration
btn = tk.Button(window, text="Show value", command=clicked)
btn.grid(column=1, row=3, padx=(10, 10), pady=(10, 10))

# activate main event loop
window.mainloop()
