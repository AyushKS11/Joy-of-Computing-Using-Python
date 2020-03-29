# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 11:03:09 2020

@author: Ayush
"""

def printDict():
  x=int(input())
  d={}
  for i in range (1,x+1):
    d[i]=i**2
  print(d,end="")
printDict()  
printDict()