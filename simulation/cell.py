from simulation.config import *
from simulation.gene import GeneManager
from simulation.unit_manager import UnitManager
from random import choice, randrange, random
from math import floor

# number of genes directly corresponds to the number
# of terminals in a gene.
# 0.0 - 1.0
# having < .50 result damages cell
# < .25 gene is broken
# having > .50 results in favorable mutations

# each terminal represents


class Cell:

    def __init__(self, gm: GeneManager, um: UnitManager, pos, options=DEFAULT_START, carc_lvl=0):
        self.unit_manager = um
        self.gene_manager = gm
        self.pos = pos

        # carc lvl determines added weighted
        self.carc_lvl = carc_lvl

        self.genome = None
        self.__generate_genome()

        self.options = options

        self.atp = self.options[ATP]
        self.phase = self.options[PHASE_START]

        self.size = self.options[CELL_SZ]
        self.hunger = self.options[HUNGER]

        self.is_splitting = False
        self.is_alive = True
        self.age = 0

    def __str__(self):
        """
        cell is represented by a series
        of encoded genes...

        {
        domain_proteins: ...
        atp_generators: ...
        cancer_prevention: ...
        mitosis: ...
        duplicaters: ...
        poopers: ...
        q_sensing: ... <-- cell density
        # note poor q sensors results in higher cell density, increasing cost per 'block'
        ...
        }
        :return: str representing genetic code (expressions)
        """
        s = ""
        s += "HISTIDINE: " + self.genome[GENE_HIST][1]
        s += "GLUCOSE: " + self.genome[GENE_HIST][1]
        s += "PENTOSE: " + self.genome[GENE_HIST][1]
        s += "FRUCTOSE: " + self.genome[GENE_HIST][1]
        s += "AMYLOSE: " + self.genome[GENE_HIST][1]
        s += "HISTIDINE: " + self.genome[GENE_HIST][1]



        return s

    def __generate_genome(self):
        # form of genome follows:
        # (genetic_code:str, performance:float, working:bool)
        self.genome = {
           GENE_HIST: self.unit_manager.build_genome(*HIST_GENE, self.gene_manager, self),

            # sugars
            GENE_GLUC: self.unit_manager.build_genome(*GLUC, self.gene_manager, self),
            GENE_PENT: self.unit_manager.build_genome(*PENT, self.gene_manager, self),
            GENE_FRUC: self.unit_manager.build_genome(*FRUC, self.gene_manager, self),
            GENE_AMYL: self.unit_manager.build_genome(*AMLY, self.gene_manager, self),

            # checkpoints
            GENE_G1_S: self.unit_manager.build_genome(*G1_S, self.gene_manager, self),
            GENE_G2_M: self.unit_manager.build_genome(*G2_M, self.gene_manager, self),

            # cell cycles
            GENE_CELL: self.unit_manager.build_genome(*CELL_CYCLE, self.gene_manager, self),

            # DNA replication
            GENE_DNA: self.unit_manager.build_genome(*DNA_REP, self.gene_manager, self),

            # excrete
            GENE_EXCR: self.unit_manager.build_genome(*EXCRETE, self.gene_manager, self),

            # q-sensing
            GENE_Q: self.unit_manager.build_genome(*Q_SENSES, self.gene_manager, self)}

    def __mutate(self):
        self.unit_manager.mutate_genome(self.gene_manager, choice(list(self.genome.values())))

    def cycle(self, dish):
        # only perform is alive
        if self.is_alive:
            self.__eat(dish)
            self.__mutate()

            # perform this phase's action
            self.__phase()

            self.__age()

        if self.is_splitting:
            modif = self.unit_manager.effective_modifier(self.genome[GENE_Q])
            return self.is_alive, self.is_splitting, floor(modif)

        return self.is_alive, self.is_splitting, 0

    def __eat(self, dish):
        """
        attempt to find food in current block

        :return:
        """
        self.__find_food(dish)

        # consume living energy
        self.atp -= self.hunger
        if self.atp < 0:
            # could not afford to eat
            self.die()

    def __find_food(self, dish):
        # find position of cell
        x, y = self.pos

        # check if food available in pos
        food = dish[x][y].next()
        if food:
            self.__consume(food)

    def __consume(self, food):

        if food is GLUCOSE:
            mod = self.unit_manager.effective_modifier(self.genome[GENE_GLUC])
            self.atp += BASE_FOOD_PROD[GLUCOSE] + BASE_FOOD_PROD[GLUCOSE] * mod
        elif food is FRUCTOSE:
            mod = self.unit_manager.effective_modifier(self.genome[GENE_FRUC])
            self.atp += BASE_FOOD_PROD[FRUCTOSE] +  BASE_FOOD_PROD[FRUCTOSE] * mod
        elif food is PENTOSE:
            mod = self.unit_manager.effective_modifier(self.genome[GENE_PENT])
            self.atp += BASE_FOOD_PROD[PENTOSE] + BASE_FOOD_PROD[PENTOSE] * mod
        elif food is AMYLOSE:
            mod = self.unit_manager.effective_modifier(self.genome[GENE_AMYL])
            self.atp += BASE_FOOD_PROD[AMYLOSE] + BASE_FOOD_PROD[AMYLOSE] * mod

    def __phase(self):
        """
        see if cell is capable
        of phase check...

        handles
        - growth of cell
        - phase progression of cell

        :return: none
        """

        # phase 1 is growth phase
        if self.phase is Phase.G1:
            if self.atp > COSTS[GROWTH]:
                self.atp -= COSTS[GROWTH]
                self.phase = Phase.S
                # double in size
                self.size += self.size
                # increase hunger
                self.hunger += COSTS[HUNGER_GROWTH]
        # phase 2 is DNA replication
        elif self.phase is Phase.S:
            if self.atp > COSTS[DNA]:
                self.atp -= COSTS[DNA]
                self.phase = Phase.G2
        # phase 3 is repeated growth
        elif self.phase is Phase.G2:
            if self.atp > COSTS[GROWTH]:
                self.atp -= COSTS[GROWTH]
                self.phase = Phase.M
                # grow in size and hunger
                self.size += self.size
                self.hunger += COSTS[HUNGER_GROWTH]
        # phase 4 is to split, M-phase, inform colony!!!
        else:
            modif = self.unit_manager.effective_modifier(self.genome[GENE_DNA]) + self.options[SPLIT_BIAS]
            bar = random()
            # only split if capable
            if modif > bar:
                self.is_splitting = True

            self.phase = Phase.G1
            # restarting...

        if self.atp < 0:
            self.die()

    def die(self):
        """
        cell dies

        :return:
        """
        self.is_alive = False

    def __age(self):
        self.age += 1
        if self.age > DEFAULT_START[MAX_AGE]:
            self.die()

    def get_pos(self):
        return self.pos


if __name__ == '__main__':
    cell = Cell(GeneManager(), UnitManager())
    print(cell)



