# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:03:31 2019

@author: patelkk
"""

def largest_odd_times(L):
    mydictionary = {}
    for element in L:
        if element in mydictionary:
            mydictionary[element] += 1
        else:
            mydictionary[element] = 1
#    print('before the deletion, mydictionary is',mydictionary)
    for e2 in mydictionary.copy():
        if mydictionary[e2]%2 == 0:
            del(mydictionary[e2])
    if mydictionary == {}:
        return None
    return max(mydictionary)
    

        
    