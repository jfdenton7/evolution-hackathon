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
        self.bottom.config(scrollregion=self.bottom.bbox("all"))
        self.bottom.grid(columnspan=3, row=1, sticky=(N, W, E, S))
        scroll = ttk.Scrollbar(self.frame, orient=HORIZONTAL, command=self.bottom.xview)
        scroll.grid(columnspan=3, row=2, sticky=(W, E))
        self.bottom.config(xscrollcommand=scroll.set)
        self.center.create_oval(11, 11, 391, 391, outline="white", width=3)
        self.jsondata = jsondata

    def populateScrollList(self):
        i = 0
        for colony in self.jsondata["colonies"]:
            c = Cavnas(self.bottom, height=90, width=90, borderwidth=0, bg"light black")
            c.create_oval(2, 2, 36, 36, outline="white", width=2)
            ttk.Label(c, text=colony["name"], column=i, row=1, sticky=S)
            c.grid((column=i, row=0, sticky=(N, W, E, S)))
            i++
