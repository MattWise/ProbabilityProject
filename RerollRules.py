from __future__ import division,print_function
from Functions import *

"""
Functions that should:
    be of signature list rerollRule(list roll).
    take a list of five values representing a dice roll and return the values (not the indexes) to be rerolled.
    be named for the category they are optimized for. Names should be precisely what's on the score card in camelCase.

No other functions are allowed in this file. Put any helpers in Functions.py
"""

def yahtzee(roll):
    #Yatzhee reroll rule. Keeps the ones you have most of and rerolls the rest.
    values=[]
    rollHash=hashList(roll)
    rolldict=unHashDict(rollHash)
    a=0
    keys=rolldict.keys()
    mode=None
    for key in keys:
        if rolldict[key]>a:
            a=rolldict[key]
            mode=key
    del rolldict[mode]
    values=unHashList(rolldict)
    return values

def chance(roll):
    return [value for value in roll if value<4]
