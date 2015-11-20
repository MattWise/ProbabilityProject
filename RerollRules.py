from __future__ import division,print_function
from Functions import *

"""
Functions that should:
    be of signature tuple rerollRule(list roll).
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
    return tuple(values)

def chance(roll):
    return tuple((value for value in roll if value<4))

def smallStraight(roll):

    def helper(a,b,c):
        #if a, b and c in roll, discards c
        if a in keeplst and b in keeplst and c in keeplst:
            keeplst.remove(c)

    def helper2(a,b):
        #if a and b in roll, discards b
        if a not in keeplst and b in keeplst:
            keeplst.remove(b)

    def invertList(sample,lst):
        invertedlst=[]
        for value in lst:


    keeplst=roll[:]
    helper(1,2,5)
    helper2(2,1)
    helper(6,5,2)
    helper2(5,6)
    helper(2,5,1)
    helper(2,5,6)

    list(set(keeplst))
    rerollList=[]



    return tuple(rerollList)