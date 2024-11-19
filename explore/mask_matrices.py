import numpy as np
import matplotlib.pyplot as plt

lim = 256

l = np.linspace(-1, 1, lim)
x, y = np.meshgrid(l, l, indexing="xy")


def bump_function(decay):
    return np.exp(-decay * (x ** 2 + y ** 2))


bump_mask = bump_function(decay=1.41)

# plt.imshow(bump_mask, cmap='gray')
# plt.show()
