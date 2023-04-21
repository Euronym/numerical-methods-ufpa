'''
    Implements the lagrange's interpolation method for a given set of data points.
    Author: Bruno Martins
'''

import matplotlib.pyplot as plt
import numpy as np

def interpolate(x: np.array, y: np.array, num=100):

    f_interp = []

    x_min = np.min(x)
    x_max = np.max(y)

    x_ar = np.linspace(x_min, x_max, num)

    for x_interp in x_ar:
        f = 0
        for i in range(len(y)):
            l = y[i]
            for j in range(len(x)):
                if j == i:
                    continue
                l *= (x_interp - x[j]) / (x[i] - x[j])
            f += l

        f_interp.append(f)
        
    return x_ar, f_interp


def main():

    x = np.arange(10)

    y = np.cos(x)

    x_ar, f = interpolate(x, y)

    plt.scatter(x, y, c='red', label='original data')
    plt.plot(x_ar, f, c='blue', label='interpolated')

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()