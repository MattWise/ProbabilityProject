from __future__ import division,print_function
import itertools as it,math as m,numpy as np
from AllRolls import *
from Functions import *
import ScoringRules


"""
Spare code and test functions.
"""

"""
P(final)=p(roll)*p(reroll|roll)*p(final|reroll)

probability of getting a specific event in 0 rerolls is p[p.SampleSpace][event]
probability of getting a specific event in 1 reroll is sum(prob(getting event from i)*prob(getting i) in 0 rerolls) for all i
sum([prob(getting event from i)*prob(i) for i in ps[]])
"""

p=allRolls(sides=4,dice=3)
#print(len(p.SampleSpace))
def verifyNormalization(subset):
    print(sum(p[subset][key] for key in p[subset].keys()))
    assert (sum(p[subset][key] for key in p[subset].keys()))==1.

sides=4
dice=3
keys=tuple((tuple(i) for i in it.product(range(1,sides+1), repeat=dice)))
print(keys)

verifyNormalization(p.SampleSpace)