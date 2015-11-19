from __future__ import division,print_function
from Functions import *

"""
Functions that should:
    be of signature bool categoryRule(list roll).
    take a list of five values representing a dice roll and return whether the category is met.
    be named for the category they determine. Names should be precisely what's on the score card in camelCase.

No other functions are allowed in this file. Put any helpers in Functions.py
"""

def threeOfAKind(roll):
    return xOfAKind(3,roll)

def fourOfAKind(roll):
    return xOfAKind(4,roll)

def yahtzee(roll):
    return xOfAKind(5,roll)

def chance(roll):
    print(roll)
    return sum(roll)>0