from __future__ import division,print_function
import random as r,numpy as np,itertools as it
from collections import Counter

sides=[1,2,3,4,5,6]
a=it.product(sides,repeat=3)
for i in a:
    print(i)
