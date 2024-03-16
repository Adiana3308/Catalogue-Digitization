import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import json
import os



# Function to check if a path is a directory
def is_directory(path):
    return os.path.isdir(path)

# Define the image data generator
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Assuming you have a dataset with subfolders for each class in '/path/to/dataset'
train_generator = train_datagen.flow_from_directory(
    'F:/Catalog Digitization/ecommerce products',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    'F:/Catalog Digitization/ecommerce products',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)

# Create a base MobileNetV2 model
base_model = tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')

# Freeze the base model
base_model.trainable = False

# Create a new model
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(train_generator.num_classes, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_generator, epochs=10, validation_data=validation_generator)

# Save the trained model
model.save('F:/Catalog Digitization/image_recognition.h5')

# Save class indices to a JSON file
class_indices_path = 'F:/Catalog Digitization/class_indices.json'
if not is_directory(class_indices_path):
    with open(class_indices_path, 'w') as f:
        json.dump(train_generator.class_indices, f)
