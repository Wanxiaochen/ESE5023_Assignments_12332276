# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 00:59:00 2023

@author: lenovo
"""

#Problem 2
#2.1
import random
def IntegerMatrix(m,n):
    M=[]
    for j in range(m):
        M.append([0]*n)
    for i in range(m):
        for j in range(n):
            M[i][j]=random.randint(0,50)
    return(M)
  
M1 = IntegerMatrix(5,10)
print(M1)  
M2 = IntegerMatrix(10,5)  
print(M2)     

#2.2
def Matrix_multip(M1,M2):
    rows, cols = len(M1), len(M2[0])
    result = [[0] * cols for n in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(len(M2)):
                result[i][j] += M1[i][k] * M2[k][j]
    print(result)

Matrix_multip(M1,M2) 