# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 18:09:30 2023

@author: raghav
"""
import random

n = int(input('How long should be the random number array \n'))
abc = []

for i in range(0, n):
    print('Enter number at index ", i, ')
    item = int(input())
    abc.append(item)
print("User list is ", abc)

def swapList(newList):
    size = len(newList)
    
    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size-1] = temp
    
    return newList

print(swapList(abc))

