from __future__ import division,print_function
from Functions import *

"""
Functions that should:
    be of signature tuple rerollRule(list roll).
    take a list of five values representing a dice roll and return the values (not the indexes) to be rerolled.
    be named for the category they are optimized for. Names should be precisely what's on the score card in camelCase.

No other functions are allowed in this file. Put any helpers in Functions.py
"""

#Sort of forgot I already implemented this and implemented it again, better. Keeping this in case the other doesn't work.
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
"""
def chance(roll):
    return tuple((value for value in roll if value<4))

def smallStraight(roll):
    roll=roll[:] #Sets the name "roll" to point to a copy of the input rather than the input itself to prevent undesired mutation.
    rerollList=listDuplicates(roll)
    keepList=[3,4]

    if 2 in roll and 5 in roll:
        keepList.append(2)
        keepList.append(5)
    if 1 in roll and 2 in roll:
        keepList.append(2)
        keepList.append(1)
    if not 1 in roll and not 2 in roll:
        keepList.append(5)
    if 5 in roll and 6 in roll:
        keepList.append(5)
        keepList.append(6)
    if not 5 in roll and not 6 in roll:
        keepList.append(2)

    for value in removeDuplicates(roll):
        if not value in keepList:
            rerollList.append(value)

    return tuple(rerollList)

def largeStraight(roll):
    rerollList=listDuplicates(roll)
    if 1 in roll and 6 in roll:
        rerollList.append(6)
    return rerollList

def fullHouse(roll):
    numberOfEach=getNumberOfEach(roll)
    if len(numberOfEach[2])==2:
        return tuple(numberOfEach[1])
    elif len(numberOfEach[2])==1:
        if len(numberOfEach[3])==1:
            return ()
        else:
            return tuple(roll)
    elif len(numberOfEach[3])==1:
        return (numberOfEach[1][0],)
    elif len(numberOfEach[4])==1:
        return (numberOfEach[4][0],)
    elif len(numberOfEach[5])==1:
        r=numberOfEach[5][0]
        return (r,r)
    else:
        return tuple(roll)

threeOfAKind=fourOfAKind=yahtzee=rerollXOfAKind

def aces(roll):
    return rerollSingles(1, roll)
def twos(roll):
    return rerollSingles(2, roll)
def threes(roll):
    return rerollSingles(3, roll)
def fours(roll):
    return rerollSingles(4, roll)
def fives(roll):
    return rerollSingles(5, roll)
def sixes(roll):
    return rerollSingles(6, roll)