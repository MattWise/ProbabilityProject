from __future__ import division,print_function
import numpy as np,itertools as it
from collections import Counter

def memodict(f):#Stolen from http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__

class defDict(dict):

    def __init__(self,default=0,seq=0,**kwargs):
        super(defDict,self).__init__(seq,**kwargs)
        self.default=default

    def __getitem__(self, item):
        if item in self:
            return self[item]
        else:
            self[item]=self.default
            return self.default

"""
class AllRolls:

    def __init__(self,sides=6,length=5):
        self.sides=sides
        self.length=length
        self.AllPossibleRolls=self.getAllRolls()

    def getAllRolls(self):
        return list(it.product(range(1,self.sides+1),repeat=self.length))

    def reroll(self,lst,values):
        f

    def isXeOfAKind(self,lst,x):
        count=Counter(lst)
        mode=count.most_common(1)
        if lst.count(mode)>=x:
            return True

    def isSameRoll(lst1,lst2):

"""
def hashList(lst):
    #returns frozenset of tuples of form (value, # of occurrences).
    dct=defDict(0)
    for element in lst:
        dct[element]+=1
    return hashDict(dct)

def hashDict(dct):
    ret=[]
    for key in dct.keys():
        ret.append((key,dct[key]))
    return frozenset(ret)

def unHashDict(dctHash):
    dct=defDict(0)
    for (value,occurences) in dctHash:
        dct[value]=occurences
    return dct

def unHashList(dct):
    #Inverse of hashList. Order is lost.
    lst=[]
    for value in dct.keys():
        for occurrence in range(dct[value]):
            lst.append(value)
    return lst




