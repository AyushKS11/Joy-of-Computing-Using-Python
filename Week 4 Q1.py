# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:18:46 2020

@author: Ayush
"""

list1=input()
x=list1.count('1')
y=list1.count('0')
l=len(list1)
if x==l-1 and y==1:
  print("YES",end='')
elif x==1 and y==l-1:
  print("YES",end="")
else:
  print("NO",end="")      
        