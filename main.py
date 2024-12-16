from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import base64

app = FastAPI(title="Text to Base64 Converter API", version="1.0.0")

# Modelo de entrada
class TextInput(BaseModel):
    text: str

# Clave API estática (puedes cambiarla a cualquier valor)
API_KEY = "my-static-api-key"

# Endpoint para convertir a Base64
@app.post("/convert-to-base64", summary="Convierte texto a Base64")
def convert_to_base64(input: TextInput, x_api_key: str = Header(...)):
    """
    Convierte texto a Base64. Requiere una API Key válida.
    """
    # Verificar la API Key
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    try:
        # Convertir texto a Base64
        base64_encoded = base64.b64encode(input.text.encode("utf-8")).decode("utf-8")
        return {"base64": base64_encoded}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
