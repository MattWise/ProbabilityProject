from __future__ import division,print_function
import random as r,numpy as np,itertools as it
from Functions import *
from Probability import *
from types import *

"""
Functions related to rolling dice
"""

@memoizeAllRolls
def allRolls(sides=6, dice=5):

    keys=tuple((tuple(i) for i in it.product(range(1,sides+1), repeat=dice)))
    assert len(keys)==sides**dice
    prob=1/(sides**dice)

    rollProbs={key:prob for key in keys}
    pRolls= P(rollProbs)
    events=frozenset((hashList(roll) for roll in keys))
    eventProbs={}
    for event in events:
        prob=pRolls.probabilityOfCompoundEvent(getSubset(pRolls.SampleSpace,lambda lst:hashList(lst)==event))
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

"""
def reroll(rollHash,rerollRule,Set):
    #Takes rollHash, rerollRule, and a sample space and returns the subset of the sample space that fits the reroll rule.
    valuesToReroll=rerollRule(rollHash)
    inEvent=getRerollInEvent(rollHash,values)
    return getSubset(Set,inEvent)
"""

@memodict2
def rerollHelper(size,valuesToKeep):
    subP=allRolls(6,size)
    probDict=defDict(0)
    for subHash,probability in subP[subP.SampleSpace].iteritems():
        probDict[addHashes(valuesToKeep,subHash)]=probability
    return probDict

def reroll(rollHash,rerollRule,p):
    rollList=unHashList(unHashDict(rollHash))
    valuesToKeep=hashList(getTheRest(rollList,rerollRule(rollHash)))
    size=len(rollList)-len(unHashList(unHashDict(valuesToKeep)))
    if size>0:
        return rerollHelper(size,valuesToKeep)
    else:
        return p[p.SampleSpace]


def calculateOutcomes(rerollRule,p,rerolls=2):
    #Takes the rerollRule and the number of rerolls desired
    #Returns a dictionary {finalRollValue:probability(finalRollValue) for finalRollValue in allPossibleRolls}
    s=p.SampleSpace
    ps=[p]#contains at index i the P object for roll values after i rerolls
    for r in range(rerolls):
        p0=ps[-1]
        #Prob(i)=sum((prob(k)*prob(i|k) for k in s)
        probDict={}
        for i in s:
            tot=0.
            for k in s:
                pk=p0[s][k] #Probability of getting event k in the last roll
                #pi=p[reroll(k,rerollRule,s)][i] #Probability of i given k
                pi=reroll(k,rerollRule,p)[i]
                tot+=pk*pi
            probDict[i]=tot
        ps.append(P(probDict))

    return ps[-1][s]

def calculateOutcomesRandom(rerollRule,rerolls=2,times=10000):
    probdict=defDict(0)
    for time in range(times):
        roll=[r.randint(1,6) for _ in range(5)]
        for _ in range(rerolls):
            valuesToRemove=rerollRule(hashList(roll))
            for value in valuesToRemove:
                roll.remove(value)
            for i in range(len(valuesToRemove)):
                roll.append(r.randint(1,6))
        probdict[hashList(roll)]+=1
    weight=sum((probdict[event] for event in probdict.keys()))
    probdict.update(((key,value/weight) for key,value in probdict.items()))
    return probdict

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