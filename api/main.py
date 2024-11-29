from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from api.predict import predict

app = FastAPI()

class ImageRequest(BaseModel):
    image_base64: str  # Imagen codificada en base64

@app.get("/")
def read_root():
    return {"message": "API de clasificación activa"}

# Creación de endpoint
@app.post("/predict/")
def predict_endpoint(request: ImageRequest):
    # Validamos la entrada del usuario y si suba una imagen
    if not request.image_base64:
        # Si hay un error de tipo 404 le mandamos un mensaje
        raise HTTPException(status_code=404, detail="Imagen no proporcionada o inválida")
    try:
        # usamos la fun predict para clasificar la imagen
        label = predict(request.image_base64)
        # Devolvemos la predicción
        return {"La categoria es": label}
    
    except ValueError as e:
        # si la entrada no es válida
        raise HTTPException(status_code=400,detail=f"Error de valor: {str(e)}")
    except AttributeError as e:
        # si hay algún error de atributos
        raise HTTPException(status_code=500, detail=f"Error de atributo: {str(e)}")
    except Exception as e:
        # Cualquier otro error
        raise HTTPException(status_code=500, detail="Error interno del servidor")