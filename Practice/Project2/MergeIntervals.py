# -*- coding: utf-8 -*-
"""
Spyder Editor
print ("hello")
This is a temporary script file.
"""

class MergeSolution:
    def __init__(self, intervals):
        i = intervals
        print(i)
        i.sort()
        
        p = 1
        while p < len(i):
            #print(i[p][1])
            if i[p][0] <= i[p-1][1]:
                i[p-1][0] = min(i[p-1][0], i[p][0])
                
                i[p-1][1] = max(i[p-1][1], i[p][1])
                
                i.pop(p)
                
            else:
                p+=1
                #continue
        print(i)
                
                
                
            
            
        
        
        
        
        
        
a = [[1,3],[2,6],[8,10],[15,18]]
b = [[1,4],[4,5]]

x = MergeSolution(b)
#print(x)