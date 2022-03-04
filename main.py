from re import sub
from matplotlib import pyplot as plt
import numpy as np
from progressbar import progressbar

import colorama
from colorama import Fore, Style

from time import sleep

# Creating array for bounds

left_bound = int(input("Left Bound? "))
right_bound = int(input("Right Bound? "))

x_axis = []

print(Fore.CYAN + "\n\n\nGenerating X Axis" + Fore.GREEN)
ind = 0
for i in range(left_bound, right_bound+1, 1):
    x_axis.append(left_bound + ind)
    ind += 1



# PreComputing Values
equation_string = input("Equation? ")
partitions = input("Partitions? ")
plt.title("Graph Output")
plt.xlabel("x")
plt.ylabel("y")

x_value = []
y_value = []

print(Fore.CYAN + "\n\n\nGenerating Graph" + Fore.GREEN)










# Calculate stuff 

f = lambda x : eval(equation_string)
a = left_bound; b = right_bound; N = partitions
n = 10 # Use n*N+1 points to plot the function smoothly

x = np.linspace(a,b,N+1)
y = f(x)

X = np.linspace(a,b,n*N+1)
Y = f(X)

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.plot(X,Y,'b')
x_left = x[:-1] # Left endpoints
y_left = y[:-1]
plt.plot(x_left,y_left,'b.',markersize=10)
plt.bar(x_left,y_left,width=(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
plt.title('Left Riemann Sum, N = {}'.format(N))

plt.subplot(1,3,2)
plt.plot(X,Y,'b')
x_mid = (x[:-1] + x[1:])/2 # Midpoints
y_mid = f(x_mid)
plt.plot(x_mid,y_mid,'b.',markersize=10)
plt.bar(x_mid,y_mid,width=(b-a)/N,alpha=0.2,edgecolor='b')
plt.title('Midpoint Riemann Sum, N = {}'.format(N))

plt.subplot(1,3,3)
plt.plot(X,Y,'b')
x_right = x[1:] # Left endpoints
y_right = y[1:]
plt.plot(x_right,y_right,'b.',markersize=10)
plt.bar(x_right,y_right,width=-(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
plt.title('Right Riemann Sum, N = {}'.format(N))

plt.show()