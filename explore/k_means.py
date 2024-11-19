import cv2
import numpy as np
from trash.mask_matrices import bump_function

image_path = "../preview_processed/Azurite_9.jpeg"
image_path = "../preview_processed/Adamite.jpeg"
# Cargar la imagen
image, gray = cv2.imread(image_path, cv2.COLOR_BGR2GRAY), cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

mask = 255 - np.round(255 * bump_function(1)).astype(int)
extra = gray + mask
# extra = (255.0 * extra)/np.max(extra)

# Convertir la imagen a formato de datos flotantes y cambiar de forma
Z = image.reshape((-1, 3))
D = extra.reshape((-1, 1))
Z = np.float32(np.hstack((Z, D)))

# Definir criterios y número de clusters
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
k = 3  # Número de clusters

# Aplicar K-means
_, labels, centers = cv2.kmeans(Z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convertir los centros a uint8 y reconstruir la imagen segmentada
centers = np.uint8(centers[:, :3])
segmented_image = centers[labels[:, :3].flatten()]
segmented_image = segmented_image.reshape(image.shape)

# Mostrar resultados
cv2.imshow('Imagen Original', image)
cv2.imshow('Imagen Segmentada', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
