import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

import json

# Load the trained model
model_path = 'F:/Catalog Digitization/image_recognition.h5'
model = load_model(model_path)

# Load class indices from the saved file
with open('F:/Catalog Digitization/class_indices.json', 'r') as f:
    actual_class_indices = json.load(f)

# Load an unseen image for prediction
unseen_image_path = r'F:\Catalog Digitization\sofa.jpg'
img = image.load_img(unseen_image_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0  # Normalize the image

# Make predictions
predictions = model.predict(img_array)

# Print raw predictions
#print("Raw Predictions:", predictions)

# Get the predicted category index
predicted_category_index = np.argmax(predictions)
print("Predicted Category Index:", predicted_category_index)

# Reverse the mapping (index to label)
class_labels = {v: k for k, v in actual_class_indices.items()}

# Get the predicted category label
predicted_category_label = class_labels.get(predicted_category_index, "Unknown")
print("Predicted Category Label:", predicted_category_label)
