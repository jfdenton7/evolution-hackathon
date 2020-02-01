from simulation.cell import Cell

from simulation.gene import GeneManager
from simulation.unit_manager import UnitManager
from simulation.config import CIRC_SIDE, DISH_RADI, DELTA, FRONT
from simulation.food import Food
from random import randrange, choice

from multiprocessing import Process, Queue

"""
Dish and Colony are titely coupled and
therefor need to be declared in the same file
"""

class Dish:

    def __init__(self, colonies: int, start_sz: int):
        """
        build a Dish to run an experiment

        :param colonies: the number of colonies
        :param start_sz: the starting size of these colonies (num_cells)
        """
        self.gm = GeneManager()
        self.um = UnitManager()

        self.num_cols = colonies
        self.dish = []
        self.__build_dish()

    def start_simul(self, start_sz):
        colonies = []

        for i in range(self.num_cols):

            # determine colony position
            x = randrange(len(self.dish))
            y = randrange(len(self.dish[x]))

            colony = Colony(start_sz, i)
            # set position to have a colony
            self.dish[x][y] = colony

            colonies.append(
                Process(target=colony.cycle_cells())
            )

    def __build_dish(self):
        """
        build the dish
        :return:
        """
        start = DISH_RADI
        for i in range(CIRC_SIDE):
            _row = [Food()] * start
            start -= DELTA
            self.dish.append(_row)
            self.dish.insert(FRONT, _row)

    def get_dish(self):
        return self.dish


# if __name__ == '__main__':
#     dish = Dish(0, 0).get_dish()
#     for row in dish:
#         print(row)


class Colony:

    def __init__(self, init_sz, id, gm: GeneManager, um: UnitManager, dish: list, pos, model=None, carc_lvl=0):
        """
        build a colony of init_sz,
        if model is not specified

        :param init_sz: number of sizes starting off in the colony
        :param model: if random is not wanted, have a cell model...
        """
        self.cells = []
        self.id = id

        self.pos = pos
        self.dish = dish

        self.gm = gm
        self.um = um
        self.carc = carc_lvl

        # current radius of population,
        # increases when cell spreads to other position
        # in dish
        self.radius = 0

        self.__init_colony(init_sz, self.gm, self.um, self.carc)

    def col_pos(self):
        return self.pos

    def cycle_cells(self):
        """
        cycle through all cells in this colony
        and perform cycle calls, update data based
        on resulting cycle calls
        :return:
        """

        for cell in self.cells:
            life, split, modif = cell.cycle(self.dish)
            if not life:
                self.cells.remove(cell)
            elif split:
                f = choice([lambda x, y: (x + modif, y),
                            lambda x, y: (x, y + modif),
                            lambda x, y: (x - modif, y),
                            lambda x, y: (x, y - modif)])

                orig = cell.get_pos()
                x, y = f(*orig)
                if self.__bounded(x, y):
                    self.cells.append(Cell(self.gm, self.um, pos=(x, y), carc_lvl=self.carc))
                    if modif > 0:
                        self.radius
                else:
                    self.cells.append(Cell(self.gm, self.um, pos=orig, carc_lvl=self.carc))

    def __bounded(self, x, y):
        return (0 <= y < len(self.dish)) and (0 <= x < len(self.dish[y]))

    def __init_colony(self, sz, gm, um, carc):
        for i in range(sz):
            self.cells.append(Cell(gm, um, pos=self.pos))


if __name__ == '__main__':
    gm = GeneManager()
    um = UnitManager()

    dish = Dish(0, 0).get_dish()

    col = Colony(1, 0, gm, um, dish, (0, 0))
    for i in range(10):
        col.cycle_cells()
