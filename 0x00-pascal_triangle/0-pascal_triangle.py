#!/usr/bin/python3
"""
pascal triangle function generator
"""

def pascal_triangle(n):
  if (n<=0):
    return []
  if n==1:
    return[[1]]

  top = pascal_triangle(n-1)
  last_row = top[-1]
  new_row = [1]

  for i,x in enumerate(last_row[:-1]):
    new_row.append(x+last_row[i+1])
  
  new_row.append(1)
  top.append(new_row)
  return top