from simulation.gene import GeneManager
from random import choice, randrange
from simulation.config import BROKEN_GENE


class UnitManager:

    def __init__(self):
        pass

    def build_genome(self, num_genes, req: bool, gene_manager: GeneManager) -> list:
        """

        :param num_genes:
        :param gene_manager:
        :param req:
        :return:
        """
        genes = []
        for i in range(num_genes):
            # format: [(gene_code, performance), ...]
            gene, perf = gene_manager.generate_gene()
            if perf < BROKEN_GENE:
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





