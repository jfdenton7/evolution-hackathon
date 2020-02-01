import re
import math
import random as ran
from random import gauss, randrange
from simulation.config import *
from binarytree import tree


# each terminal will be between (8-16) constants,
# these represent base pairs building the gene

class GeneManager:
    """
    GeneManager
    will need to generate a base
    gene and perform a single mutation
    to the gene to set relative performance
    of this gene....

    linear based encoding, finds
    longest 'correct' set of an
    expression, determines
    remainder as in-active genetic code
    """

    def __init__(self):
        """
        GM manages cell encoding generator and
        performance calculation.

        Capable of mutating a past generated encoding
        """
        self.gene_enc = ""
        self.perf = 1
        self.functions = list(FUNCTIONS.keys())

    def mutate(self, encoding) -> (str, float):
        """
        given some encoding of a gene,
        mutate the gene sequence

        :param encoding: encoding of the gene
        this mutate event will incur
        :return: a newly encoded gene with performance
        """
        self.gene_enc = encoding

        ops, consts = self.__decode_gene()

        index = randrange(len(ops))

        op = ran.choice(self.functions)
        ops[index] = op

        if op is not EMPTY:
            const_str = self.__gen_const(op)
            consts[index] = const_str

        self.gene_enc = ""
        for op, const in zip(ops, consts):
            self.gene_enc += op + const

        self.__calc_gene()

        return self.gene_enc, self.perf

    def __gen_const(self, func):
        if func == ADD or func == MINUS:
            return str(abs(gauss(MU_P, SIG_P)))
        else:
            return str(abs(gauss(MU_M, SIG_M)))

    def generate_gene(self) -> (str, float):
        """
        generate gene encoding and relative performane score
        based on mean average of that gene
        *(will be between 0.0 - 1.0)

        :return: none
        """
        # reset
        self.gene_enc = ""
        self.perf = 0
        # Initially create an array of the encoding
        # perform bottom up calculation based on the
        # heap layout
        # finally, set gene representation as a string and remove
        # the array... (should be translatable...)
        gene_len = abs(int(gauss(GENE_LEN_STD, GEN_LEN_DEV)))

        # now generate random constants to influence gene
        # will be based on gaussian distribution between dev -10 and 10, mean 0
        # run through, select func, select const, repeat

        # generate encoding
        for i in range(gene_len):
            func = ran.choice(self.functions)
            if not func == EMPTY:
                self.gene_enc += func + self.__gen_const(func)
            else:
                self.gene_enc += func + str(0)

        self.__calc_gene()

        return self.gene_enc, self.perf

    def __calc_gene(self):
        """
        calculate performance of gene based on encoding

        :return:
        """

        consts = re.findall(r"\d+\.\d+|\d+", self.gene_enc)
        ops = re.findall(r'[abc_]', self.gene_enc)
        res = START

        # print(len(consts))
        # print(len(ops))

        for i in range(len(ops)):
            if ops[i] is EMPTY:
                continue
            res = FUNCTIONS[ops[i]](res, float(consts[i]))

        perf = res / START

        self.perf = perf

    def __decode_gene(self):
        """
        decode gene

        :return:
        """
        consts = re.findall(r"\d+\.\d+|\d+", self.gene_enc)
        ops = re.findall(r'[abc_]', self.gene_enc)

        return ops, consts


if __name__ == '__main__':
    gm = GeneManager()
    res = gm.generate_gene()
    print(res)
    res = gm.mutate(res[0])
    print(res)





