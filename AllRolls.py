from __future__ import division,print_function
import random as r,numpy as np,itertools as it
from Functions import *
from Probability import *
from types import *

"""
Functions related to rolling dice
"""

def allRolls(sides=6, dice=5):

    keys=tuple((tuple(i) for i in it.product(range(1,sides+1), repeat=dice)))
    assert len(keys)==sides**dice
    prob=1/(sides**dice)

    rollProbs={key:prob for key in keys}
    pRolls= P(rollProbs)
    events=frozenset((hashList(roll) for roll in keys))
    eventProbs={}
    for event in events:
        prob=pRolls.probabilityOfCompoundEvent(pRolls.getSubset(lambda lst:hashList(lst)==event))
        eventProbs[event]=prob
    return P(eventProbs)

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
    values=rerollRule(rollHash)
    inEvent=getRerollInEvent(rollHash,values)
    return p.getSubset(inEvent)

def calculateOutcomes(rerollRule,p,rerolls=2): #TODO: K is not a partitioning. Redo math.
    #Takes the rerollRule and the number of rerolls desired
    #Returns a dictionary {finalRollValue:probability(finalRollValue) for finalRollValue in allPossibleRolls}
    s=p.SampleSpace
    ps=[p]#contains at index i the P object for roll values after i rerolls
    for r in range(rerolls):
        p0=ps[-1]
        #Prob(i)=sum((prob(k)*prob(i|k) for k in s)
        ps.append(P({i: sum((p0[s][k] * p0[reroll(i, rerollRule, p0)][i] for k in s)) for i in s}))
        verifyNormalizationP(ps[r+1],s)
    return ps[-1][s]

"""
Testing Functions
"""

def rerollTest():
    p=allRolls(3,2)
    roll=[1,3]
    rh=hashList(roll)
    rerollRule=lambda x:tuple((value for value in x if value<2))
    rerollRule=unHashDecorator(rerollRule)
    print(reroll(rh,rerollRule,p))

def calculateOutcomesTest():
    p=allRolls(3,2)
    rerollRule=lambda x:tuple((value for value in x if value<2))
    rerollRule=unHashDecorator(rerollRule)
    calculateOutcomes(rerollRule,p)

if __name__=="__main__":
    calculateOutcomesTest()