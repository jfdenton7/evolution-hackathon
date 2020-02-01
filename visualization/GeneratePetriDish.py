from tkinter import *
from tkinter import ttk


class GeneratePetriDish:
    def __init__(self, root, jsondata, generate):
        self.generate = generate
        self.frame = ttk.Frame(root, padding="5 5 5 5")
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.left = Canvas(self.frame, width=300, height=400, borderwidth=0, bg="dark gray")
        self.left.grid(column=0, row=0, sticky=(N, W, E, S))
        self.center = Canvas(self.frame, width=400, height=400, borderwidth=0, bg="gray")
        self.center.grid(column=1, row=0, sticky=(N, W, E, S))
        self.right = Canvas(self.frame, width=300, height=400, borderwidth=0, bg="dark gray")
        self.right.grid(column=2, row=0, sticky=(N, W, E, S))

        self.bottom = Canvas(self.frame, width=1000, height=100, borderwidth=0, bg="dark gray")
        self.bottom.config(scrollregion=(self.bottom.bbox("all")))
        self.bottom.grid(columnspan=3, row=1, sticky=(N, W, E, S))

        scroll = ttk.Scrollbar(self.frame, orient=HORIZONTAL, command=self.bottom.xview)
        scroll.grid(columnspan=3, row=2, sticky=(W, E))
        self.bottom.config(xscrollcommand=scroll.set)

        self.interior = ttk.Frame(canvas)
        


        self.jsondata = jsondata
        # self.settings()

    def populatePetridish(self, x, y):
        print(x, y)
        self.center.create_oval(11, 11, 391, 391, outline="white", width=3)
        self.jsondata["colonies"][index]

    def xyClick(self, event):
        print(event.widget.children)
        return self.populatePetridish(event.x_root, event.y_root)

    def populateScrollList(self):
        i = 0
        for colony in self.jsondata["colonies"]:
            c = Canvas(self.bottom, height=90, width=90, borderwidth=0, bg="black")
            c.bind("<Button-1>", self.xyClick)
            c.create_oval(10, 10, 80, 80, outline="white", width=2)
            c.create_oval(20, 20, 40, 40, fill="yellow")
            c.create_oval(70, 70, 60, 60, fill="yellow")
            c.create_oval(30, 60, 40, 70, fill="yellow")
            ttk.Label(self.bottom, text=colony["name"]).grid(column=i, row=1, sticky=S)
            c.grid(column=i, row=0, sticky=(N, W, E, S))
            i = i + 1

    # def settings(self):
        # ttk.Button(self.left, text="Generate", command=self.generate   .grid(column=0, row=0, sticky=N)