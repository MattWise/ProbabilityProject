from __future__ import division,print_function
from Functions import *
from types import *

"""
P is a dictionary of frozenset, dictionary pairs.
    The former is the sample space or a subset of it.
    The latter is a dictionary of frozenset, float pairs.
        The former is a simple event.
        The latter is the probability of its occurrence.

It may sometimes be desirable to use some other hashable for the keys of P or the keys of the values of P. Do not attempt set theoretic operations in these cases.

To get the probability of a given simple event E with event set S taken as the sample space, call P[S][E].
The over all sample space with accompanying event probabilities must be explicitly passed to P before any subset probabilities can be calculated.

Random Variables are implemented as functions of signature: float func(frozenset event) and are expected to be memoized with Functions.memodict.
"""

def memoizeGetSubset(getSubset):
    #If the naming convention is not clear enough, this should not be used with anything except getSubset.
    #Using an id of a mutable type as a key is unsafe in general, and only tremendous performance gains make it worth the risk here.
    cache={}
    def memoizedGetSubset(self,inEvent):
        key=id(inEvent)
        if key in cache:
            return cache[key]
        else:
            ret=getSubset(self, inEvent)
            cache[key]=ret
            return ret
    return memoizedGetSubset

class P(dict):

    def __init__(self, inpt, **kwargs):
        #inpt must be a list or tuple of form: (frozenset sampleSpace,dict probabilities)
        assert len(inpt)==2
        assert type(inpt[1]) is DictType
        super(P,self).__init__(**kwargs)
        self[inpt[0]]=inpt[1]
        self.SimpleEvents=inpt[1].keys()
        self.SampleSpace=inpt[0]
        self.Weights={self.SampleSpace:1.}

    def verifySampleSpace(self):
        #Debugging function.
        for key in self.keys():
            if not self.SampleSpace.issuperset(key):
                raise ValueError("Keys of P not subsets of sample space.")

    def __missing__(self,key):
        #Recall, key should be a hashable collection of hashable collections representing simple events.
        if not frozenset(key).issubset(frozenset(self.SampleSpace)):
            raise ValueError("Key not subset of sample space")
        else:
            return self.__addSubset(key)

    def __addSubset(self, subset):
        #For internal use. No verification.
        weight=sum((self[self.SampleSpace][event] for event in subset))
        self.Weights[subset]=weight
        probabilities={}
        for event in subset:
            probabilities[event]= self[self.SampleSpace][event] / weight
        self[subset]=probabilities
        return self[subset]

    @memoizeGetSubset
    def getSubset(self,inEvent):
        #inEvent is a function of signature bool inEvent(frozenset simpleEvent) which, given a simple event, returns whether that event is a member of the compound event.
        #Returns the subset of the sample space for which inEvent is true, representing a compound event.
        #Cheated to memioze this. Treat inEvent as an immutable, or else.
        #Must be a class function becuases memoization is only valid for the same sample space.
        return frozenset(it.ifilter(inEvent,self.SimpleEvents))

    def probabilityOfCompoundEvent(self,subset):
        #inEvent is a function of signature bool inEvent(frozenset simpleEvent) which, given a simple event, returns whether that event is a member of the compound event.
        #Returns probability of the compound event represented by the set of simple events "subset".
        #Memiozed, of course.
        self[subset] #Ensures subset in P
        assert subset in self
        return self.Weights[subset]