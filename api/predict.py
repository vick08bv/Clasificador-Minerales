from keras.models import load_model
from api.utils.process_images_api import process_images_api
import cv2
import base64
import numpy as np
from typing import Any

# Cargamos la dirección donde se encuentra el modelo
MODEL_PATH = "api/models/trained_model.keras"

# Cargamos las categorias
LABELS = {
    0: "Copper",
    1: "Pyromorphite",
    2: "Quartz (Var: Amethyst)",
    3: "Malachite",
    4: "Azurite",
    5: "Wulfenite",
    6: "Pyrite",
    7: "Quartz",
    8: "Fluorite",
    9: "Calcite"
}

# Cargamos el modelo
model = load_model(MODEL_PATH)

# imagen procesada para base64

def preprocess_base54_image(base64_image: str) -> Any:
    decoded_image = base64.b64decode(base64_image)
    np_image = np.frombuffer(decoded_image, np.uint8)
    image = cv2.imdecode(np_image,cv2.IMREAD_COLOR)
    return image

# Procesamos la imagen para que tenga los parametros que se usaron en el
# modelo
def predict(base64_image: str) -> str:
    image = preprocess_base54_image(base64_image)
    processed_image = process_images_api(image)

    prediction = model.predict(processed_image)
    predicted_index = np.argmax(prediction,axis=1)[0]
    return LABELS.get(predicted_index,"Etiqueta desconocida")
