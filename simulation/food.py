from simulation.config import *
from copy import deepcopy


class Food:

    def __init__(self):
        self.food_amt = deepcopy(BASE_FOOD_DISTR)

    def next(self):
        """
        get next available food,
        follows this ordering:
        - GLUCOSE
        - PENTOSE
        - FRUCTOSE
        - AMYLOSE

        :return: food type
        """
        if self.food_amt[GLUCOSE] > 0:
            self.food_amt[GLUCOSE] -= 1
            return GLUCOSE
        elif self.food_amt[PENTOSE] > 0:
            self.food_amt[PENTOSE] -= 1
            return PENTOSE
        elif self.food_amt[FRUCTOSE] > 0:
            self.food_amt[FRUCTOSE] -= 1
            return FRUCTOSE
        elif self.food_amt[AMYLOSE] > 0:
            self.food_amt[AMYLOSE] -= 1
            return AMYLOSE