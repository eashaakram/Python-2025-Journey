from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.utils import to_categorical

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

# Load dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print("Dataset Loaded Successfully!")
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 4))

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(y_train[i])
    plt.axis('off')

plt.tight_layout()
plt.show()

# Normalize
x_train = x_train / 255.0
x_test = x_test / 255.0

# One hot encoding
y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)

# Build model
model = Sequential()

model.add(Flatten(input_shape=(28,28)))
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compile
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train
history = model.fit(
    x_train, y_train_cat, epochs=5, validation_split=0.1, verbose=1
)

# Evaluate Model
loss, accuracy = model.evaluate(
    x_test,
    y_test_cat,
    verbose=0
)

print("\n==============================")
print(f"Test Accuracy : {accuracy * 100:.2f}%")
print(f"Test Loss     : {loss:.4f}")
print("==============================")

# Accuracy & Loss Graphs
plt.figure(figsize=(12, 5))


# Accuracy & Loss Graphs
plt.figure(figsize=(12, 5))

# Accuracy Graph
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Accuracy Graph')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

# Loss Graph
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss Graph')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()

# Predictions
y_pred = model.predict(x_test, verbose=0)

y_pred_classes = np.argmax(y_pred, axis=1)
y_true = y_test

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred_classes)

plt.figure(figsize=(8, 6))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues'
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")

plt.show()

# Classification Report
print("\nClassification Report:\n")

print(
    classification_report(
        y_true,
        y_pred_classes
    )
)

# Random Prediction Test
random_index = np.random.randint(0, len(x_test))

sample_image = x_test[random_index]

prediction = model.predict(
    sample_image.reshape(1, 28, 28),
    verbose=0
)

predicted_digit = np.argmax(prediction)
actual_digit = y_true[random_index]

confidence = np.max(prediction) * 100

plt.figure(figsize=(4, 4))
plt.imshow(sample_image, cmap='gray')

plt.title(
    f"Actual: {actual_digit}\n"
    f"Predicted: {predicted_digit}\n"
    f"Confidence: {confidence:.2f}%"
)

plt.axis('off')
plt.show()

print("\nRandom Prediction Test")
print("----------------------")
print("Actual Digit    :", actual_digit)
print("Predicted Digit :", predicted_digit)
print(f"Confidence      : {confidence:.2f}%")

# Save model
model.save("bestmodel.h5")

print("\nModel saved successfully as bestmodel.h5")

