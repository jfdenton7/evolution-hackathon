from enum import Enum
from math import sqrt

# all genes encoded follow func:terminal:func:terminal....


class Phase(Enum):
    G1 = 0,
    G2 = 1,
    S = 2,
    M = 3

MULT = 'a'
ADD = 'b'
MINUS = 'c'
OP_SET = '[abc]'
EMPTY = '_'

TERMINALS = []
FUNCTIONS = {MULT: lambda a, b: a * b,
             ADD: lambda a, b: a + b,
             MINUS: lambda a, b: a - b,
             EMPTY: None}
# encoding follows pattern....
FRONT = 0
# two possible sequences of the same length
#

# possible placeholder
HEAD_LEN = 10

GENE_LEN_STD = 10
GEN_LEN_DEV = 1

# gene count per Unit
# form (count,
HIST_GENE = 8, True

# ======== CELL - INFO ========
# sugars
GLUC = 3, False
PENT = 4, False
FRUC = 3, False
AMLY = 4, False

G1_S = 1, True
G2_M = 1, True

CELL_CYCLE = 5, True

DNA_REP = 7, True

EXCRETE = 3, False
Q_SENSES = 9, False

# cycle time in milliseconds (may be set by user)

# ======== DISH - INFO ========
CYCLE_TIME = 1
DISH_RADI = 250
CIRC_SIDE = 30
DELTA = 5

# plus/minus
SIG_P = 0
MU_P = 0.25

# start value
START = 1

# DMGed CODE
BROKEN_GENE = 0.25

# multi
SIG_M = 0.025
MU_M = 1

# ======== CELL - START ========
ATP = 100
PHASE_START = 101
HUNGER = 102
CELL_SZ = 103
# ======== CELL - COSTS ========
GROWTH = 104
DNA = 105
HUNGER_GROWTH = 106
MAX_AGE = 107
SENSE_DIST = 108


# ======== MAPS ========
COSTS = {
    GROWTH: 20,
    DNA: 30,
    HUNGER_GROWTH: 5
}

# Cell options
DEFAULT_START = {
    ATP: 50,
    PHASE_START: Phase.G1,
    HUNGER: 10,
    # cell size in mu_m
    CELL_SZ: 5,
    MAX_AGE: 72,
    SENSE_DIST: 2 # changes based on performance in q-sense


}

# ======== FOOD ========
# food
PENTOSE = 'P'
GLUCOSE = 'G'
FRUCTOSE = 'F'
AMYLOSE = 'A'

# ======== FOOD MAP ========
# decrements by 10
BASE_FOOD_PROD = {
    GLUCOSE: 38,
    PENTOSE: 28,
    FRUCTOSE: 18,
    AMYLOSE: 8

}
BASE_FOOD_DISTR = {
    GLUCOSE: 10,
    PENTOSE: 10,
    FRUCTOSE: 10,
    AMYLOSE: 10
}

# ======== GENE MAP  ======== #


GENE_HIST = 'h'
GENE_GLUC = 'g'
GENE_PENT = 'p'
GENE_FRUC = 'f'
GENE_AMYL = 'a'
GENE_G1_S = '<'
GENE_G2_M = '>'
GENE_CELL = 'c'
GENE_DNA = 'd'
GENE_EXCR = 'e'
GENE_Q = 'q'






