from __future__ import division,print_function
from Functions import *
import CategoryRules

"""
Functions that should:
    be of signature int scoringRule(list roll).
    take a list of five values representing a dice roll and return the associated score.
    be named for the category they are score. Names should be precisely what's on the score card in camelCase.
    use respective CategoryRule to determine if category condition is met.


No other functions are allowed in this file. Put any helpers in Functions.py
"""

#TODO: Unhashing decorator to make these work with hashed rolls.

def chance(roll):
    if CategoryRules.chance(roll):
        return sum(roll)
    else:
        return 0