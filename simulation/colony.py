from simulation.cell import Cell
from simulation.gene import GeneManager
from simulation.unit_manager import UnitManager


class Colony:

    def __init__(self, init_sz, id, gm: GeneManager, um: UnitManager, dish, pos, model=None, carc_lvl=0):
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
            life, split, modif = cell.cycle()
            if not life:
                self.cells.remove(cell)
            elif split:
                self.cells.append(Cell(self.gm, self.um, self.carc))

    def __init_colony(self, sz, gm, um, carc):
        for i in range(sz):
            self.cells.append(Cell(gm, um, carc))


if __name__ == '__main__':
    gm = GeneManager()
    um = UnitManager()

    col = Colony(1, 0, gm, um)

    col.cycle_cells()