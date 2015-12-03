from __future__ import division,print_function
import functools
import numpy as np,itertools as it
import collections
import decorator
"""
File for small, general purpose classes and functions used by other modules.
"""

"""
Decorators
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

def memoizeGetSubset(getSubset):
    """
    getSubset is O(len(sampleSpace)), which is potentially very large.
    Further, the only easy way to cut down on calls to getSubset is memoization.
    inEvent functions are generally going to be generated dynamically from data P can't access, so the only place to memoize is here.
    Therefore, the performance gains from memoizing getSubset are potentially huge in an already unweildy algoritm.

    I had to cheat to get this to work. A lot.
    Functions are not hashable types, but integer IDs are.
    However, python reuses IDs when the associated object is garbage collected.
    My options are to either put the onus of generating unique IDs on the library user, or prevent garbage collection of the inEvent functions.
    I chose the latter.

    Warning:
        Do not use with any other function.
        This function is a memory leak: inEvent functions are never garbage collected.
    """
    cache={}
    doNotGarbageCollect=[]
    def memoizedGetSubset(set,inEvent):
        key=(set,id(inEvent))
        doNotGarbageCollect.append(inEvent)
        if key in cache:
            return cache[key]
        else:
            ret=getSubset(set, inEvent)
            cache[key]=ret
            return ret
    return memoizedGetSubset

def squared(func):
    def squaredFunc(x):
        return func(x)**2
    return squaredFunc

def unHashDecorator(rule):
    #For application to the functions in CategoryRules, RerollRules, and Scoring Rules. Allows them to keep the roll-as-list input while allowing them to be called using hashes.
    def hashCompatibleRule(hash):
        return rule(unHashList(unHashDict(hash)))
    hashCompatibleRule.__name__=rule.__name__
    return hashCompatibleRule

class defDict(dict):
    #dictionary with a default value. When __getitem__ is called on a key not in the dictionary, the value is set to default value and returned.
    def __init__(self,default=0,**kwargs):
        super(defDict,self).__init__(**kwargs)
        self.default=default

    def __missing__(self,key):
        self[key]=self.default
        return self.default

"""
Functions relating to manipulating sets.
"""

@memoizeGetSubset
def getSubset(Set,inEvent):
    #inEvent is a function of signature bool inEvent(frozenset simpleEvent) which, given a simple event, returns whether that event is a member of the compound event.
    #Returns the subset of the sample space for which inEvent is true, representing a compound event.
    #Cheated to memioze this. Treat inEvent as an immutable, or else.
    #Must be a class function becuases memoization is only valid for the same sample space.
    return frozenset(event for event in Set if inEvent(event))

"""
Functions relating to roll hashing and unhashing.

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

"""
Helper functions for the rules, since the only functions allowed in those files are the rules themselves.
"""

def xOfAKind(x,roll):
    rolldict=unHashDict(hashList(roll))
    for key in rolldict.keys():
        if rolldict[key]>=x:
            return True
    return False

def singles(x,roll):
    keepList = []
    rerollList = []

    for i in roll:
        if i == x:
            keepList.append(i)
        else:
            rerollList.append(i)

    return tuple(rerollList)

"""
Debugging Functions
"""

def verifyNormalizationP(p, subset):
    probDict=p[subset]
    return verifyNormalizationProbDict(probDict)

def verifyNormalizationProbDict(probdict):
    a=sum(probdict[key] for key in probdict.keys())
    assert equalWithinTollerance(a, 1.), "total p = {}".format(a)

def equalWithinTollerance(a, b):
    #For checking floating point numbers
    return abs(a-b)<(10**-5)

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