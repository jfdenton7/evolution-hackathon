from simulation.gene import GeneManager
from simulation.unit_manager import UnitManager

from threading import Thread


class Dish:

    def __init__(self, colonies: int, start_sz: int):
        """
        build a Dish to run an experiment

        :param colonies: the number of colonies
        :param start_sz: the starting size of these colonies
        """
        self.gm = GeneManager()
        self.um = UnitManager()

        self.num_cols = colonies
        self.dish = []
        self.__build_dish()

    def start_simul(self):
        colonies = []



        for i in range(self.num_cols):

            for cell in
            colonies.append(
                Thread()
            )

    def __build_dish(self):
        pass


if __name__ == '__main__':
    pass

