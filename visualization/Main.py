from tkinter import *
from tkinter import ttk
from visualization import GeneratePetriDish
from simulation import colony
import json

title = "Bacterial Evolution"
water = "../evolutiondata/dataWATER.json"
ferr = "../evolutiondata/dataFERR.json"
aa = "../evolutiondata/dataAA.json"
files = [water, ferr, aa]
master = Tk()
master.title(title)
master.columnconfigure(0, weight=1)
master.rowconfigure(0, weight=1)

dish = colony.Dish()
petri = GeneratePetriDish.GeneratePetriDish(master, colony.Dish().start_simul, files)

master.mainloop()
