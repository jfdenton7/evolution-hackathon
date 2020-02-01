from tkinter import *
from tkinter import ttk
from GeneratePetriDish import GeneratePetriDish
import json

title = "Trial x"
filename = "..\evolutiondata\evo_mutigens_timestamp.json"
master = Tk()
master.title(title)
master.columnconfigure(0, weight=1)
master.rowconfigure(0, weight=1)

if filename:
    with open(filename, 'r') as f:
        datastore = json.load(f)

petri = GeneratePetriDish(master, datastore)
# petri.populateScrollList()

# label = ttk.Label(frame, textvariable=v).grid(column=2, row=2, sticky=(W, E))
# ttk.Button(frame, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
#
# ttk.Label(frame, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(frame, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(frame, text="meters").grid(column=3, row=2, sticky=W)

# for child in frame.winfo_children():
#     child.grid_configure(padx=5, pady=5)
# # label.focus()
# master.bind('<Return>', calculate)

master.mainloop()
