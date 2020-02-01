from tkinter import *
from tkinter import ttk


class GeneratePetriDish:
    def __init__(self, root, jsondata):
        self.frame = ttk.Frame(root, padding="5 5 5 5")
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.frame.focus()
        self.left = Canvas(self.frame, width=300, height=400, borderwidth=0, bg="dark gray")
        self.left.grid(column=0, row=0, sticky=(N, W, E, S))
        self.center = Canvas(self.frame, width=400, height=400, borderwidth=0, bg="gray")
        self.center.grid(column=1, row=0, sticky=(N, W, E, S))
        self.right = Canvas(self.frame, width=300, height=400, borderwidth=0, bg="dark gray")
        self.right.grid(column=2, row=0, sticky=(N, W, E, S))
        self.bottom = Canvas(self.frame, width=1000, height=100, borderwidth=0, bg="dark gray")
        self.bottom.grid(columnspan=3, row=1, sticky=(N, W, E, S))
        self.center.create_oval(11, 11, 391, 391, outline="white", width=3)
        self.jsondata = jsondata

    def populateScrollList(self):
        listbox = Listbox(self.bottom, height=5)
        listbox.grid(column=0, row=0, sticky=(N, W, E, S))
        scroll = ttk.Scrollbar(self.bottom, orient=VERTICAL, command=listbox.xview)
        scroll.grid(column=1, row=0, sticky=(W, E))
        listbox['xscrollcommand'] = scroll.set
        self.bottom.grid_columnconfigure(0, weight=1)
        self.bottom.grid_rowconfigure(0, weight=1)
        for colony in self.jsondata.colonies:
            listbox.insert('end', colony.name)
