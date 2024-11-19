import cv2
import numpy as np
import matplotlib.pyplot as plt

def fill_contours(original_matrix):
    contours, _ = cv2.findContours(original_matrix.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filled_image = np.zeros_like(original_matrix)
    cv2.drawContours(filled_image, contours, -1, 1, thickness=cv2.FILLED)  # Rellenar contornos
    return filled_image


# def getBordered(image, width):
#     bg = np.zeros(image.shape)
#     contours, _ = cv2.findContours(image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     biggest = 0
#     bigcontour = None
#     for contour in contours:
#         area = cv2.contourArea(contour)
#         if area > biggest:
#             biggest = area
#             bigcontour = contour
#    return cv2.drawContours(bg, [bigcontour], 0, (255, 255, 255), width).astype(bool)


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

# t = Image.open("preview_processed/Adamite.jpeg")

images = [cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB) for path in paths]
images = [cv2.Canny(image=image, threshold1=125, threshold2=250) for image in images]
images = [cv2.GaussianBlur(np.float32(image), (7, 7), 0) for image in images]
images = [np.where(image > 0, 1, 0) for image in images]

clustered_images = []

for image in images:
    clustered_images.append(fill_contours(image))

# for image in images:
#     alpha = 1  # Ajustar este valor según sea necesario
#     clustered_images.append(create_alpha_shape_image(image, alpha))
# for image in images:
#
#     # 1. Obtener las coordenadas de los unos
#     ones_indices = np.argwhere(image == 1)
#
#     # 2. Aplicar DBSCAN a los unos
#     dbscan = DBSCAN(eps=10, min_samples=5)
#     labels_ones = dbscan.fit_predict(ones_indices)
#
#     # 3. Crear una matriz de resultados para visualizar
#     result_matrix = np.zeros(image.shape)  # Inicializamos la matriz de resultados
#
#     # 4. Llenamos la matriz de resultados con los labels de los clusters
#     for cluster_label, (i, j) in zip(labels_ones, ones_indices):
#         if cluster_label != -1:  # Ignorar el ruido
#             result_matrix[i, j] = 1  # Mantener los unos
#     clustered_images.append(image)
#
# for image in images:
#
#     coords, labels = kmeans_separation(image)
#     clustered_images.append(visualize_kmeans(image, coords, labels))


# filled = []
# for image in images:
#    filled.append(getBordered(image, 10))

    # # get the (largest) contour
    # contours = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # contours = contours[0] if len(contours) == 2 else contours[1]
    # big_contour = max(contours, key=cv2.contourArea)
    # result = np.zeros_like(image)
    # cv2.drawContours(result, [big_contour], 0, (255,255,255), cv2.FILLED)
    # # draw white filled contour on black background
    # result = np.zeros_like(image)
    # cv2.drawContours(result, [big_contour], 0, (255,255,255), cv2.FILLED)
    # filled.append(result)

# Mostrar la imagenes
i = 0
fig, axs = plt.subplots(3, 3, sharex=True, sharey=True)
fig.suptitle('Imágenes en gris')
for ax in axs.flat:
    ax.imshow(clustered_images[i], cmap='gray')
    i += 1
plt.show()
