from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from api.predict import predict

app = FastAPI()

class ImageRequest(BaseModel):
    image: str  # Imagen codificada en base64

@app.get("/")
def read_root():
    return {"message": "API de clasificación activa"}

@app.post("/predict/")
def predict_endpoint(request: ImageRequest):
    try:
        label = predict(request.image)
        return {"label": label}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    except AttributeError as e:
        raise HTTPException(status_code=500, detail=f"Attribute error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")