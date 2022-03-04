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
print(left_bound)
print(right_bound)
x_axis = []

print(Fore.CYAN + "\n\n\nGenerating X Axis" + Fore.GREEN)
ind = 0
for i in range(left_bound, right_bound+1, 1):
    x_axis.append(left_bound + ind)
    ind += 1
    print(i)
print(x_axis)



plt.grid(True)
# PreComputing Values
equation_string = input("Equation? ")
subdivision = int(input("Precision "))
jump_amount = 1/subdivision
plt.title("Graph Output")
plt.xlabel("x")
plt.ylabel("y")

x_value = []
y_value = []

for i in progressbar(x_axis):
    current_jump = jump_amount
    for j in range(subdivision):
        x = x_axis[i]+current_jump
        x_value.append(x_axis[i]+current_jump)
        y_value.append(eval(equation_string))
        #plt.scatter(x_axis[i]+current_jump, eval(equation_string))

        current_jump = current_jump + jump_amount
    
plt.plot(x_value,y_value)
plt.show()
