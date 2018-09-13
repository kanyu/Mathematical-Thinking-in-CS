# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 22:46:01 2018

@author: Kan
"""

def countdown(num):
    """
    The yield statement pauses the function and saves the local state so that
    it can be resumed right where is left off.
    >>> val = countdown(5)
    >>> val
    <generator object countdown at 0x10213aee8>
    
    Calling the function does not execute it. 
    We know this because the string Starting did not print. 
    Instead, the function returns a generator object 
    which is used to control execution.
    
    >>> next(val)
    >>> Starting
    >>> 5
    >>> next(val)
    >>> 4
    >>> next(val)
    >>> 3
    >>> next(val)
    >>> 2
    >>> next(val)
    >>> 1
    >>> next(val)
    Traceback (most recent call last):
    
      File "<ipython-input-47-a2a2bf9708c5>", line 1, in <module>
        next(val)
    
    StopIteration
    
    """
    print('Starting')
    while num > 0:
        yield num
        num -= 1
        
my_list = ['a', 'b', 'c', 'd']
# generator object use () compare to list  use []
gen_obj = (x for x in my_list)
gen_obj2 = (4, 5, 6, 7)
for val in gen_obj:
    print(val)
    
for val in gen_obj2:
    print(val)
    
import sys
g = (i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0)
print(sys.getsizeof(g))  
"""
>>> 88
"""

l = [i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0]
print(sys.getsizeof(l))
"""
>>>38216
"""

import cProfile
cProfile.run('sum((i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0))')
# see code performance / number of function call 
#    NOTE: Keep in mind that generator expressions are drastically faster 
#    when the size of your data is larger than the available memory.
#    
#    Use Cases
#    Generators are perfect for reading a large number of large files 
#    since they yield out data a single chunk at a time 
#    irrespective of the size of the input stream. 
#    They can also result in cleaner code by decoupling 
#    the iteration process into smaller components.

import os
def emit_lines(pattern=None):
    lines = []
    for dir_path, dir_names, file_names in os.walk('test/'):
        for file_name in file_names:
            if file_name.endswith('.py'):
                for line in open(os.path.join(dir_path, file_name)):
                    if pattern in line:
                        lines.append(line)
    return lines

#    This function loops through a set of files in the specified directory. 
#    It opens each file and then loops through each line 
#    to test for the pattern match.
#    This works fine with a small number of small files. 
#    But, what if we’re dealing with extremely large files? 
#    And what if there are a lot of them? Fortunately, 
#    Python’s open() function is efficient and doesn’t load 
#    the entire file into memory. But what if our matches list far exceeds 
#    the available memory on our machine?
#    So, instead of running out of space (large lists) and time 
#    (nearly infinite amount of data stream) when processing large amounts of data, 
#    generators are the ideal things to use, as they yield out data one time at a time 
#    (instead of creating intermediate lists).

#    GENERATOR ###########################################

#    Let’s look at the generator version of the above problem and try to understand 
#    why generators are apt for such use cases using processing pipelines.
#    We divided our whole process into three different components:
    #    Generating set of filenames
    #    Generating all lines from all files
    #    Filtering out lines on the basis of pattern matching
    
def generate_filenames():
    """
    generates a sequence of opened files
    matching a specific extension
    """
    for dir_path, dir_names, file_names in os.walk('test/'):
        for file_name in file_names:
            if file_name.endswith('.py'):
                yield open(os.path.join(dir_path, file_name))
                
def cat_files(files):
    """
    takes in an iterable of filenames
    """
    for fname in files:
        for line in fname:
            yield line
            
def grep_files(lines, pattern = None):
    """
    takes in an iterable of lines
    """
    for line in lines:
        if pattern in line:
            yield line
            
py_files = generate_filenames()
py_file = cat_files(py_files)
lines = grep_files(py_file, 'python')
for line in lines:
    print(line)

import requests
import re

def get_pages(link):
    links_to_visit = []
    links_to_visit.append(link)
    while links_to_visit:
        current_link = links_to_visit.pop(0)
        page = requests.get(current_link)
        for url in re.findall('<a href = "([^"]+)">', str(page.content)):
            if url[0] == '/':
                url = current_link + url[1:]
            pattern = re.compile('https?')
            if pattern.match(url):
                links_to_visit.append(url)
        yield current_link
        

webpage = get_pages('https://bunnybear.home.blog')
for result in webpage:
    print(result)
                


                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                





















