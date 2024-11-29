# Documentación General de la API

## Tabla de Contenidos
1. Introducción
2. Requisitos previos
3. Instalación
   - Clonación del Repositorio
   - Configuración del Entorno
4. Uso de Docker
   - Construcción de la Imagen
   - Ejecución del Contenedor
5. Endpoints de la API
6. Manejo de Errores

---
---

## Introducción
Esta API permite clasificar imágenes de minerales de 10 tipos

### Fecha de Actualización
Última actualización: 29-11-2024

---

## Requisitos Previos
- Docker y Docker Compose instalados.
- Git instalado.
- Python 3.12.
- Configuración básica del sistema operativo.

## Instalación

### Clonación del Repositorio
Clona el repositorio del proyecto:
```bash
git clone https://github.com/vick08bv/Clasificador-Minerales.git
cd Clasificador-Minerales
```
## Carga del modelo

El archivo del modelo es necesario para ejecutar la API.
Este ya esta cargado en GitHub, de modo que debio clonarse. (/api/models/trained_model.keras si usas Docker).
 
## Uso de Docker

### Construcción de la Imagen
Construye la imagen de Docker:
```bash
docker build -t image-classifer-api .
```

### Ejecución del Contenedor
Inicia el contenedor con Docker:
```bash
docker run -d -p 8000:8000 image-classifer-api
```
Accede a la API en `http://localhost:8000/docs` para la documentación interactiva.

### Detener y Eliminar Contenedores
Para detener un contenedor:
```bash
docker stop id_contenedor
```
Para eliminarlo:
```bash
docker rm id_contenedor
```

---

## Endpoints de la API

### POST /predict
**Descripción:** Clasifica una imagen para decir que tipo de mineral es.

**Request Body:**
- `image` (string): Imagen codificada en Base64.

**Ejemplo:**
```bash
curl -X POST -H "Content-Type: application/json" -d '{"image": "base64_string"}' http://localhost:8000/predict
```

**Response:**
```json
{
  "Quarz"
}
```

---

## Manejo de Errores
La API devuelve respuestas HTTP con códigos de error estándar:
- **400**: Error en la solicitud (p. ej., imagen inválida o no soportada).
- **404**: Endpoint no encontrado.
- **500**: Error interno del servidor.

## Observaciones

- Los modelos deben estar entrenados y disponibles en el directorio `/api`.
