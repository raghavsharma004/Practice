# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 14:45:25 2023

@author: raghav
"""

print("\nEnter the string with words separated by spaces\n")
n = input()

split_n = n.split(" ")
for i in split_n:
    if len(i)%2==0:
        print(i)
#print(split_n)

