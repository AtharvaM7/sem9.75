"""
Create a function that populates a list L with 0s and 1s with probability p and
1-p respectively and returns L. p is a parameter of the function.
"""

import random

def populate(p):
    L = []
    for i in range(1000000):
        L.append(random.choice([0, 1], p=[p, 1-p]))
    return L

def sample(L, k):
    """Samples k elements from L with repetition allowed.
    L is guaranteed to have only 0s and 1s.
    Output the proportion of 0s in the sample.
    """
    sample = random.choices(L, k=k)
    return sample.count(0)/k

