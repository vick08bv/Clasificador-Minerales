import cv2
import numpy as np

# Tamaño de procesamiento
SIZE = (256, 256)
# Tamaño de salida
OUTPUT_SIZE = (128, 128)
# Centro de la imagen
CENTER_X, CENTER_Y = SIZE[0] // 2, SIZE[1] // 2
# Límites usados en el filtro de Canny
CANNY_THRESHOLD_1 = 100
CANNY_THRESHOLD_2 = 75
# Intensidad del desenfoque gaussiano
GAUSSIAN_BLUR_KERNEL_SIZE = 5
# Límite de la anchura de las aristas (Cero para anchura máxima)
EDGE_THRESHOLD = 0
# Valor positivo de la máscara
MARKER = 1
# Criterio de conexidad
CONNECTIVITY_DIAGONAL = 8
CONNECTIVITY_SIMPLE = 4
# Eliminación de agujeros
AREA_THRESHOLD_SUP = (SIZE[0] * SIZE[1]) // 3
AREA_THRESHOLD_INF = (SIZE[0] * SIZE[1]) // 32
# Varianza
VARIANCE_THRESHOLD = 0.01

""" Operaciones de procesamiento """


# Redimensionamiento
def resize(image, size):
    # Tamaño original de la imagen
    height, width, channels = image.shape

    # Orientación de la imagen
    if height < width:
        crop_width = (width - height) // 2
        image = image[:, crop_width:crop_width + height, :]
    else:
        crop_height = (height - width) // 2
        image = image[crop_height:crop_height + width, :, :]
    resized_image = cv2.resize(image, size, interpolation=cv2.INTER_LANCZOS4)
    return resized_image


# Encuentra los bordes del mineral
def canny_filter(image, threshold1, threshold2):
    image = cv2.cvtColor(np.float32(image), cv2.COLOR_BGR2RGB)
    return cv2.Canny(image=cv2.convertScaleAbs(image), threshold1=threshold1, threshold2=threshold2)


# Engrosa las aristas detectadas
def thinner_edges(image, kernel_size, threshold, marker):
    image = cv2.GaussianBlur(np.float32(image), (kernel_size, kernel_size), 0)
    return np.where(image > threshold, marker, 0)


# Rellena el contorno encontrado en la imagen
def fill_contours(image):
    contours, _ = cv2.findContours(image.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filled_image = np.zeros_like(image).astype(np.uint8)
    cv2.drawContours(filled_image, contours, -1, 1, thickness=cv2.FILLED)
    return filled_image


# Elimina pequeñas islas del mineral
def remove_components(image, connectivity, threshold):
    # Etiqueta las regiones conectadas
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(image, connectivity=connectivity)
    # Recorre cada componente
    for i in range(1, num_labels):
        area = stats[i, cv2.CC_STAT_AREA]
        # Se elimina la isla si su área es menor que el umbral especificado
        if area < threshold:
            image[labels == i] = 0
    return image


# Elimina pequeñas islas del fondo, rescatando trozos del mineral
def fill_holes(image, foreground, connectivity, area_threshold, variance_threshold):
    # Máscara
    foreground_mask = foreground == 1
    # Inversión de valores
    background_mask = ~foreground_mask
    # Etiqueta las regiones conectadas
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(background_mask.astype(np.uint8),
                                                                    connectivity=connectivity)
    # Valores promedios encontrados
    foreground_mean = np.mean(image[foreground_mask], axis=0)
    background_mean = np.mean(image[background_mask], axis=0)
    # Recorre cada componente
    for i in range(1, num_labels):
        area = stats[i, cv2.CC_STAT_AREA]
        region_mask = labels == i
        region_mean = np.mean(image[region_mask], axis=0)
        # Se rescata la isla si tiene un color más parecido al del mineral
        norms = [np.linalg.norm(background_mean-region_mean),
                 np.linalg.norm([255, 255, 255]-region_mean),
                 np.linalg.norm([0, 0, 0]-region_mean)]
        var = np.var(region_mean)
        if var > variance_threshold and area < area_threshold \
                and np.linalg.norm(foreground_mean - region_mean) < min(norms):
            foreground[region_mask] = 1

    return foreground


# Flujo de procesamiento
def process_image(image):
    resized_image = resize(image, SIZE)
    edges = canny_filter(resized_image, CANNY_THRESHOLD_1, CANNY_THRESHOLD_2)
    blur_edges = cv2.GaussianBlur(np.float32(edges), (GAUSSIAN_BLUR_KERNEL_SIZE, GAUSSIAN_BLUR_KERNEL_SIZE), 0)
    filled_mask = fill_contours(blur_edges)
    filled_mask = fill_holes(resized_image, filled_mask, CONNECTIVITY_DIAGONAL, AREA_THRESHOLD_SUP, VARIANCE_THRESHOLD)
    filled_mask = remove_components(filled_mask, CONNECTIVITY_SIMPLE, AREA_THRESHOLD_INF)
    rounded = np.round(resized_image * filled_mask[:, :, np.newaxis]).astype(np.uint8)
    return cv2.resize(rounded, OUTPUT_SIZE, interpolation=cv2.INTER_LANCZOS4)
