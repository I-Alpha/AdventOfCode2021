from matplotlib.pyplot import table
import numpy as np
from pyparsing import line


data = list(map(lambda x: list(map(lambda y: int(y), x.split(","))),
            open("day_07/input.txt", "r")))[0]
