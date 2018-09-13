# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 22:43:40 2018

@author: Kan
"""

#    Given a list of values inputs and a positive integer n, 
#    write a function that splits inputs into groups of length n. 
#    For simplicity, assume that the length of the input list is divisible by n. 
#    For example, if inputs = [1, 2, 3, 4, 5, 6] and n = 2, 
#    your function should return [(1, 2), (3, 4), (5, 6)].

def naive_grouper(inputs, n):
    """
    >>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> naive_grouper(nums, 2)
    [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
    """
    num_groups = len(inputs) // n
    return [tuple(inputs[i * n:(i + 1) * n]) for i in range(num_groups)]

#for _ in naive_grouper(range(100000000), 10):
#    pass
    
def better_grouper(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters)

"""
>>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> iters = [iter(nums)] * 2
>>> list(id(itr) for itr in iters) #IDs are the same
"""
bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

"""
    >>> list(it.combinations(bills, 3))
    [(20, 20, 20), (20, 20, 10), (20, 20, 10), ... ]
    A choice of k things form a set of n things called a combination, and itertools
    has your back here. The itertools.combinations() function take two arguments
    an iterable inputs and a positive integer n - and produces an iterator over tuples
    of all combinations of n elements inputs
"""
makes_100 = []
import itertools as it
for n in range(1, len(bills) + 1):
    for combination in it.combinations(bills, n):
        if sum(combination) == 100:
            makes_100.append(combination)

"""            
If you print out makes_100, you will notice there are 
a lot of repeated combinations. This makes sense because 
you can make change for $100 with three $20 dollar bills and four $10 bills, 
but combinations() does this with the first four $10 dollars bills 
in your wallet; the first, third, fourth and fifth $10 dollar bills; 
the first, second, fourth and fifth $10 bills; and so on.
To remove duplicates from makes_100, you can convert it to a set:
>>> set(makes_100)
{(20, 20, 10, 10, 10, 10, 10, 5, 1, 1, 1, 1, 1),
 (20, 20, 10, 10, 10, 10, 10, 5, 5),
 (20, 20, 20, 10, 10, 10, 5, 1, 1, 1, 1, 1),
 (20, 20, 20, 10, 10, 10, 5, 5),
 (20, 20, 20, 10, 10, 10, 10)}

"""

"""-----------------------------------------------------
Here’s a variation on the same problem:

How many ways are there to make change for a $100 bill 
using any number of $50, $20, $10, $5, and $1 dollar bills?

--------------------------------------------------------"""

# Recursive

#LD = (50, 20, 10, 5, 1)
#
#def rChange_money(n, m, i = 0):
#    if n - m < 0:
#        return 0
#    if n == 0:
#        return 1
#    if m <= 0:
#        return 0
#    else:
#        return rChange_money(LD[i] - n, LD[i], i) + rChange_money(n - LD[i], LD[i + 1], i + 1)

"""----------------------------------------------------------------------------
#    itertools.combinations Example
#    combinations(iterable, n)
#    
#    Return successive n-length combinations of elements in the iterable.
#    
#    >>> combinations([1, 2, 3], 2)
#    (1, 2), (1, 3), (2, 3)
#    itertools.combinations_with_replacement Example
#    combinations_with_replacement(iterable, n)
#    
#    Return successive n-length combinations of elements in the iterable allowing 
#    individual elements to have successive repeats.
#    
#    >>> combinations_with_replacement([1, 2], 2)
#    (1, 1), (1, 2), (2, 2)
#    itertools.permutations Example
#    permutations(iterable, n=None)
#    
#    Return successive n-length permutations of elements in the iterable.
#    
#    >>> permutations('abc')
#    ('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'),
#    ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')
----------------------------------------------------------------------------"""

def evens():
    """Generate even integers, starting with 0."""
    n = 0
    while True:
        yield n
        n += 2
        
evens = evens()

#list(next(evens) for _ in range(5))
def odds():
    n = 1
    while True:
        yield n
        n += 2


































