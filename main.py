from matplotlib import pyplot as plt
import numpy as np


# Getting bounds

left_bound = int(input("Left Bound? "))
right_bound = int(input("Right Bound? "))


# Getting Equation and number of divisions
equation_string = input("Equation? ")
partitions = int(input("Partitions? "))




# Calculate all the points 

f = lambda x : eval(equation_string)
a = left_bound; b = right_bound; N = partitions
n = 10 # Use n*N+1 points to plot the function smoothly

x = np.linspace(a,b,N+1)
y = f(x)

X = np.linspace(a,b,n*N+1)
Y = f(X)

plt.figure(figsize=(15,5))


dx = (b - a)/N
x_left = np.linspace(a,b-dx,N)
x_midpoint = np.linspace(dx/2,b - dx/2,N)
x_right = np.linspace(dx,b,N)
h = (b - a) / (n - 1)


x_mid = (x[:-1] + x[1:])/2
mid = np.sum(f(x_mid)*dx)



plt.subplot(1,4,1)
plt.grid(True, color = 'black', linestyle = '--', linewidth = 1)
plt.plot(X,Y,'b')
x_left = x[:-1] # Left endpoints
y_left = y[:-1]
plt.plot(x_left,y_left,'b.',markersize=10)
plt.bar(x_left,y_left,width=(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
j = np.sum(f(x_left) * dx)
plt.title('Left Riemann Sum, Ans ≈ {0:.2f}'.format(j))




plt.subplot(1,4,2)
plt.grid(True, color = 'black', linestyle = '--', linewidth = 1)
plt.plot(X,Y,'b')
x_mid = (x[:-1] + x[1:])/2 # Midpoints
y_mid = f(x_mid)
plt.plot(x_mid,y_mid,'b.',markersize=10)
plt.bar(x_mid,y_mid,width=(b-a)/N,alpha=0.2,edgecolor='b')
plt.title('Midpoint Riemann Sum, Ans ≈ {0:.2f}'.format(mid))




plt.subplot(1,4,3)
plt.grid(True, color = 'black', linestyle = '--', linewidth = 1)
plt.plot(X,Y,'b')
x_right = x[1:] # Left endpoints
y_right = y[1:]
plt.plot(x_right,y_right,'b.',markersize=10)
plt.bar(x_right,y_right,width=-(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
right_riemann_sum = np.sum(f(x_right) * dx)
plt.title('Right Riemann Sum, Ans ≈ {0:.2f}'.format(right_riemann_sum))




plt.subplot(1,4,4)
plt.grid(True, color = 'black', linestyle = '--', linewidth = 1)
plt.plot(X,Y,'b')

plt.plot(x_right,y_right,'b.',markersize=10)
for i in range(N):
    xs = [x[i],x[i],x[i+1],x[i+1]]
    ys = [0,f(x[i]),f(x[i+1]),0]
    plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)

h = float(b - a) / n
s = 0.0
s += f(a)/2.0
for i in range(1, n):
    s += f(a + i*h)
s += f(b)/2.0
ans =  s * h
plt.title('Trapezoid Rule, N ≈ {0:.2f}'.format(ans))

plt.show()




