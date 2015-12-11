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
    return categoryXOfAKind(3, roll)

def fourOfAKind(roll):
    return categoryXOfAKind(4, roll)

def yahtzee(roll):
    return categoryXOfAKind(5, roll)

def chance(roll):
    return True

def fullHouse(roll):
    for value,occurences in RollHash(roll):
        if occurences==2:
            return categoryXOfAKind(3, roll)
    return False

def smallStraight(roll):
    if 3 in roll and 4 in roll:
        if 2 in roll:
            if 1 in roll or 5 in roll:
                return True
        elif 5 in roll and 6 in roll:
            return True
    return False

def largeStraight(roll):
    if 2 in roll and 3 in roll and 4 in roll and 5 in roll:
        if 1 in roll or 6 in roll:
            return True
    return False

def aces(roll):
    return 1 in roll
def twos(roll):
    return 2 in roll
def threes(roll):
    return 3 in roll
def fours(roll):
    return 4 in roll
def fives(roll):
    return 5 in roll
def sixes(roll):
    return 6 in roll