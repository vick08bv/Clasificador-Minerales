import os
import numpy as np
import cv2


# Operaciones de procesamiento
def resize(img):
    # Comprobar el tamaño de la imagen
    if img.shape[1] > new_size[0] or img.shape[0] > new_size[1]:
        img_resized = cv2.resize(img, new_size, interpolation=cv2.INTER_LANCZOS4)
    else:
        print(filename)
        img_resized = img
    return img_resized


def normalize(img):
    # Cálculo de la media y la desviación
    mean = np.mean(img)
    std = np.std(img)

    # Normalizar usando Z-Score
    return (img - mean) / std


# Directorios
input_dir = "../preview_raw"
output_dir = "preview_resized"

# Directorio de salida
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Tamaño deseado
new_size = (256, 256)

# Procesar las imágenes
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # Lectura
        img_path = os.path.join(input_dir, filename)
        image = cv2.imread(img_path)

        # Redimensionamiento
        img_resized = resize(image)

        # Imagen final
        img_processed = img_resized

        # Escritura
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, img_processed)
