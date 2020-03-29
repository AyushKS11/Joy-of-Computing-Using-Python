# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 10:58:44 2020

@author: Ayush
"""

n=int(input())
a=[int(x) for x in input().split()]
k=int(input())
key=a[k-1]
a.sort()
for i in range(len(a)):
  if key==a[i]:
    print(i+1,end="")
    break