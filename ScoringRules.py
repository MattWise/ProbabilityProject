from __future__ import division,print_function
from Functions import *

"""
Functions that should:
    be of signature int scoringRule(list roll).
    take a list of five values representing a dice roll and return the associated score.
    be named for the category they are score.
"""

def Chance(roll):
    return sum(roll)