# Memoria Técnica

## Índice
- [Portada](#portada)
- [Alcance del proyecto](#alcance-del-proyecto)
  - [Objetivo](#objetivo)
  - [Introducción](#introducción)
- [Fuentes de información y procedimientos aplicados](#fuentes-de-información-y-procedimientos-aplicados)
  - [Construcción del modelo](#construcción-del-modelo)
  - [Resultados modelo](#resultados-modelo)
  - [Pruebas sobre el modelo](#pruebas-sobre-el-modelo)
  - [Conclusiones](#conclusiones)
- [Conclusiones generales](#conclusiones-generales)
- [Anexos](#anexos)

## Portada
- **Nombre del Proyecto**: Clasificador de Minerales
- **Fecha**: 31 de noviembre de 2024.
- **Glosario**: 
  - *Mineral*: Sustancia natural, de composición química definida. Normalmente sólido e inorgánico, y con cierta estructura cristalina.
  - *Variedad*: Grupo de minerales que tienen una estructura cristalina determinada y una composición química en un rango de variaciones continuas.
  - *Cuarzo*: El cuarzo es un mineral compuesto de sílice (SiO2), el segundo más común en la corteza terrestre, después del feldespato.
  - *[MinDat](https://www.mindat.org/)*: Base de datos abierta con imágenes de minerales, rocas y meteoritos.

## Alcance del proyecto

### Objetivo
Los minerales presentan características complejas a simple vista, sin embargo, la clasificación precisa de estos es necesaria para diversas aplicaciones en la geología y en la minería. 
Inspirado en ello, el objetivo es hacer un clasificador de minerales que sea capaz de identificar imágenes pertenecientes a 10 categorías distintas, 
mediante una red neuronal convolucional entrenada desde cero con imágenes obtenidas de MinDat.

### Introducción
Dar una breve explicación o resumen del resultado del proyecto.

## Fuentes de información y procedimientos aplicados

### Construcción del modelo
Se utiliza el framework de tensorflow y keras para construir un modelo de red neuronal secuencial.
La red neuronal consta de cuatro capas de convolución y una capa densa. 
Después de la elección del modelo se hace el ajuste de hiperparámetros con keras.

### Resultados modelo
Documenta los resultados obtenidos del modelo.

### Pruebas sobre el modelo
Describe las pruebas realizadas sobre el modelo.

### Conclusiones
Conclusiones específicas de cada modelo probado.

## Conclusiones generales
Presenta las conclusiones globales del proyecto.

## Anexos
- Flujo de trabajo:
  - Visualización del conjunto de datos: [viewing_data.ipynb](viewing_data.ipynb)
  - Selección de categorías a descargar: [filter_url_list.py](filter_url_list.py)
  - Descarga de las imágenes: [download_images.py](download_images.py)
  - Desestimación de imágenes con otras extensiones: [remove_png_images.py](remove_png_images.py)
  - Selección de imágenes para el entrenamiento: [remove_extra_images.py](remove_extra_images.py)
  - Preprocesamiento de imágenes: [process_images.py](process_images.py)
  - Creación de subcarpetas para alimentar el modelo [create_subfolders.py](create_subfolders.py)
  - Entrenamiento y comparación de modelos: [training_models.ipynb](training_models.ipynb)
  - Ajuste de hiperparámetros: [tuning_parameters.ipynb](tuning_parameters.ipynb)
  - Entrenamiento final del modelo ajustado: [cnn_model.py](cnn_model.py)
- [Repositorio en GitHub](https://github.com/vick08bv/Clasificador-Minerales)
