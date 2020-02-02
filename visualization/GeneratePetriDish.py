from tkinter import *
from tkinter import ttk
import json

class GeneratePetriDish:
    populateArray = []

    def __init__(self, root, generate, jsondata):
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
        self.bottom = Canvas(self.frame, height=100, width=1000, borderwidth=0, bg="dark gray")
        self.bottom.grid(columnspan=3, row=1, sticky=(N, W, E, S))
        self.jsondata = jsondata
        self.settings = self.settings()


    def populatePetridish(self, trial):
        self.center.delete("all")
        for bacteria in trial["colonies"]:
            x = bacteria["x"]
            y = bacteria["y"]
            radius = bacteria["radius"]
            x1 = x - radius + 200
            y1 = y - radius + 200
            x2 = x + radius + 200
            y2 = y + radius + 200
            self.center.create_oval(y1, x1, y2, x2, fill="yellow")
        self.center.create_oval(11, 11, 391, 391, outline="white", width=3)

    def xyClick(self, event):
        m = self.settings["m"].get() if 0 < self.settings["m"].get() < 4 else 1
        filepath = self.jsondata[m-1]
        if filepath:
            with open(filepath, 'r') as f:
                data = json.load(f)
        # self.generate(15, 8, m)
        self.populateScrollList(data)

    def populateScrollList(self, json):
        i = 0
        for trial in json["trials"]:
            c = Canvas(self.bottom, height=90, width=90, borderwidth=0, bg="black")
            c.create_oval(10, 10, 80, 80, outline="white", width=2)
            c.create_oval(20, 20, 40, 40, fill="yellow")
            c.create_oval(70, 70, 60, 60, fill="yellow")
            c.create_oval(30, 60, 40, 70, fill="yellow")
            name = trial["trial_id"]
            Button(self.bottom, text=name, command=lambda trial=trial: self.populatePetridish(trial)).grid(
                column=i, row=1, sticky=S)
            c.grid(column=i, row=0, sticky=(N, W, E, S))
            i = i + 1

    def settings(self):
        evo = Canvas(self.left, height=90, width=200, borderwidth=0, bg="dark green")
        evo.bind("<Button-1>", self.xyClick)
        evo.grid(column=0, row=0, sticky=N)

        mutagens = IntVar()

        ttk.Radiobutton(self.left, text="Water", variable=mutagens, value=1, underline=FALSE).grid(column=0, row=1)
        ttk.Radiobutton(self.left, text="Formaldehyde", variable=mutagens, value=2, underline=FALSE).grid(column=0,
                                                                                                          row=2)
        ttk.Radiobutton(self.left, text="2-Aminofluorine", variable=mutagens, value=3, underline=FALSE) \
            .grid(column=0, row=3)

        text = StringVar()
        # entry = ttk.Entry(self.left, textvariable=text, command=lambda text: self.settings.append({"e": int(text)})).grid(column=0, row=5)

        return {"m": mutagens}

