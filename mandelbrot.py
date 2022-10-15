import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(N_max, threshold, n):

    x,y = np.meshgrid(np.linspace(-2, 1, n), np.linspace(-1.5, 1.5, n))
    #Line 6 is responsible for creating arrays the size of n with desired parameters
    c = x + y * 1j
    #Line 8 is responsible for crating the nxn grid
    z = 0
    #Line 10 sets a base
    for j in range(N_max):
        z = z ** 2 + c
    #Lines 12-13 execute the mandelbrot iterations
    z[abs(z) > threshold] = threshold
    mask = (abs(z) < threshold)
    #Line 16 Creates the matrix
    return mask
    """
    This function calculates the mandelbrot set
    - N_max is the max number of iterations to be performed in the function
    - threshold is float threshold for the function
    - n represents the length of the set 
    - There is also a return statement that returns an updated nxn matrix as it gets iterated 
        """


# Calls the mandelbrot function
mask = mandelbrot(N_max=50, threshold=50, n=1100)

# Plots and saves the image as 'mandelbrot.png'
plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig("mandelbrot.png")

