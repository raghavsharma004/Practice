# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 16:27:05 2023

@author: raghav
"""
import csv
import re
from collections import OrderedDict

a_list=[]
dict = {}

with open('Book1.txt', "r", encoding="utf8") as f:
        tsv_reader = csv.reader(f, delimiter="\t")
        #print(tsv_reader)
        
        for row in tsv_reader:
            (a, b) = row
           # print(f"{a} : {b}")
            dict[a] = b
            

sorted_dict = OrderedDict(sorted(dict.items()))

print(sorted_dict)


#print(dict.keys())    
f.close()