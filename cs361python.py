# -*- coding: utf-8 -*-
"""CS361PythonExercises.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WftC5E807Hb8ww6luBpWe-kBPIYI7plk
"""

print(5/3)
print(5%3)
print(5.0/3)
print(5/3.0)
print(5.2%3)

# print(2000.3**200)
print(1.0+1.0-1.0)
print(1.0+1.0e20-1.0e20)

print (float(123))
print (float('123'))
print (float('123.23'))

print (int(123.23))
# print (int('123.23'))
print (int(float('123.23')))

print (str(12))
print (str(12.2))

print (bool('a'))
print (bool(0))
print (bool(0.1))

for i in range(5):
  print(i)

type(range(5))

numberFound = 0
x = 11
while numberFound<20 :
  if x%5==0 and x%7==0 and x%11==0:
    print(x)
    numberFound+=1
  x+=1

def is_prime(n):
  count = 2
  while count<n:
    if n%count == 0:
      return True
    count += 1
    
  return False

print(is_prime(5))
print(is_prime(6))
print(is_prime(7))
print(is_prime(10))
print(is_prime(11))
print(is_prime(13))

def is_prime_updated(n):
  if n==2 or n==3:
    return True
  if ( int(n-1)%6 == 0.0 ):
    return True
  if ( int((n+1)%6) == 0 ):
    return True
  return False
  
print(is_prime_updated(3))
print(is_prime_updated(4))
print(is_prime_updated(5))
print(is_prime_updated(6))
print(is_prime_updated(7))
print(is_prime_updated(10))
print(is_prime_updated(11))
print(is_prime_updated(13))
print(is_prime_updated(19))
print(is_prime_updated(24))
print(is_prime_updated(50))

def PrimesUpToN (n):
  primes = []
  i=2
  while(i<n):
    if (is_prime_updated(i)):
      primes.append(i)
    i += 1
  return primes

print(PrimesUpToN (6))
print(PrimesUpToN (13))
print(PrimesUpToN (29))

def FirstNPrimes(n):
  primes = []
  count=0
  i=2
  while (count<n):
    if (is_prime_updated(i)):
      primes.append(i)
      count+=1
    i+=1
  return primes

print(FirstNPrimes (5))
print(FirstNPrimes (10))

def elementsOfList (list):
  result = []
  for element in list:
    result.append(element)
  return result

list1 = ["apple","bear","cat"]
elementsOfList(list1)

# or simply print the list, a method is not necessary

def reverseList (list):
  result = []
  length = len (list)
  while (length>0):
    result.append(list[length-1])
    length -= 1
  return result

list1 = ["apple","bear","cat"]
reverseList(list1)

# or simply use the reverse method: list1.reverse()

def countElements (list):
  count = 0
  for element in list:
    count += 1
  return count

list1 = ["apple","bear","cat"]
countElements(list1)

a = [3,"apple",20.0, 12, "trees"]
b = a
b[1] = "japan"

print (a)
print (b)

c = a[:]
c[2] = 523

print (a)
print (c)

def set_first_elem_to_zero(l):
  l[0]=1;
  return l;

list1 = [4,2,6,4,1,2]
list2 = set_first_elem_to_zero(list1)

print(list1)
print(list2)

def combineLists (l):
  result = []
  for i in l:
    for j in i:
      result.append(j)
  return result

test = [[1,2],[2,3],[],[1]]
combineLists (test)

import matplotlib.pyplot as plt
import math

x = []
y = []

for i in range(0,20):
  x.append(i/10)
  function1 = math.sin((i/10)-2)
  function2 = function1**2
  function3 = math.exp(-1*((i/10)**2))
  function4 = function2*function3
  y.append(function4)

plt.plot(x,y,color="red")
plt.title("f(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

def iterateProduct (list):
  if list == []:
    return "empty list"
  result = 1;
  for i in list: 
    result *= i
  return result

list = [1,2,3,4]
print(iterateProduct(list))
list1 = []
print(iterateProduct(list1))
list2 = [4]
print(iterateProduct(list2))
list3 = [5,8]
print(iterateProduct(list3))

def recurseProduct (list):
  if list == []:
    return "empty list"
  elif len(list)==1:
    return list[0]
  elif len(list)==2:
    return list[0]*list[1]
  else:
    return list[0] * recurseProduct(list[1:len(list)])

listA = [1,2,3,4]
print(recurseProduct(listA))
listB = [4]
print(recurseProduct(listB))
listC = [4,5]
print(recurseProduct(listC))
listD = []
print(recurseProduct(listD))

def fibonacci(n):
  if n<0 : 
    return "positive numbers only"
  if n==0 or n==1:
    return n
  else:
    return fibonacci(n-2)+fibonacci(n-1)
# with Python3, there is no longer a limit to the value of integers
print (fibonacci(6))
print (fibonacci(-3))
print (fibonacci(0))