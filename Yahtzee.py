from __future__ import division,print_function
import inspect
import ScoringRules,RerollRules,CategoryRules
from AllRolls import *
from Functions import *
from Probability import *
from AnalyzeRandomVariable import *
from types import *

def compileRules(modules=(RerollRules,ScoringRules,CategoryRules)):

    def getFuncs(module):
        return inspect.getmembers(module,inspect.isfunction)

    rr,sr,cr=tuple((getFuncs(module) for module in modules))
    Rules={rName:(rFunc,sFunc,cFunc) for rName,rFunc in rr for sName,sFunc in sr for cName,cFunc in cr if rName==sName==cName}
    for key in Rules.keys():
        Rules[key]=tuple((unHashDecorator(func) for func in Rules[key]))
    return Rules

Rules=compileRules()

class Yahtzee:

    def __init__(self,sides=6,dice=5):
        self.sides=sides
        self.dice=dice
        self.p=allRolls(sides,dice)


def problem3(n):
    #expected value and variance of chance score in n rerolls.
    y=Yahtzee()
    outcomes=calculateOutcomes(Rules["chance"][0],y.p,n)
    a=AnalyzeRandomVariable(Rules["chance"][1],outcomes)
    print("\nProblem 3: {} rerolls".format(n))
    a.prnt()

problem3(0)