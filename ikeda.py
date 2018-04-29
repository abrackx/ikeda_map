from matplotlib import pyplot as plt
import math
from random import random
import random
import numpy as np
import imageio


def t_n(x, y):
    return 0.4 - 6 / (1 + x**2 + y**2)


def ikeda_map(u, x, y):
    xn = 1 + u * (x * math.cos(t_n(x, y)) - y * math.sin(t_n(x, y)))
    yn = u * (x * math.sin(t_n(x, y)) + y * math.cos(t_n(x, y)))
    return [xn, yn]

def rand_list(p, r):
    l = []
    for i in range(p):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        l.append([x, y])

    return l



def ikeda_plot(points, num_iter, u, r):
    #generate p amount of points [x,y], apply the function for n iterations
    #with u as the parameter value for the ikeda map
    x = []
    y = []
    xinit = []
    yinit = []
    l = rand_list(points, r)
    initial_list = l.copy()
    images = []

    for k in range(len(initial_list)):
        xinit.append(initial_list[k][0])
        yinit.append(initial_list[k][1])

    plt.scatter(xinit, yinit)
    # plt.ylim(-r, r)
    # plt.xlim(-r, r)
    plt.savefig("frame" + str(0) + ".png")
    images.append(imageio.imread("frame" + str(0) + ".png"))
    plt.clf()

    for i in range(num_iter):
        x = []
        y = []
        for coord in range(len(l)):
            l[coord] = ikeda_map(u, l[coord][0], l[coord][1])
        for j in range(len(l)):
            x.append(l[j][0])
            y.append(l[j][1])
        plt.scatter(x,y)
        # plt.ylim(-r, r)
        # plt.xlim(-r, r)
        plt.savefig("frame" + str(i + 1) + ".png")
        plt.clf()
        images.append(imageio.imread("frame" + str(i + 1) + ".png"))

    imageio.mimsave('final.gif', images)
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
    r = input('Enter the bound for random point generation (don\'t get too crazy): ')
    ikeda_plot(int(p), int(n), float(u), int(r))

    v = input('Press enter to start again. Press x to exit. ')

    if v == 'x':
        running = False




