from __future__ import division,print_function
import inspect
import cPickle as pickle
import ScoringRules,RerollRules,CategoryRules
from AllRolls import *
from Functions import *
from Probability import *
from AnalyzeRandomVariable import *
from types import *

categories=["aces","twos","threes","fours","fives","sixes","threeOfAKind","fourOfAKind","fullHouse","smallStraight","largeStraight","yahtzee","chance"]

def compileRules(modules=(RerollRules,ScoringRules,CategoryRules)):

    def getFuncs(module):
        return inspect.getmembers(module,inspect.isfunction)

    rr,sr,cr=tuple((getFuncs(module) for module in modules))
    Rules={rName:(rFunc,sFunc,cFunc) for rName,rFunc in rr for sName,sFunc in sr for cName,cFunc in cr if rName==sName==cName and rName in categories}
    for key in Rules.keys():
        Rules[key]=tuple((unHashDecorator(func) for func in Rules[key]))
    return Rules

Rules=compileRules()

def problem1():
    p=allRolls()
    print("\nProblem 1:\n")
    for name in categories:
        outcomes=calculateOutcomes(Rules[name][0],p)
        a=AnalyzeRandomVariable(Rules[name][2],outcomes)
        print("\n{}:".format(name))
        a.prnt()

def problem3(N=(0,1,2,3)):
    #expected value and variance of chance score in n rerolls.
    p=allRolls()
    print("\nProblem 3: Chance in n rerolls\n")
    for n in N:
        outcomes=calculateOutcomes(Rules["chance"][0],p,n)
        a=AnalyzeRandomVariable(Rules["chance"][1],outcomes)
        print("\n{} rerolls:".format(n))
        a.prnt()

def problem4(category="aces",rerolls=2):
    p=allRolls()
    print("\nProblem 4: Expected Value and Variance in score of {}\n".format(category))
    outcomes=calculateOutcomes(Rules[category][0],p,rerolls)
    a=AnalyzeRandomVariable(Rules[category][1],outcomes)
    a.prnt()

def problem5b(times=10000):
    p=allRolls()
    randomOutcomes=calculateOutcomesRandom(Rules["chance"][0],p,rerolls=0,times=times)
    outcomes=calculateOutcomes(Rules["chance"][0],p,0)
    a=AnalyzeRandomVariable(Rules["chance"][1],outcomes)
    randomA=AnalyzeRandomVariable(Rules["chance"][1],randomOutcomes)
    print("\nProblem 5b:\n")
    print("\nAnalytic:")
    a.prnt()
    print("\nRandom:")
    randomA.prnt()

def problem5c(category="aces",rerolls=2,times=10000):
    p=allRolls()
    print("\nProblem 5c: Expected Value and Variance in score of {}\n".format(category))
    outcomes=calculateOutcomes(Rules[category][0],p,rerolls)
    a=AnalyzeRandomVariable(Rules[category][1],outcomes)
    print("\nAnalytic:")
    a.prnt()
    randomOutcomes=calculateOutcomesRandom(Rules[category][0],p,rerolls,times)
    randomA=AnalyzeRandomVariable(Rules[category][1],randomOutcomes)
    print("\nRandom:")
    randomA.prnt()



problem1()
problem3()
problem4()
problem5b()
problem5c()