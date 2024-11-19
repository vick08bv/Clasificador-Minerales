import os
import re

# Directorio de imágenes
current_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(current_dir, "images_processed")

# Lectura de la lista de url
labels = {}
with open("list_selected_labels (full_names).csv") as file:
    lines = file.readlines()
    for line in lines:
        label = line.strip()
        match = re.search(r"\(Var: ([^\)]+)\)", label)
        if match:
            label = match.group(1)
        labels[label] = 0

# Cuenta el número de imágenes por categoría
for image_name in os.listdir(images_dir):
    name = os.path.splitext(image_name)[0].split("_")[0]
    labels[name] += 1

with open("list_selected_labels (summary).csv", "w") as file:
    for label, total in labels.items():
        file.write(label + "," + str(total) + "\n")
