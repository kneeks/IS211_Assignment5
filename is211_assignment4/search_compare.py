#!user/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment Week 4"""


import random
import time


def sequential_search(alist, item):
    """
    Finding a particular value in a list that checks each element in 
    sequence until the desired element is found or the list is exhausted.
    
    Args:
        alist (list): list in which data will be searched
        item (mixed): item or value to search in given list
        
    Returns:
        tuple with the time it took to process and T or F if in the list
    """
    start = time.time()
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    tot = end - start
    return tot, found


def ordered_sequential_search(alist, item):
    """
    Finding a particular value in a list that checks each element in an ordered
    sequence until the desired element is found or the list is exhausted.
    
    Args:
        alist (list): list in which data will be searched
        item (mixed): item or value to search in given list
        
    Returns:
        tuple with the time it took to process and T or F if in the list
    """
    alist.sort()
    start = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = time.time()
    tot = end - start
    return tot, found


def binary_search_iterative(alist, item):
    """
    Finds the position of a target value within a sorted list.
    
    Args:
        alist (list): list in which data will be searched
        item (mixed): item or value to search in given list
        
    Returns:
        tuple with the time it took to process and T or F if in the list
    """
    alist.sort()
    start = time.time()
    first = 0
    last = len(alist) - 1
    found = False
	
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    end = time.time()
    tot = end - start
    return tot, found


def binary_search_recursive(alist, item):
    """
    Implementation of the binary search algorithm that uses 
    recursive method calls.
    
    Args:
        alist (list): list in which data will be searched
        item (mixed): item or value to search in given list
        
    Returns:
        tuple with the time it took to process and T or F if in the list
    """
    alist.sort()
    start = time.time()
    if len(alist) == 0:
        found = False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                return binary_search_recursive(alist[:midpoint], item)
            else:
                return binary_search_recursive(alist[midpoint + 1:], item)
    end = time.time()
    tot = end - start
    return tot, found


def random_list(num):
    """Generates a random list"""
    mylist = []
    for item in range(num):
        mylist.append(random.randint(1, num))
    return mylist


def main():
    """The program itself"""
    input_num = [500, 1000, 10000]

    for x in input_num:
        counter = 100
        time = [0, 0, 0, 0]
        while counter > 0:
            mylist = random_list(x)
            time[0] += sequential_search(mylist, -1)[0]
            time[1] += ordered_sequential_search(mylist, -1)[0]
            time[2] += binary_search_iterative(mylist, -1)[0]
            time[3] += binary_search_recursive(mylist, -1)[0]
            counter -= 1
        print 'For the list of {}:'.format(x)
        print ('Sequential search took %10.7f seconds to run, '
               'on average.') % (time[0] / 100)
        print ('Ordered sequential search took %10.7f seconds to run, '
               'on average.') % (time[1] / 100)
        print ('Iterative binary search took %10.7f seconds to run, '
               'on average.') % (time[2] / 100)
        print ('Recursive binary search took %10.7f seconds to run, '
               'on average.\n') % (time[3] / 100)
                
                
if __name__ == '__main__':
    main()