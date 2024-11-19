import cv2
import numpy as np
from matplotlib import pyplot as plt
import process_pipeline as pp

paths = [
        "preview_raw/Beryl_3.jpeg",
        "preview_raw/Carminite_1.jpeg",
        "preview_raw/Stibnite_7.jpeg",
        "preview_raw/Elbaite_9.jpeg",
        "preview_raw/Malachite_27.jpeg",
        "preview_raw/Smoky Quartz_7.jpeg",
        "preview_raw/Silver_4.jpeg",
        "preview_raw/Crocoite_1.jpeg",
        "preview_raw/Rhodochrosite_4.jpeg"]

paths = ["preview_processed/Quartz_3.jpeg",
         "preview_processed/Schorl_2.jpeg",
         "preview_processed/Almandine_3.jpeg",
         "preview_processed/Aegirine.jpeg",
         "preview_processed/Kyanite.jpeg",
         "preview_processed/Siderite_3.jpeg",
         "preview_processed/Topaz_10.jpeg",
         "preview_processed/Copper_4.jpeg",
         "preview_processed/Adamite.jpeg",
         ]

images = []
for path in paths:
    image = cv2.imread(path)
    resized = pp.resize(image, pp.SIZE)
    f = np.fft.fft2(resized)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))
    images.append(f)

# Mostrar la imagenes
i = 0
fig, axs = plt.subplots(3, 3, sharex=True, sharey=True)
fig.suptitle('Imágenes en gris')
for ax in axs.flat:
    ax.imshow(images[i].astype(np.uint8))
    # ax.imshow(cv2.cvtColor(images[i].astype(np.uint8), cv2.COLOR_BGR2RGB))
    i += 1
plt.show()