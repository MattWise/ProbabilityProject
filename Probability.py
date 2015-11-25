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

class P(dict):

    def __init__(self, probDict, **kwargs):
        #inpt must be a list or tuple of form: (frozenset sampleSpace,dict(0) probabilities)
        assert isinstance(probDict,DictType)
        super(P,self).__init__(**kwargs)
        self.SampleSpace=frozenset(probDict.keys())
        self[self.SampleSpace]=probDict
        self.Weights={self.SampleSpace:1.}

    def verifySampleSpace(self):
        #Debugging function.
        for key in self.keys():
            if not self.SampleSpace.issuperset(key):
                raise ValueError("Keys of P not subsets of sample space.")

    def __missing__(self,key):
        #Recall, key should be a hashable collection of hashable collections representing simple events.
        if not frozenset((frozenset(item) for item in key)).issubset(frozenset(frozenset(item) for item in self.SampleSpace)):
            print(frozenset(key))
            raise ValueError("Key not subset of sample space")
        else:
            return self.__addSubset(key)

    def __addSubset(self, subset):
        #For internal use. No verification.
        weight=sum((self[self.SampleSpace][event] for event in subset))
        self.Weights[subset]=weight
        probabilities=defDict()
        for simpleEvent in subset:
            probabilities[simpleEvent]=self[self.SampleSpace][simpleEvent]/weight
        self[subset]=probabilities
        #verifyNormalization(self,subset)
        return self[subset]

    def probabilityOfCompoundEvent(self,subset):
        #Returns probability of the compound event represented by the set of simple events "subset".
        #Memiozed, of course, via the dictionary behavior of P.
        self[subset] #Ensures subset in P
        assert subset in self
        return self.Weights[subset]