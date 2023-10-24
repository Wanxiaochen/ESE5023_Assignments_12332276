# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 00:59:01 2023

@author: lenovo
"""

#Problem 4 
def Least_moves(x):
	if x <= 3:
		return x-1
	else:
		T = [0 for i in range(x+1)]
		for i in range(4, x+1):
			if i%2 != 0:
			    T[i] = 1 + T[i-1]
			else:
				T[i] = 1 + min(T[i-1], T[int(i/2)])
	print(T[x])

import random
x = random.randint(1,101)
print(x)
Least_moves(x)