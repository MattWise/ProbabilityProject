from __future__ import division,print_function

from Functions import *
import cmath as m


class AnalyzeRandomVariable:
    """
    Takes:
        Function randomVariable: returns a number when operated on a simple event
        Dictionary probabilities: gives the probability for each simple event of form:
            probabilities[simpleEvent]=probability(simpleEvent)

    Calculates the expected value, variance, and sigma for the random variable
    """
    def __init__(self,randomVariable,probabilities):
        self.randomVariable=randomVariable
        self.randomVariableSquared=squared(randomVariable)
        self.probabilities=probabilities
        self.values=self.getValues(self.randomVariable)
        self.expectedValue=self.getExpectedValue(self.values)
        self.variance=self.getVariance()
        self.sigma=m.sqrt(self.variance)

    def verify(self):
        #debugging function
        assert equalWithinTollerance(sum((self.probabilities[key] for key in self.probabilities.keys())), 1),sum(self.values)

    def getValues(self,f):
        values=[]
        for key in self.probabilities.keys():
            values.append(self.probabilities[key]*f(key))
        return values

    def getExpectedValue(self,values):
        return sum(values)

    def getVariance(self):
        expSquared=self.getExpectedValue(self.getValues(self.randomVariableSquared))
        return expSquared-(self.expectedValue)**2

    def prnt(self):
        print("\n{}:\n\nExpected Value: {}\nVariance: {}".format(self.randomVariable.__name__,self.expectedValue,self.variance))

