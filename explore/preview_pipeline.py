import cv2
import numpy as np
import matplotlib.pyplot as plt
import process_pipeline as pp

paths = [
        "preview_raw/Beryl_3.jpeg",
        "preview_raw/Carminite_1.jpeg",
        "preview_raw/Stibnite_7.jpeg",
        "preview_raw/Elbaite_9.jpeg",
        "preview_raw/Baryte_22.jpeg",
        "preview_raw/Smoky Quartz_7.jpeg",
        "preview_raw/Silver_4.jpeg",
        "preview_raw/Elbaite_6.jpeg",
        "preview_raw/Rhodochrosite_4.jpeg"]

images = []
for path in paths:
    image = cv2.imread(path)
    processed, filled = pp.process_image(image)
    images.append(processed)

# Mostrar la imagenes
i = 0
fig, axs = plt.subplots(3, 3, sharex=True, sharey=True)
fig.suptitle('Imágenes en gris')
for ax in axs.flat:
    ax.imshow(cv2.cvtColor(images[i].astype(np.uint8), cv2.COLOR_BGR2RGB))
    i += 1
plt.show()
