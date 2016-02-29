#!user/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment Week 4"""


import random
import time


def insertion_sort(alist):
    """Implementation of insertion sort"""
    start = time.time()
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index
        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = current_value
    end = time.time()
    tot = end - start
    return tot


def gap_insertion_sort(alist, start, gap):
    """Implementation of gap insertion sort"""
    for x in range(start + gap, len(alist), gap):
        current_value = alist[x]
        position = x
        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = current_value


def shell_sort(alist):
    """Diminishing increment sort"""
    start = time.time()
    sublist_count = len(alist) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(alist, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end = time.time()
    tot = end - start
    return tot


def python_sort(alist):
    """A list sort"""
    start = time.time()
    alist = alist.sort()
    end = time.time()
    tot = end - start
    return tot


def random_list(num):
    """Generates a random list"""
    mylist = []
    for item in range(num):
        mylist.append(random.randint(1, num))
    return mylist


def main():
    """The main function of the program."""
    input_num = [500, 1000, 10000]

    for x in input_num:
        counter = 100
        time = [0, 0, 0]
        while counter > 0:
            mylist = random_list(x)
            time[0] += insertion_sort(mylist)
            time[1] += shell_sort(mylist)
            time[2] += python_sort(mylist)
            counter -= 1
        print 'For the list of {}: '.format(x)
        print ('Insertion Sort took %10.7f seconds to run, '
               'on average.' % (time[0] / 100))
        print ('Shell Sort took %10.7f seconds to run, '
               'on average.' % (time[1] / 100))
        print ('Python Sort took %10.7f seconds to run, '
               'on average.\n' % (time[2] / 100))


if __name__ == "__main__":
    main()