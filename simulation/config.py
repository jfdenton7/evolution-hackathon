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

# two possible sequences of the same length
#

# possible placeholder
HEAD_LEN = 10

GENE_LEN_STD = 10
GEN_LEN_DEV = 1

# gene count per Unit
# form (count,
HIST_GENE = 8, True

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
CYCLE_TIME = 1


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

ATP = 100
PHASE_START = 101
HUNGER = 102
CELL_SZ = 103

GROWTH = 104
DNA = 105


COSTS = {
    GROWTH: 20,
    DNA: 30
}

# Cell options
DEFAULT_START = {
    ATP: 50,
    PHASE_START: Phase.G1,
    HUNGER: 20,
    # cell size in mu_m
    CELL_SZ: 5

}









