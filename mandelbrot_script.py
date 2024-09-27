# %%
import numpy as np
import matplotlib.pyplot as plt
import mandelbrot

# %%
if __name__ == "__main__":
    # setting parameters (these values can be changed)
    xDomain, yDomain, max_iter = np.linspace(-2,1.5,500), np.linspace(-2,2,500), 40
    # xDomain, yDomain, max_iter = np.linspace(-0.8,-0.775,500), np.linspace(0.12,0.14,500), 500
    colormap = 'viridis'    # set to any matplotlib valid colormap

    # computing 2-d array to represent the mandelbrot-set
    iterationArray = mandelbrot.generate_data(xDomain, yDomain, max_iterations=max_iter)

    # plotting the data
    mandelbrot.plot(iterationArray, xDomain, yDomain)

# %%