# Clasificador-Minerales
Clasificación de imágenes de minerales mediante una red neuronal convolucional usando el framework de tensorflow-keras.

## Origen de los datos:
Las imágenes se obtienen del sitio web de [MinDat](https://mindat.org) 
con ayuda de la lista de URL's que alberga, provista por Oliver Hennigh en su [repositorio](https://github.com/loliverhennigh/MinDat-Mineral-Image-Dataset/blob/master/img_url_list.csv) de GitHub.

## Descripción del modelo:
Se ha usado una red neuronal secuencial con 1,823,882 de parámetros, 
compuesta por cuatro capas de convolución y una capa totalmente conectada. 
El modelo, alimentado con 50,000 imágenes de 96x96 pixeles, 
es capaz de clasificar diez categorías, 
previamente escogidas por su relevancia 
dentro de MinDat y en la comunidad geológica en general.

## Flujo de trabajo:
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

## Directorios:
- images: Imágenes recién descargadas.
- images_samples: Muestra para visualización.
- images_png: Residuales con extensiones como png, bmp y mpo.
- images_unused: Imágenes que no se usaron durante el entrenamiento del modelo.
- images_processed: Directorio de las imágenes procesadas y usadas por el modelo.
