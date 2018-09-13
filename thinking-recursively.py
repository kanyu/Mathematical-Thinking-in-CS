# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 12:15:24 2018

@author: Kan
"""

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

def deliver_iter():
    for house in houses:
        print("Delivering presents to", house)
        

def deliver_recursive(houses):
    if len(houses) == 1:
        print("Delivering presents to", houses[0])
    else:
        print("Delivering presents to", houses[0])
        deliver_recursive(houses[1:])

# Each function call represents an elf doing his work
def deliver_recursive2(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)
        
    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]
        
        # Divides his work among two elves
        deliver_recursive2(first_half)
        deliver_recursive2(second_half)
        
        
def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)
"""----------------------------------------------------------------------------
    Recursive Data Structures in Python
    A data structure is recursive if it can be deﬁned 
    in terms of a smaller version of itself. 
    
    A list is an example of a recursive data structure. 
    Let me demonstrate. 
    Assume that you have only an empty list at your disposal, 
    and the only operation you can perform on it is this:
----------------------------------------------------------------------------"""

# Return a new list that is the result of 
# adding element to the head (i.e. front) of input_list

def attach_head(element, input_list):
    return[element] + input_list


attach_head(1,                                                  # Will return [1, 46, -31, "hello"]
            attach_head(46,                                     # Will return [46, -31, "hello"]
                        attach_head(-31,                        # Will return [-31, "hello"]
                                    attach_head("hello", [])))) # Will return ["hello"]

from functools import lru_cache
def Fibnaive(n):
    print("Calculating F", "(", n, ")", sep="", end=", ")

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return Fibnaive(n-1) + Fibnaive(n-2)
    
@lru_cache(maxsize = None)
def Fib(n):
    print("Calculating F", "(", n, ")", sep="", end=", ")
    
    # Base case
    if n <= 2:
        return n
    
    # Recursive case
    else:   
        return Fib(n - 1) + Fib(n - 2)



























