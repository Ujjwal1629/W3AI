import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd

# Example data
data = pd.read_csv('data.csv')
X = data['features']
y = data['labels']

# Define the model
model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(X.shape[1],)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=10, batch_size=32)