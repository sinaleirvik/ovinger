#Task 1
a = 12
b = 15
text = "dette er en string"
print(f'a + b = {a+b}')
print(f'a * b = {a*b}')
print (text)

#Task 2
l_1 = [1,2,3,4]
l_2 = [4,3,2,1]
print(f'l_1 + l_2 = {l_1+l_2}')
#not valid operation: 
#print(f'l_1 - l_2 = {l_1 - l_2}')
#print(f'l_1 * l_2 = {l_1*l_2}')

l_s= ["fuck", "fuck"]
print(3*l_s)
print(l_s[1]) #indekserer

l_s.append("you")
print(l_s)

l_s.remove ("fuck")
print (l_s)

#Task 3
def odd_numbers (n):
    odd = []
    for i in range (n):
        if i%2 != 0: 
            odd.append (i)
    
    return odd

print(odd_numbers(10))

#Task 4
import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, log

print(f'The square root of 36 is: {np.sqrt(36)}')
print(f'The square root of 64 is: {math.sqrt(64)}')

def f(x):
    return x**2

def g(x): 
    return np.sqrt(x)

x = np.linspace (1, 20, 100)

plt.plot(x, f(x), color = "pink" )
plt.plot(x, g(x), color = "purple")
plt.show ()

#Task 5
x, y = symbols ('x y')

f = 3*x**2
g = log(x) #need to import log-function from sympy.
h = x**3 + 2*y**2

df = diff(f,x)
print (f'The derivative of {f} is {df}')

dg = diff(g, x)
print (f'The derivative of {g} is {dg}')

dhx = diff(h, x)
dhy = diff (h, y)

l = [dhx, dhy]
print (f'The partial derivatives of {h} is {l}')
