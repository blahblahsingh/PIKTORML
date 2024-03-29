# -*- coding: utf-8 -*-
"""Assignment_1c

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LCYt_N5ToYZmaQNcVoeCQe8lt7o_XYcr

#PIKTORML Python Assignment

**DISCLAIMER : Plagiarism is strictly prohibited. This is a best practise for your good. If copied then you are fooling yourself**

##Introduction

You will be given a question and the code for it should be added with a code block cell added just below it with comments which explain the code

For example

***
Example Question:

Write a program :

A function which implements quicksort on an array input to it and returns a sorted array
***
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print quicksort([3,6,8,10,1,2,1])

"""**Question 1: (30 points)(20 for code 10 for comments)**

Write a function which does a mtrix multiplication on two arrays input to it

Hint : Use nested loops, AB is not always equal to BA in matrices
"""

#Your code goes here
A = [[9,8,7],  # input matrix 
      [6,5,4],  
      [3,2,1]]  
 
B = [[1,2,3],  # input matrix
      [4,5,6],  
      [7,8,9]]

C = [[0,0,0], # C = AB
      [0,0,0],
      [0,0,0]]

# loops for multiplication begins

for i in range(len(A)):  
   for j in range(len(B[0])):  
       for k in range(len(B)):  
           C[i][j] += A[i][k] * B[k][j]
           
for x in C:  #iterating through the rows in C
  print(x)

"""**Question 2: (40 points)(30 for code 10 for comments)**

Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

Print the area of a circle object defined by the class you created with radius 3
"""

#your code goes here

class Circle:
  def __init__(self, r): # calls itself when instanciated
    self.r = r # assigning input param to radius "r"
  def calArea(self):
    return ((22/7)*self.r**2) # calculate area of circle

c1 = Circle(3) #instance of Circle

print("Area for radius", c1.r, "is:", c1.calArea()) # Prints Area of the circle

"""**Question 3: (60 points)(50 for code 10 for comments)**

Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

500

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
We can define recursive function in Python.
"""

# your code here

#The example given in the question f(5)=500 is misleading as the solution is 501

inp = 5
def f(n):
  if n == 0:  # f(0) = 1
    return 1 
    
  for i in range(n):
    return f(n-1)+100 #calling method recursively
 
print (f(inp))

"""**Question 4**: (**120 points)(60 for code 60 for comments)**

***This is a bonus question to prove your mettle to the world***

***Even if you are not able to solve this it won't be graded but if you are able to solve it you get bonus points***

It is possible to write ten as the sum of primes in exactly five different ways:

* 7 + 3
* 5 + 5
* 5 + 3 + 2
* 3 + 3 + 2 + 2
* 2 + 2 + 2 + 2 + 2

What is the **first value** which can be written as the sum of primes in **over** five thousand different ways?

Write a program(a function) to solve the above problem to a generic input value and returns the first value which can be written in >= the input value times 

Print the value for input = 5000
"""

#your code here

#Cool problem, will take it up later

"""**END OF ASSIGNMENT**"""