from __future__ import division,print_function
import random as r,numpy as np,itertools as it
from Functions import *
from Probability import *
from types import *

"""
Functions related to rolling dice
"""

def allRolls(sides=6, dice=5):
    def genInEvent(event):
        return lambda lst: hashList(lst) == event

    keys=tuple((tuple(i) for i in it.product(range(1,sides+1), repeat=dice)))
    prob=1/(dice ** sides)
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
    inEvent=getRerollInEvent(rollHash,values)
    return p.getSubset(inEvent)

def calculateOutcomes(rerollRule,p,rerolls=2):
    #Takes the rerollRule and the number of rerolls desired
    #Returns a dictionary {finalRollValue:probability(finalRollValue) for finalRollValue in allPossibleRolls}
    probDicts=[p[p.SampleSpace]]#contains at index i the probability dictionary for roll values after i rerolls
    for r in range(rerolls):
        probDict=defDict()
        for k in p.SimpleEvents:
            for i in p.SimpleEvents:
                probDict[k]+=p[reroll(i,rerollRule,p)][k] #With memoization, this isn't as bad as it appears.
        probDicts.append(probDict)
    return probDicts[-1]