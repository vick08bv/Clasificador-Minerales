import cv2
import os
import process_pipeline as pp

# Carpetas de imágenes de muestra
current_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(current_dir, "../preview_raw")
output_dir = os.path.join(current_dir, "../preview_processed")


# Lee y procesa todas las imágenes
for filename in os.listdir(input_dir):
    input_path = os.path.join(input_dir, filename)
    image = cv2.imread(input_path)

    # Procesar la imagen
    processed, filled = pp.process_image(image)

    # Guardar la imagen procesada en la carpeta de salida
    output_path = os.path.join(output_dir, filename)
    cv2.imwrite(output_path, processed)
