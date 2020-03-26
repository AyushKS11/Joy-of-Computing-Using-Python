# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:48:15 2020

@author: Ayush
"""

x=[int(x) for x in input().split()]
x1=sorted(x)
c=0
for i in range (len(x)):
  if x[i]==x1[c]:
    c=c+1
print(len(x)-c,end="")    