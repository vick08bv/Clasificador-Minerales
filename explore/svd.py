import cv2
import numpy as np
from matplotlib import pyplot as plt
import process_pipeline as pp

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

# A partir de la lista de valores singulares
# se crea la matriz de valores singulares,
# especificando cuántos de estos valores
# se tomarán en cuenta, ignorando los otros.
def matriz_valores_singulares(S, columnas, numero_valores):
    dimension = len(S)
    # Matriz del tamaño requerido
    matriz = [columnas * [0] for _ in range(dimension)]
    for i in range(numero_valores):
        matriz[i][i] = S[i]
    return matriz


images = []
for path in paths:
    image = cv2.imread(path)
    resized = pp.resize(image, pp.SIZE)

    # normalized = pp.normalize(cv2.cvtColor(resized.astype(np.uint8), cv2.COLOR_BGR2GRAY))
    # Descomposición en valores singulares.
    valores_usados = 32
    Ur, Sr, Vr = np.linalg.svd(cv2.cvtColor(resized.astype(np.uint8), cv2.COLOR_BGR2GRAY))
    Spr = np.array(matriz_valores_singulares(Sr, pp.SIZE[0], valores_usados))
    image = Ur.dot(Spr).dot(Vr)
    images.append(image)

# Mostrar la imagenes
i = 0
fig, axs = plt.subplots(3, 3, sharex=True, sharey=True)
fig.suptitle('Imágenes en gris')
for ax in axs.flat:
    ax.imshow(images[i].astype(np.uint8), cmap="gray")
    # ax.imshow(cv2.cvtColor(images[i].astype(np.uint8), cv2.COLOR_BGR2RGB))
    i += 1
plt.show()
