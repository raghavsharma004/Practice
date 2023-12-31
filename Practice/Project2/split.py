# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 23:48:09 2023

@author: raghav
"""

string = "geeks quiz practice code"

s = string.split()[::-1]
#print(s)
l = []
reverse_string = ''

for i in s:
    l.append(i)
    reverse_string = reverse_string + " " + i
    
    
print("\n")
    
print(reverse_string)