from __future__ import division,print_function
import functools
import numpy as np,itertools as it
import collections
import decorator
"""
File for small, general purpose classes and functions used by other modules.
"""

def memodict(f):
    """
    Stolen from http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/
    Memoization decorator for a function taking a single argument
    """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__

def memodict2(f):
    """
    Also stolen from http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/
    Slower than memodict for one argument, but allows mutiple arguments.
    """
    class memodict(dict):
        def __getitem__(self, *key):
            return dict.__getitem__(self, key)

        def __missing__(self, key):
            ret = self[key] = f(*key)
            return ret

    return memodict().__getitem__


class defDict(dict):
    #dictionary with a default value. When __getitem__ is called on a key not in the dictionary, the value is set to default value and returned.
    def __init__(self,default=0,**kwargs):
        super(defDict,self).__init__(**kwargs)
        self.default=default

    def __missing__(self,key):
        self[key]=self.default
        return self.default

def squared(func):
    def squaredFunc(x):
        return func(x)**2
    return squaredFunc
"""
Not actually a hash, of course. These functions merely convert an ordered list with repeats into a hashable, unordered set that retains information on repeats.
The dictionary intermediates contain the same information, but are mutable, and thus nonhashable.
"""


def hashList(lst):
    #returns frozenset of tuples of form (value, # of occurrences).
    dct=defDict(0)
    for element in lst:
        dct[element]+=1
    return hashDict(dct)

def hashDict(dct):
    ret=[]
    for key in sorted(dct.keys()):
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

def xOfAKind(x,roll):
    rolldict=unHashDict(hashList(roll))
    for key in rolldict.keys():
        if rolldict[key]>=x:
            return True
    return False

def unHashDecorator(rule):
    def hashCompatibleRule(hash):
        return rule(unHashList(unHashDict(hash)))
    hashCompatibleRule.__name__=rule.__name__
    return hashCompatibleRule

#Debugging Functions

def verifyNormalizationP(p, subset):
    probDict=p[subset]
    return verifyNormalizationProbDict(probDict)

def verifyNormalizationProbDict(probdict):
    a=sum(probdict[key] for key in probdict.keys())
    assert equalWithinTollerance(a, 1.), "total p = {}".format(a)

def equalWithinTollerance(a, b):
    return abs(a-b)<10^-5

def testHash(lst):
    hsh=hashList(lst)
    listsToHash=[]
    for i in np.arange(100):
        a=r.randint(0,len(lst)-1)
        b=r.randint(0,len(lst)-1)
        lst[a],lst[b]=lst[b],lst[a]
        listsToHash.append(lst[:])
    hshs=[hashList(L) for L in listsToHash]
    for h in hshs:
        assert h==hsh,"{}!={}".format(h,hshs)