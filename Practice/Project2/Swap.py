# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:11:35 2023

@author: raghav
"""

n = int(input('How long should be the random number array \n'))
abc = []

for i in range(0, n):
    print('Enter number at index ", i, ')
    item = int(input())
    abc.append(item)
print("User list is ", abc)

def swapList(newList):
    