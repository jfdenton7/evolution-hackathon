from simulation.cell import Cell
from copy import deepcopy
from simulation.controller import Controller
from simulation.gene import GeneManager
from simulation.unit_manager import UnitManager
from simulation.config import (CIRC_SIDE, DISH_RADI, DELTA, FRONT,
                               DEFAULT_START_SZ, CARC_AA, CARC_FERR, CARC_WATER, MAX_COLONY_SZ)
from simulation.food import Food
from random import randrange, choice

from multiprocessing import Process, Queue

"""
Dish and Colony are titely coupled and
therefor need to be declared in the same file
"""


class Dish:

    def __init__(self):
        """
        build a Dish to run an experiment

        :param colonies: the number of colonies
        :param start_sz: the starting size of these colonies (num_cells)
        """
        self.gm = GeneManager()
        self.um = UnitManager()

        self.controller = None

        self.dish = []
        self.__build_dish()

    def start_simul_with_workers(self, num_cols, start_sz):
        """
        TODO
        :param num_cols:
        :param start_sz:
        :return:
        """
        # colonies = []
        pass
        # for i in range(num_cols):

        # determine colony position
        # y = randrange(len(self.dish))
        # x = randrange(len(self.dish[y]))
        #
        # #colony = Colony(start_sz, i)
        # # set position to have a colony
        # self.dish[y][x] = colony
        #
        # colonies.append(
        #     Process(target=colony.cycle_cells())
        #)

    def start_simul(self, num_colonies, test_sz, carc, model=None):
        """
        Start single threaded simulation of genetic test

        :param num_colonies: the number of starting colonies (configs to 1 bacteria starting)
        :param test_sz: the
        :param carc:
        :param model:
        :return:
        """
        colonies = []
        if not self.controller:
            self.controller = Controller(carc)

        for i in range(num_colonies):
            # determine colony position
            row = randrange(len(self.dish))
            col = randrange(len(self.dish[row]))

            colony = Colony(DEFAULT_START_SZ, i, self.gm, self.um,
                            self.dish, pos=(row, col), carc_lvl=carc, model=model)

            colonies.append(colony)

        max_col = colonies[0]
        max_cells = 0
        while True:
            for colony in colonies:
                colony.cycle_cells()
                sz = colony.num_cells()
                if sz == 0:
                    colonies.remove(colony)
                elif sz > max_cells:
                    max_col = colony
                    max_cells = sz
                    print('new max colony of size: ' + str(sz) + ' with radius ' + str(max_col.get_radius())
                          + ' and id: ' + str(max_col.id))

                max_col_sz = max_col.num_cells()
                if max_col_sz >= MAX_COLONY_SZ:
                    model = max_col.fetch_model()
                    # send trial data
                    self.controller.send_data(colonies, max_col, max_col_sz, max_col.get_radius(), False)
                    # start next sim
                    self.start_simul(num_colonies, test_sz - 1, carc, model=model)
                elif len(colonies) == 1:
                    if test_sz > 0:
                        # send trial data
                        self.controller.send_data(colonies, max_col, max_col_sz, max_col.get_radius(), False)
                        # start next sim
                        self.start_simul(num_colonies, test_sz - 1, carc, model=None)
                    else:
                        # end sim
                        self.controller.send_data(colonies, max_col, max_col_sz, max_col.get_radius(), True)
                        print('exiting simulation...')
                        exit(0)

            print('colonies remain: ' + str(len(colonies)))


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

        # model is a cell from any past colony...
        self.model = model

        # current radius of population,
        # increases when cell spreads to other position
        # in dish
        self.radius = 1

        self.__init_colony(init_sz, self.gm, self.um, self.carc)

    def __str__(self):
        s = ""
        for cell in self.cells:
            s += str(cell)
        return s

    def get_radius(self):
        return self.radius

    def col_pos(self):
        return self.pos

    def num_cells(self):
        return len(self.cells)

    def fetch_model(self) -> Cell:
        return deepcopy(choice(self.cells))

    def cycle_cells(self):
        """
        cycle through all cells in this colony
        and perform cycle calls, update data based
        on resulting cycle calls
        :return:
        """

        for cell in self.cells:
            life, split, modif, new_cell = cell.cycle(self.dish)
            if not life:
                self.cells.remove(cell)
            elif split:
                f = choice([lambda r, c: (r + modif, c),
                            lambda r, c: (r, c + modif),
                            lambda r, c: (r - modif, c),
                            lambda r, c: (r, c - modif)])

                orig = cell.get_pos()
                row, col = f(*orig)
                if self.__bounded(row, col):
                    self.cells.append(new_cell)
                    new_cell.set_pos((row, col))
                    if modif > 0:
                        self.radius = max(abs(row - self.pos[0]), abs(col - self.pos[1]))
                else:
                    self.cells.append(new_cell)

    def __bounded(self, row, col):
        return (0 <= row < len(self.dish)) and (0 <= col < len(self.dish[row]))

    def __init_colony(self, sz, gm, um, carc):
        for i in range(sz):
            if self.model:
                self.cells.append(deepcopy(self.model))
            else:
                self.cells.append(Cell(gm, um, pos=self.pos, col_id=self.id))
        print('starting colony ' + str(self.id) + ' with: ' + str(len(self.cells)) + ' cells')


if __name__ == '__main__':
    Dish().start_simul(15, 1, CARC_WATER)
