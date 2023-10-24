# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 00:58:59 2023

@author: lenovo
"""

#Problem 1
def Print_values(a,b,c):
    if a>b:
        if b>c: print(a,b,c)
        elif a>c: print(a,c,b)
        else: print(c,a,b)
    elif b>c:
        if a>c: print(b,a,c)
        else: print(b,c,a)
    else: print(c,b,a)

import random
a,b,c  = random.random()*100, random.random()*100, random.random()*100
print(a,b,c) 
Print_values(a,b,c)