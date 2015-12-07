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

def chance(roll):
    return sum(roll)

def yahtzee(roll):
    return 50*CategoryRules.yahtzee(roll)

def fullHouse(roll):
    return 25*CategoryRules.fullHouse(roll)

def threeOfAKind(roll):
    if CategoryRules.threeOfAKind(roll):
        return sum(roll)
    else:
        return 0

def fourOfAKind(roll):
    if CategoryRules.fourOfAKind(roll):
        return sum(roll)
    else:
        return 0

def smallStraight(roll):
    return 30*CategoryRules.smallStraight(roll)

def largeStraight(roll):
    return 40*CategoryRules.largeStraight(roll)

def aces(roll):
    return scoringSingles(1, roll)
def twos(roll):
    return scoringSingles(2, roll)
def threes(roll):
    return scoringSingles(3, roll)
def fours(roll):
    return scoringSingles(4, roll)
def fives(roll):
    return scoringSingles(5, roll)
def sixes(roll):
    return scoringSingles(6, roll)

