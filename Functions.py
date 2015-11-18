from __future__ import division,print_function
import random as r,numpy as np,itertools as it
from collections import Counter

def roll():
    return r.randint(1,6)

def rollFive():
    return [roll() for i in range(5)]

def getAllRolls(sides,length):
    return it.combinations_with_replacement(range(1,sides+1),length)


def reroll(lst,values):
    #value is a tuple of values you want to reroll
    for value in values:
        lst.remove(value)
        lst.apppend(roll())
    return lst

def isXeOfAKind(lst,x):
    count=Counter(lst)
    mode=count.most_common(1)
    if lst.count(mode)>=x:
        return True
