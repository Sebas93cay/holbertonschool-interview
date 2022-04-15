#!/usr/bin/python3
"""
pascal triangle function generator
This is the first exercise for holberton interviews
"""

def pascal_triangle(n):
  """
  This functions return an array of arrays with the numbers for the first n
  rows of the pascal triangle, or an empty list if n is less or equal to cero
  """
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