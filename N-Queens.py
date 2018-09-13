# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 15:01:43 2018

@author: Kan
"""
# permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
# permutations(range(3)) --> 012 021 102 120 201 210

# combinations('ABCD', 2) --> AB AC AD BC BD CD
# combinations(range(4), 3) --> 012 013 023 123

import itertools as it

def is_solution(perm):
    for (i1, i2) in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False
    return True

for perm in it.permutations(range(3)):
    print (perm)
    if is_solution(perm):
        print(perm)

        
#def combinations(iterable, r):
#    """
#    >>> combinations('ABCD', 2)
#    >>> AB AC AD BC BD CD
#    >>> combinations(range(4), 3)
#    >>> 012 013 023 123
#    """
#    pool = tuple(iterable)
#    n = len(pool)
#    
#    if r > n:
#        return
#    
#    indices = list(range(r))
#    yield tuple(pool[i] for i in indices)
#    while True:
#        for i in reversed(range(r)):
#            if indices[i] != i + n - r:
#                break
#        else:
#            return
#        
#        indices[i] += 1
#        for j in range(i + 1, r):
#            indices[j] = indices[j - 1] + 1
#        yield tuple(pool[i] for i in indices)