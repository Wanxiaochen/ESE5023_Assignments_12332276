# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 00:59:01 2023

@author: lenovo
"""

#Problem 5 
import matplotlib.pyplot as plt
list_number = ['1','2','3','4','5','6','7','8','9'] 
list_symbol = ["0","1","2"] 
symbol_pool = [] 
for i in list_symbol:
    for j in list_symbol:
        for k in list_symbol:
            for l in list_symbol:
                for m in list_symbol:
                    for n in list_symbol:
                        for o in list_symbol:
                            for p in list_symbol:
                                symbol_pool.append(i+j+k+l+m+n+o+p)

Total_solutions = []
def Find_expression(n):
    r = n
    mate_number = 0 
    for i in symbol_pool:
        s=list(i)
        result = []
        result.append('1')
        for j in range(0,8):
            if s[j] =="0":
                result.append(list_number[j+1])
            elif s[j] == "1":
                result.append("+")
                result.append(list_number[j+1])
            else:
                result.append("-")
                result.append(list_number[j+1])
        all_result = ''.join(result)
        final_result = int(eval(all_result))
        if final_result == r:
            mate_number += 1
            print(all_result +"="+ str(final_result))        
    if mate_number == 0:
        print("未找到匹配的等式")
    else:  
        print("共有" + str(mate_number) + "种匹配的结果")
    Total_solutions.append(mate_number)

Total_solutions = []
Find_expression(50)
print(Total_solutions)

Total_solutions = []
for x in range(1, 101):
    Find_expression(x)
    print(Total_solutions)
max_value = max(Total_solutions)
print(max_value)
min_value = min(Total_solutions)
print(min_value)

max_numbers = [i for i, value in enumerate(Total_solutions, start=1) if value == max_value]
print(max_numbers)
min_numbers = [i for i, value in enumerate(Total_solutions, start=1) if value == min_value]
print(min_numbers)

x = range(1, 101)
plt.plot(x, Total_solutions)
plt.xlabel('Number')
plt.ylabel('Total Solutions')
plt.title('Total Solutions for Number')
plt.show()