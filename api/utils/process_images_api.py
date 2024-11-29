import cv2
import numpy as np
from typing import Any

def process_images_api(image: Any) -> np.ndarray:
    image =cv2.resize(image,(224,224))
    image = image/255.0
    image = np.expand_dims(image,axis=0)
    return image 
