from keras.models import load_model
from api.utils.process_images_api import process_images_api
import cv2
import base64
import numpy as np
from typing import Any

MODEL_PATH = "api/models/trained_model.keras"

LABELS = {
    0: "Amethyst",
    1: "Azurite",
    2: "Calcite",
    3: "Copper",
    4: "Fluorite",
    5: "Malachite",
    6: "Pyrite",
    7: "Pyromorphite",
    8: "Quartz",
    10: "Wulfenite"
}

model = load_model(MODEL_PATH)

def preprocess_base54_image(base64_image: str) -> Any:
    decoded_image = base64.b64decode(base64_image)
    np_image = np.frombuffer(decoded_image, np.uint8)
    image = cv2.imdecode(np_image,cv2.IMREAD_COLOR)
    return image

def predict(base64_image: str) -> str:
    image = preprocess_base54_image(base64_image)
    processed_image = process_images_api(image)

    prediction = model.predict(processed_image)
    predicted_index = np.argmax(prediction,axis=1)[0]
    return LABELS.get(predicted_index,"Etiqueta desconocida")
