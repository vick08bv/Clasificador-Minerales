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
La clasificación de minerales es una tarea compleja para la mayoria de las personas, 
por sus características visuales únicas, pero hacer un clasificador de minerales 
capaz de superar a expertos en la materia es bastante difícil. Después del 
preprocesamiento para eliminar el fondo de las imágenes, la elección de una arquitectura
de red neuronal convolucional presenta otro reto debido al nivel de abstracción de las 
imágenes y el costo computacional de los entrenamientos.

## Fuentes de información y procedimientos aplicados

### Construcción del modelo
Se utiliza el framework de tensorflow y keras para construir un modelo de red neuronal secuencial.
La red neuronal consta de cuatro capas de convolución y una capa densa. 
Después de la elección del modelo se hace el ajuste de hiperparámetros con keras.

### Resultados modelo
Se prueban tres modelos de redes convolucionales, obteniendo resultados similares
(superiores al 70% de precisión en el conjunto de entrenamiento) 
después de un entrenamiento moderado a 15 épocas. Se ha elegido el mejor de estos 
tres modelos para hacer el ajuste de hiperparámetros.

### Pruebas sobre el modelo
Después de elegir el modelo final, se hace el ajuste de hiperparámetros de 
regularización en las últimas dos capas de convolución y dropout sólo en la 
capa densa, para evitar el sobreajuste de la red.

### Conclusiones
Después de añadir técnicas de regularización se nota una mejora en la precisión 
obtenida en el conjunto de validación, sin embargo, se ralentiza el entrenamiento de la red, 
por lo que hay aún una ventana de mejora en cuanto a la precisión que es posible alcanzar, 
pues se ha alcanzado un 73% de precisión después del entrenamiento final, cuando 
los primeros modelos sobreajustados alcanzaron un 84% de precisión.

## Conclusiones generales
A pesar de que existen miles de minerales en la naturaleza y varios métodos para 
su identificación, la clasificación de estos sólamente por métodos visuales presenta 
una serie de dificultades que aumentan considerablemente conforme se desea trabajar 
con más categorías, gracias a las variaciones que estos objetos presentan por lo que 
pueden ser confundidos fácilmente. Contando con más tiempo y capacidad de cómputo 
sería posible mejorar e incluso extender el modelo, mediante la exploración de otras 
técnicas y un ajuste más profundo de los parámetros escogidos.


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
  - Modelo entrenado: [trained_model.keras](api/models/trained_model.keras)
  - Predicción del modelo que usa la API: [predict.py](api/predict.py)
  - Procesamiento de imágenes que recibirá la API: [process_images_api.py](api/utils/process_images_api.py)
  - Código principal para el funcionamiento de la API: [main.py](api/main.py)
  - Dockerfile para la API en contenedor: [Dockerfile](Dockerfile)
- [Repositorio en GitHub](https://github.com/vick08bv/Clasificador-Minerales)
