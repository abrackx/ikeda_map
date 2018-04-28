from matplotlib import pyplot as plt
import math
from random import random
import random
import numpy as np
import pylab


def t_n(x, y):
    return 0.4 - 6 / (1 + x**2 + y**2)


def ikeda_map(u, x, y):
    xn = 1 + u * (x * math.cos(t_n(x, y)) - y * math.sin(t_n(x, y)))
    yn = u * (x * math.sin(t_n(x, y)) + y * math.cos(t_n(x, y)))
    return [xn, yn]

def rand_list(p):
    l = []
    for i in range(p):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        l.append([x, y])

    return l



def ikeda_plot(points, num_iter, u):
    #generate p amount of points [x,y], apply the function for n iterations
    #with u as the parameter value for the ikeda map
    x = []
    y = []
    xinit = []
    yinit = []
    l = rand_list(points)
    initial_list = l.copy()




    for i in range(num_iter):
        for coord in range(len(l)):
            l[coord] = ikeda_map(u, l[coord][0], l[coord][1])


    for j in range(len(l)):
        x.append(l[j][0])
        y.append(l[j][1])

    for k in range(len(initial_list)):

        xinit.append(initial_list[k][0])
        yinit.append(initial_list[k][1])

    plt.subplot(121)
    plt.scatter(xinit, yinit)
    plt.title('initial values')
    plt.subplot(122)
    plt.scatter(x, y)
    plt.title('values after ' + str(num_iter) + ' iterations')
    plt.show()

running = True
while running:
    p = input('Enter the number of points: ')
    n = input('Enter the number of iterations: ')
    u = input('Enter your choice of u value (between 0 and 1 in decimal form): ')
    ikeda_plot(int(p), int(n), float(u))

    v = input('Press enter to start again. Press x to exit. ')

    if v == 'x':
        running = False




