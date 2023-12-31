# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 14:22:48 2023

@author: raghav
"""

print("\n Enter string : \t")
value = input()

print(f'\n You entered : {value}')

def findLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter

#print(findLen(value))

