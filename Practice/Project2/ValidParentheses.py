class Solution:
    valid_counter = 0
    
    def __init__(self, s):
        self.s = str(s)
        print("\n")
        print(s)
        counter1_open = 0
        counter1_close = 0
        counter2_open = 0
        counter2_close = 0
        counter3_open = 0
        counter3_close = 0
        
        
        for i in s:
                        
            if("(" in i):
               counter1_open = counter1_open + 1
               
            if(")" in i):
                counter1_close = counter1_close + 1
                
            if("{" in i):
               counter2_open = counter2_open + 1
               
            if("}" in i):
                counter2_close = counter2_close + 1
                
            if("[" in i):
               counter3_open = counter3_open + 1
               
            if("]" in i):
                counter3_close = counter3_close + 1
                
               
        print(counter1_open)
        print(counter1_close)
        print(counter2_open)
        print(counter2_close)
        print(counter3_open)
        print(counter3_close)
        
        if counter1_open != counter1_close:
            Solution.valid_counter += 1
        elif counter2_open != counter2_close:
            Solution.valid_counter += 1
        elif counter3_open != counter3_close:
            Solution.valid_counter += 1
            
        # if valid_counter > 0:
        #     print("\nString invalid")
        # else:
        #     print("\nString is valid")
            
        
a = input("Enter the string with parenthesis\n")        
obj = Solution(a)

if Solution.valid_counter > 0:
     print("\nString invalid")
else:
     print("\nString is valid")
#print(Solution.valid_counter)