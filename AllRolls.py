from __future__ import division,print_function
import random as r,numpy as np,itertools as it
from Functions import *
from Probability import *
from types import *

"""
Functions related to rolling dice
"""

def allRolls(sides=6,length=5):
    def genInEvent(event):
        return lambda lst: hashList(lst) == event

    keys=tuple((tuple(i) for i in it.product(range(1,sides+1),repeat=length)))
    prob=1/(length**sides)
    rollProbs={key:prob for key in keys}
    pRolls=P((keys,rollProbs))
    events=frozenset(hashList(roll) for roll in keys)
    eventProbs={}
    for event in events:
        inEvent=genInEvent(event)
        prob=pRolls.probabilityOfCompoundEvent(pRolls.getSubset(inEvent))
        eventProbs[event]=prob
    return P((events,eventProbs))

@memodict2 #Memoization here ensures identically same function returned, which allows memoization of P.getSubset. This is why rollHash and values are used rather than roll and rerollRule.
def getRerollInEvent(rollHash,values):

    def getRolldict(rollHash, values):
        rolldict=unHashDict(rollHash)
        for value in values:
            rolldict[value]-=1
        return rolldict

    rolldict=getRolldict(rollHash,values)

    def inEvent(simpleEvent):
        simpleEventDict=unHashDict(simpleEvent)
        for key in rolldict.keys():
            if simpleEventDict[key]<rolldict[key]:
                return False
        return True
    return inEvent

def reroll(rollHash,rerollRule,p):
    #Takes rollHash, rerollRule, and P for sample space and returns the subset of the sample space that fits the reroll rule.
    values=rerollRule(unHashList(unHashDict(rollHash)))

if __name__=="__main__":
    R=AllRolls(sides=6,length=5)
    print(len(R.P.keys()[0]))