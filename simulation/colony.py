class Colony:

    def __init__(self, init_sz, model=None):
        """
        build a colony of init_sz,
        if model is not specified

        :param init_sz:
        :param model: if random is not wanted, have a cell model...
        """
        self.cells = []

    def cycle_cells(self):
        """
        cycle through all cells in this colony
        and perform cycle calls, update data based
        on resulting cycle calls
        :return:
        """
        pass