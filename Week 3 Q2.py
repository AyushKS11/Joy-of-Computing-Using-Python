# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:04:43 2020

@author: Ayush
"""

list1=list(map(int,input().split()))
list1.sort()
length=len(list1)
print(list1[length-2],list1[1],end="")