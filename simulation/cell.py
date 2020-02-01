from simulation.config import *
from simulation.gene import GeneManager
from simulation.unit_manager import UnitManager
from random import choice

# number of genes directly corresponds to the number
# of terminals in a gene.
# 0.0 - 1.0
# having < .50 result damages cell
# < .25 gene is broken
# having > .50 results in favorable mutations

# each terminal represents


class Cell:

    def __init__(self, gm: GeneManager, um: UnitManager, options=DEFAULT_START, carc_lvl=0):
        self.unit_manager = um
        self.gene_manager = gm

        # carc lvl determines
        self.carc_lvl =carc_lvl

        self.genome = None
        self.__generate_genome()

        self.atp = DEFAULT_START[ATP]
        self.phase = DEFAULT_START[PHASE_START]

        self.size = DEFAULT_START[CELL_SZ]
        self.hunger = DEFAULT_START[HUNGER]

        self.is_splitting = False

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
        for gene_unit in self.genome:
            for gene in gene_unit:
                s += str(gene) + "\n"
        return s

    def __generate_genome(self):
        # form of genome follows:
        # (genetic_code:str, performance:float, working:bool)
        self.genome = [
            self.unit_manager.build_genome(*HIST_GENE, self.gene_manager),

            # sugars
            self.unit_manager.build_genome(*GLUC, self.gene_manager),
            self.unit_manager.build_genome(*PENT, self.gene_manager),
            self.unit_manager.build_genome(*FRUC, self.gene_manager),
            self.unit_manager.build_genome(*AMLY, self.gene_manager),

            # checkpoints
            self.unit_manager.build_genome(*G1_S, self.gene_manager),
            self.unit_manager.build_genome(*G2_M, self.gene_manager),

            # cell cycles
            self.unit_manager.build_genome(*CELL_CYCLE, self.gene_manager),

            # DNA replication
            self.unit_manager.build_genome(*DNA_REP, self.gene_manager),

            # excrete
            self.unit_manager.build_genome(*EXCRETE, self.gene_manager),

            # q-sensing
            self.unit_manager.build_genome(*Q_SENSES, self.gene_manager)]

    def __mutate(self):
        self.unit_manager.mutate_genome(self.gene_manager, choice(self.genome))

    def cycle(self):
        self.__eat()
        self.__mutate()

        # perform this phase's action
        self.__phase()

        self.__age()

    def __eat(self):
        """
        attempt to find food in current block

        :return:
        """
        pass

    def __phase(self):
        """
        see if cell is capable
        of phase check...

        handles
        - growth of cell
        - phase progression of cell

        :return: none
        """
        # cell demands energy to keep functions
        self.atp -= self.hunger

        # phase 1 is growth phase
        if self.phase is Phase.G1:
            if self.atp > COSTS[GROWTH]:
                self.atp -= COSTS[GROWTH]
                self.phase = Phase.S
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
        # phase 4 is to split, M-phase, inform colony!!!
        else:
            self.is_splitting = True
            self.phase = Phase.G1
            # restarting...

    def __split(self):
        """
        attempt to split the cell
        must have:
        - available ATP
        - enough saved hisidine
        - q-sensing says space is available

        :return:
        """
        pass

    def __age(self):
        pass




if __name__ == '__main__':
    cell = Cell(GeneManager(), UnitManager())
    print(cell)



