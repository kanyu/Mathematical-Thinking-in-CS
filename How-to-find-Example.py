# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 23:32:24 2018

@author: Kan
"""
from math import ceil, floor

# find numbers in 100000 - 100999 which is a multiple of 9127 
def find1(start, end, div):
    """
    Run 1000 times
    """
    for i in range(start,end + 1):
        if i % div == 0:
            print(i)


#find1(100000, 100999, 9127)

def find2(start, end, div):
    """
    Run fewer times
    """        
    for i in range(floor(start / div), ceil(end / div) + 1):
        if (i * div >= start) and (i * div <= end):
            print(i * div)
        
#find2(100000, 100999, 9127)        

#    There exists a three-digit number N that produces remainder 1 when divided by
#    2, 3, 4, 5, 6, 7
#    [x for x in range(0,1000) if for x % y[i] in [2, 3, 4, 5, 6, 7] == 1] 

def question3():
    for y in range (2, 8):
        for x in range(0, 1000):
            if x % y == 1:
                print(x)

def grid():
    i = 0
    for y in range(0, 10):
        for x in range(0, 10):
            i += 1
            print(i,'-- y:', y, 'x:', x)
            
#    Find a number mod plus N such that 
#    N % 10 = 9
#    N % 9 = 8
#    N % 8 = 7
#    N % 7 = 6
#    N % 6 = 5
#    N % 5 = 4
#    N % 4 = 3
#    N % 3 = 2
#    N % 2 = 1

def search_mod_plus(N):
    n = [i for i in \
         [h for h in \
          [g for g in \
           [f for f in \
            [e for e in \
             [d for d in \
              [c for c in \
               [b for b in \
                [a for a in range(N + 1) \
                 if a % 10 == 9] \
                     if b % 9 == 8] \
                         if c % 8 == 7] \
                             if d % 7 == 6] \
                                 if e % 6 == 5] \
                                     if f % 5 == 4] \
                                         if g % 4 == 3] \
                                             if h % 3 == 2] \
                                                 if i % 2 == 1]
    return len(n)

    
def count_len_mod_plus(step, times):
    stop = step * times
    i = 0
    lst = []
    while i <= stop:
        lst.append(search_mod_plus(i))
        i += step
    return lst
L = count_len_mod_plus(10000, 1000)  
   
import matplotlib.pyplot as plt    
plt.plot(L)
plt.ylabel('distribution of Mp numbers in step 10000')
plt.show()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
