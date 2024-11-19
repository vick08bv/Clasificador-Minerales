import tensorflow as tf
from tensorflow.keras import layers, models, regularizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.optimizers import Adam
import os

# Tamaño de la imagen y las categorías
img_height = 64
img_width = 64
batch_size = 32
num_categories = 10
learning_rate = 0.0005

# Carpeta de imágenes procesadas
current_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(current_dir, "images_processed")

# Lista todas las clases disponibles
all_classes = sorted(os.listdir(input_dir))

# Selecciona las primeras `num_categories_to_load` clases
selected_classes = all_classes[:num_categories]
print(f"Clases seleccionadas: {selected_classes}")


def preprocess_input(image):
    # Centra y escala la imagen
    return (image - 127.5) / 255.0


# Usar un generador personalizado
train_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    validation_split=0.1,
    rotation_range=10,           # Rotaciones aleatorias
    width_shift_range=0.1,       # Desplazamiento horizontal aleatorio
    height_shift_range=0.1,      # Desplazamiento vertical aleatorio
    shear_range=0.1,             # Transformaciones de corte
    zoom_range=0.1,              # Zoom aleatorio
    horizontal_flip=True,        # Volteo horizontal
    fill_mode='nearest'          # Relleno de píxeles
)

# Generador de imágenes para el conjunto de entrenamiento
train_generator = train_datagen.flow_from_directory(
    input_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training',
    classes=selected_classes,
    shuffle=True
)

# Generador de imágenes para el conjunto de validación
validation_generator = train_datagen.flow_from_directory(
    input_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation',
    classes=selected_classes,
    shuffle=False
)

# Imprime la información sobre las clases
print("Class mapping:", train_generator.class_indices)

# Convierte el generador en un tf.data.Dataset para agregar repetición y precarga
train_dataset = tf.data.Dataset.from_generator(
    lambda: train_generator,
    output_signature=(
        tf.TensorSpec(shape=(None, img_height, img_width, 3), dtype=tf.float32),
        tf.TensorSpec(shape=(None, num_categories), dtype=tf.float32)
    )
)

validation_dataset = tf.data.Dataset.from_generator(
    lambda: validation_generator,
    output_signature=(
        tf.TensorSpec(shape=(None, img_height, img_width, 3), dtype=tf.float32),
        tf.TensorSpec(shape=(None, num_categories), dtype=tf.float32)
    )
)

train_dataset = train_dataset.repeat()
validation_dataset = validation_dataset.repeat()

train_dataset = train_dataset.prefetch(tf.data.AUTOTUNE)
validation_dataset = validation_dataset.prefetch(tf.data.AUTOTUNE)

# Definición de la arquitectura a utilizar
model = models.Sequential([

    # Capa 1
    layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(img_height, img_width, 3)),
    layers.MaxPooling2D((2, 2)),

    # Capa 2
    layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D((2, 2)),

    # Capa 3
    layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D((2, 2)),

    # Capa 4
    layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D((2, 2)),

    # Capa 5
    layers.Conv2D(512, (3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D((2, 2)),

    # Aplanamiento
    layers.GlobalAveragePooling2D(),

    # Capa densa
    layers.Dense(1024, activation='relu'),

    # Capa de salida
    layers.Dense(num_categories, activation='softmax')

])

# Compilación del modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Resumen del modelo para ver el total de parámetros
model.summary()

# Se detiene el entrenamiento del modelo cuando deja de haber mejora
early_stopping = EarlyStopping(monitor='val_loss',
                               patience=3,
                               restore_best_weights=True)

# Ajusta dinámicamente la tasa de entrenamiento cuando no hay mejora
reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.25,
    patience=2,
    min_lr=1e-6
)

# Entrenamiento del modelo
history = model.fit(
    train_dataset,
    epochs=25,
    callbacks=[reduce_lr],
    validation_data=validation_dataset,
    validation_steps=validation_generator.samples // batch_size,
    steps_per_epoch=train_generator.samples // batch_size,
)

# Se guarda el modelo entrenado
model.save('modelo_entrenado.keras')

# Rendimiento del modelo en el conjunto de validación
val_loss, val_acc = model.evaluate(validation_dataset, steps=validation_generator.samples // batch_size)
print(f"Precisión en el conjunto de validación: {val_acc * 100:.2f}%")
