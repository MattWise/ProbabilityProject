from __future__ import division,print_function
import numpy as np,itertools as it
from collections import Counter
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




