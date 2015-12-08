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

def problem1():
    p=allRolls()
    print("\nProblem 1:\n")
    for name in Rules.keys():
        outcomes=calculateOutcomes(Rules[name][0],p)
        a=AnalyzeRandomVariable(Rules[name][2],outcomes)
        print("\n{}:".format(name))
        a.prnt()

def problem3(n):
    #expected value and variance of chance score in n rerolls.
    p=allRolls()
    outcomes=calculateOutcomes(Rules["chance"][0],p,n)
    a=AnalyzeRandomVariable(Rules["chance"][1],outcomes)
    print("\nProblem 3: {} rerolls".format(n))
    a.prnt()

def problem5b():
    p=allRolls()
    outcomes=calculateOutcomesRandom(Rules["chance"][0],p,rerolls=0)
    a=AnalyzeRandomVariable(Rules["chance"][1],outcomes)
    print("\nProblem 5b:")
    a.prnt()

problem1()