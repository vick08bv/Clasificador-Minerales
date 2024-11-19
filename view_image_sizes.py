import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.124 Safari/537.36 '
}


# Obtiene el tamaño de una imagen desde la URL
def get_image_size(image_url):
    try:
        # Enviar una solicitud para obtener los bytes de la imagen
        response = requests.get(image_url, headers=headers, stream=True)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        return img.size
    except Exception as e:
        print(f"Error obteniendo el tamaño de imagen desde {image_url}: {e}")
        return None, None


widths = []
heights = []

# Descarga por lotes
counter_from = 1
counter_to = 1000

# Guarda las imágenes
with open("trash/list_filtered_urls173.csv") as file:
    lines = file.readlines()
    line_count = 0
    for line in lines:
        line_count += 1
        if line_count < counter_from:
            pass
        else:
            if line_count > counter_to:
                break
            url, label = line.strip().split(",")
            width, height = get_image_size(url)
            if width is not None and height is not None:
                widths.append(width)
                heights.append(height)

plt.scatter(widths, heights)
plt.show()
