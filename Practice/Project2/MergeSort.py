# -*- coding: utf-8 -*-
"""
Spyder Editor
print ("hello")
This is a temporary script file.
"""

class Solution:
    def __init__(self, arr1, m, arr2, n):
        self.arr1 = arr1
        self.m = m
        self.arr2 = arr2
        self.n = n
        
        #print(n)
        #print("\n")
        #print(m)
        arr3 = []
        arr3 = arr1 + arr2
        #print(arr3)
        arr1 = arr3
        print(arr1)
        arr1.sort()
        print(arr1)
        
        
arr1 = [2,1,4,7]
m = 4
arr2 = [6,9,4,2,8]
n = 5

a = Solution(arr1, m, arr2, n)