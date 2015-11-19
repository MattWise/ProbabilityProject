from __future__ import division,print_function
import itertools as it,math as m,numpy as np
from AllRolls import *
from Functions import *
import ScoringRules


"""
Spare code and test functions.
"""

"""
P(final)=p(roll)*p(reroll|roll)*p(final|reroll)

probability of getting a specific event in 0 rerolls is p[p.SampleSpace][event]
probability of getting a specific event in 1 reroll is sum(prob(getting event from i)*prob(getting i) in 0 rerolls) for all i
sum([prob(getting event from i)*prob(i) for i in ps[]])
"""

sides=[1,2,3,4,5,6]
a=it.product(sides,repeat=3)
for i in a:
    print(i)

class AllRolls:

    def __init__(self,sides=6,length=5):
        self.sides=sides
        self.length=length
        self.P=self.genRolls()

    def genRolls(self):
        #returns P object for genHash(roll) for roll in allPossibleRolls.

        def genInEvent(event):
            return lambda lst: hashList(lst) == event

        keys=tuple((tuple(i) for i in it.product(range(1,self.sides+1),repeat=self.length)))
        prob=1/(self.length**self.sides)
        rollProbs={key:prob for key in keys}
        pRolls=P((keys,rollProbs))
        events=frozenset(hashList(roll) for roll in keys)
        eventProbs={}
        for event in events:
            inEvent=genInEvent(event)
            prob=pRolls.probabilityOfCompoundEvent(pRolls.getSubset(inEvent))
            eventProbs[event]=prob
        return P((events,eventProbs))

    def calculateOutcomes(rerollRule,rerolls=2):
    #Takes the rerollRule and the number of rerolls desired
    #Returns a dictionary {finalRollValue:probability(finalRollValue) for finalRollValue in allPossibleRolls}
    p=allRolls()
    probDicts=[p[p.SampleSpace]]#contains at index i the probability dictionary for roll values after i rerolls
    for r in range(rerolls):
        probDict=defDict()
        for k in p.SimpleEvents:
            for i in p.SimpleEvents:
                probDict[k]+=p[reroll(i,rerollRule,p)][k] #With memoization, this isn't as bad as it appears.
        probDicts.append(probDict)
    return probDicts[-1]