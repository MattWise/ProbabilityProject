from __future__ import division,print_function
import itertools as it,math as m,numpy as np,random as r
from AllRolls import *
from Functions import *
import ScoringRules


"""
Spare code and test functions.
"""

"""
p=allRolls(sides=2,dice=2)
"""


"""
sides=4
dice=3
keys=tuple((tuple(i) for i in it.product(range(1,sides+1), repeat=dice)))
print(keys)
print(len(keys))
print(sides**dice)
"""

calculateOutcomesTest()