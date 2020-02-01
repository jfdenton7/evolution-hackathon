from tkinter import *
from tkinter import ttk
from visualization import GeneratePetriDish
from simulation import colony
import json

title = "Bacterial Evolution"
water = "..\\simulation\\dataWATER.json"
ferr = "..\\simulation\\dataWATER.json"
aa = "..\\simulation\\dataWATER.json"
files = [water, ferr, aa]
jsondata = []
master = Tk()
master.title(title)
master.columnconfigure(0, weight=1)
master.rowconfigure(0, weight=1)

i = 0
for file in files:
    if file:
        with open(file, 'r') as f:
            jsondata[i] = json.load(f)
    i += 1

dish = colony.Dish()
petri = GeneratePetriDish(master, Dish().start_simul)
petri.populateScrollList()

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
