# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:21:36 2020

@author: Ayush
"""

r,c=input().split(" ")
r=int(r)
c=int(c)
mat=[[0 for i in range(c)]for j in range(r)]
val=1
for i in range(r):
  for j in range(c):
    mat[i][j]=val
    val=val+1
for i in range(r):
  for j in range(c):
    if j!=(c-1):
      print(mat[i][j],end=" ")
    else:
      print(mat[i][j],end="")
  if i!=(r-1):
    print()