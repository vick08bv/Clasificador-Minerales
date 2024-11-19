import cv2
import matplotlib.pyplot as plt
import numpy as np
from trash.mask_matrices import bump_function

paths = ["preview_processed/Quartz_3.jpeg",
         "preview_processed/Schorl_2.jpeg",
         "preview_processed/Azurite_9.jpeg",
         "preview_processed/Silver_2.jpeg",
         "preview_processed/Kyanite.jpeg",
         "preview_processed/Siderite_3.jpeg",
         "preview_processed/Topaz_10.jpeg",
         "preview_processed/Copper_4.jpeg"]

images = [cv2.imread(path, 0) for path in paths]

mask = np.round(255 * bump_function(1)).astype(int)
images = [image * mask for image in images]
images = [np.round(255 * image / np.max(image)).astype(int) for image in images]
images.append(mask)

# Mostrar la imagenes
i = 0
fig, axs = plt.subplots(3, 3, sharex=True, sharey=True)
fig.suptitle('Imágenes en gris')
for ax in axs.flat:
    ax.imshow(images[i], cmap='gray')
    i += 1
plt.show()
