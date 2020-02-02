from tkinter import *
from tkinter import ttk
from visualization import GeneratePetriDish
from simulation import colony

title = "Bacterial Evolution"
water = "../simulation/dataWATER.json"
ferr = "../simulation/dataFERR.json"
aa = "../simulation/dataAA.json"
files = [water, ferr, aa]
jsondata = [water, ferr, aa]
master = Tk()
master.title(title)
master.columnconfigure(0, weight=1)
master.rowconfigure(0, weight=1)



dish = colony.Dish()
petri = GeneratePetriDish.GeneratePetriDish(master, dish.start_simul, jsondata)

master.mainloop()
