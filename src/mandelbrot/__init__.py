"""
Demonstration package for creating and plotting the Mandelbrot set.
"""
import numpy as np
import matplotlib.pyplot as plt

from .utils import *
from .io import *
from .plotting import *

def generate_data(xDomain, yDomain, bound=3, power=2, max_iterations=40):
    """Computer 2D array to represent the mandelbrot set."""
    # computing 2-d array to represent the mandelbrot-set
    iterationArray = []
    for y in yDomain:
        row = []
        for x in xDomain:
            c = complex(x,y)
            z = 0
            for iterationNumber in range(max_iterations):
                if(abs(z) >= bound):
                    row.append(iterationNumber)
                    break
                else: z = z**power + c
            else:
                row.append(0)
        iterationArray.append(row)
    return iterationArray
    

def plot(iterationArray, xDomain, yDomain, power=2, colormap="viridis"):
    """Plot the Mandelbrot set."""
    # plotting the data
    ax = plt.axes()
    ax.set_aspect('equal')
    graph = ax.pcolormesh(xDomain, yDomain, iterationArray, cmap=colormap)
    plt.colorbar(graph)
    plt.xlabel("Real-Axis")
    plt.ylabel("Imaginary-Axis")
    plt.title('Mandelbrot set for $z_{{new}} = z^{{{}}} + c$'.format(power))
    plt.savefig("mandel.png")


def hypot(a, b):
    return np.sqrt(a**2 + b**2)