# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:19:57 2020

@author: Ayush
"""

n=input()
num=int(n)
factorial=1
if num==0:
  print("The factorial of 0 is 1")
else:
  for i in range (1,num+1):
    factorial=factorial*i
  print(factorial,end="")  