from tkinter import *
from tkinter import ttk


class GeneratePetriDish:
    def __init__(self, root, jsondata, generate):
        self.generate = generate
        self.frame = ttk.Frame(root, padding="5 5 5 5")
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.canLeft = Canvas(self.frame, width=300, height=400, borderwidth=0, bg="dark gray")
        self.canLeft.grid(column=0, row=0, sticky=(N, W, E, S))
        self.left = ttk.Frame(self.canLeft, padding="5 5 5 5")
        self.left.grid(column=0, row=0, sticky=(N, W, E, S))
        self.center = Canvas(self.frame, width=400, height=400, borderwidth=0, bg="gray")
        self.center.grid(column=1, row=0, sticky=(N, W, E, S))
        self.right = Canvas(self.frame, width=300, height=400, borderwidth=0, bg="dark gray")
        self.right.grid(column=2, row=0, sticky=(N, W, E, S))

        self.scrollFrame = ttk.Frame(self.frame).grid(columnspan=3, row=1, sticky=(N, W, E, S))

        # scroll = Scrollbar(self.scrollFrame, orient=HORIZONTAL)
        # scroll.pack(fill=X, side=BOTTOM, expand=FALSE)
        # self.bottom = Canvas(self.scrollFrame, bd=0, highlightthickness=0,
        #                 xscrollcommand=scroll.set)
        # self.bottom.pack(side=TOP, fill=BOTH, expand=TRUE)

        self.bottom = Canvas(self.frame, height=100, width=1000, borderwidth=0, bg="dark gray")
        self.bottom.grid(columnspan=3, row=1, sticky=(N, W, E, S))

        # scroll.config(command=self.bottom.xview)
        self.interior = Frame(self.bottom)

        self.jsondata = jsondata
        self.settings = self.settings()

    def populatePetridish(self, index):
        self.center.create_oval(11, 11, 391, 391, outline="white", width=3)


    def xyClick(self, event):
        if 600 < event.y_root:
            if 170 < event.x_root < 260:
                return self.populatePetridish(0)
            if 270 < event.x_root < 360:
                return self.populatePetridish(1)
            if 370 < event.x_root < 460:
                return self.populatePetridish(2)
            if 470 < event.x_root < 560:
                return self.populatePetridish(3)
            if 570 < event.x_root < 660:
                return self.populatePetridish(4)
            if 670 < event.x_root < 760:
                return self.populatePetridish(5)
            if 770 < event.x_root < 860:
                return self.populatePetridish(6)
            if 870 < event.x_root < 960:
                return self.populatePetridish(7)
            if 970 < event.x_root < 1060:
                return self.populatePetridish(8)
        if 200 < event.y_root < 300:
            if 180 < event.x_root < 375:
                self.generate(15, int(self.settings["e"].get()) if type(int(self.settings["e"].get())) == int else 8,
                              self.settings["m"])
    
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

    def settings(self):
        evo = Canvas(self.left, height=90, width=200, borderwidth=0, bg="dark green")
        evo.bind("<Button-1>", self.xyClick)
        evo.grid(column=0, row=0, sticky=N)

        mutagens = IntVar()

        ttk.Radiobutton(self.left, text="Water", variable=mutagens, value=1, underline=FALSE).grid(column=0, row=1)
        ttk.Radiobutton(self.left, text="Formaldehyde", variable=mutagens, value=2, underline=FALSE).grid(column=0, row=2)
        ttk.Radiobutton(self.left, text="2-Aminofluorine", variable=mutagens, value=3, underline=FALSE)\
            .grid(column=0, row=3)

        entry = ttk.Entry(self.left).grid(column=0, row=5)

        return {"e": entry, "m": mutagens}
