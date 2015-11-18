from __future__ import division,print_function
import random as r,numpy as np,itertools as it
from Functions import *
from Probability import *
from types import *

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

    def reroll(self,rollHash,values):

        def getRerollInEvent(self,rolldict):
            def inEvent(simpleEvent):
                simpleEventDict=unHashDict(simpleEvent)
                for key in rolldict.keys():
                    if simpleEvent[key]<rolldict[key]:
                        return False
                return True
            return inEvent

        rolldict=unHashDict(rollHash)
        for value in values:
            rolldict[value]-=1
        inEvent=getRerollInEvent(self,rolldict)
        self.P.getSubset(inEvent)



        """
        #Takes a roll hash (that is hashList(roll)) and the values to reroll and returns a frozenset of the hashes of all possible reroll values
        roll=unHashList(rollHash)
        for value in values:
            roll.remove(value)
        roll=tuple(roll) #remove mutability worries

        newDiceRolls=it.product(range(1,self.sides+1),repeat=len(values))
        newRolls=(it.chain(roll,newDiceRoll) for newDiceRoll in newDiceRolls)
        return frozenset(hashList(newRoll) for newRoll in newRolls)
        """
