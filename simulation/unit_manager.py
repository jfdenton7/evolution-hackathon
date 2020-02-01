from simulation.gene import GeneManager
from random import choice, randrange
from simulation.config import BROKEN_GENE
from simulation.cell import Cell


class UnitManager:

    def __init__(self):
        pass

    def build_genome(self, num_genes, req: bool, gene_manager: GeneManager, cell: Cell) -> list:
        """

        :param num_genes:
        :param gene_manager:
        :param req:
        :param cell:
        :return:
        """
        genes = []
        for i in range(num_genes):
            # format: [(gene_code, performance), ...]
            gene, perf = gene_manager.generate_gene()
            if perf < BROKEN_GENE:
                if req:
                    cell.die()
                genes.append((gene, perf, False))
            else:
                genes.append((gene, perf, True))

        return genes

    def mutate_genome(self, gene_manager: GeneManager, genome: list):
        index = randrange(len(genome))

        code, perf, _ = genome[index]

        # mutate and re-calculate
        # form: gene, perf on return
        genome[index] = gene_manager.mutate(code)

    def effective_modifier(self, genome):
        """
        given a genome, calculate the
        effective modifier on the input
        :param genome:
        :return:
        """
        modif = 0

        for gene in genome:
            _, perf, _ = gene
            modif += perf - 1

        return modif





