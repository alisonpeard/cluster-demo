import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # setting parameters (these values can be changed)
    xDomain, yDomain = np.linspace(-2,1.5,500), np.linspace(-2,2,500)
    bound = 2
    power = 2             # any positive floating point value
    max_iterations = 40   # any positive integer value
    colormap = 'magma'    # set to any matplotlib valid colormap


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

    # plotting the data
    ax = plt.axes()
    ax.set_aspect('equal')
    graph = ax.pcolormesh(xDomain, yDomain, iterationArray, cmap = colormap)
    plt.colorbar(graph)
    plt.xlabel("Real-Axis")
    plt.ylabel("Imaginary-Axis")
    plt.title('Mandelbrot set for $z_{{new}} = z^{{{}}} + c$'.format(power))
    plt.savefig("mandel.png")
