from simulation.gene import GeneManager
from simulation.colony import Colony
from simulation.unit_manager import UnitManager
from simulation.config import CIRC_SIDE, DISH_RADI, DELTA, FRONT
from simulation.food import Food
from random import randrange

from multiprocessing import Process, Queue


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
            colony = Colony(start_sz, i)

            x = randrange(len(self.dish))
            y = randrange(len(self.dish[x]))

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


if __name__ == '__main__':
    dish = Dish(0, 0).get_dish()
    for row in dish:
        print(row)

