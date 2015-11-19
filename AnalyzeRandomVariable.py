from Functions import *
import math


class AnalyzeRandomVariable:
    """
    Takes:
        Function randomVariable: returns a number when operated on a simple event
        Dictionary probabilities: gives the probability for each simple event of form:
            probabilities[simpleEvent]=p(simpleEvent)

    Calculates the expected value, variance, and sigma for the random variable
    """
    def __init__(self,randomVariable,probabilities):
        self.randomVariable=randomVariable
        self.randomVariableSquared=squared(randomVariable)
        self.probabilities=probabilities
        self.expectedValue=self.getExpectedValue(self.values)
        self.variance=self.getVariance()
        self.sigma=math.sqrt(self.variance)

    def getValues(self,f):
        self.values=[]
        for key in self.probabilities.keys():
            self.values.append(self.probabilities[key]*f(key))

    def getExpectedValue(self,values):
        return sum(values)/len(values)

    def getVariance(self):
        expSquared=self.getExpectedValue(self.getValues(self.randomVariableSquared))
        return expSquared-(self.expectedValue)**2
