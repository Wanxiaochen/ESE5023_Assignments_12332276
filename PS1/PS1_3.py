# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 00:59:00 2023

@author: lenovo
"""

#Problem 3    
def Pascal_triangle(k):
    result = [1]
    for i in range(1, k + 1):
        row = result[i-1] * (k-i+1) // i
        result.append(row)
    print(result)

Pascal_triangle(100)
Pascal_triangle(200)