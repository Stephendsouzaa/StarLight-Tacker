import argparse
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from sklearn.metrics import accuracy_score

def load_test_data(test_data_path, img_size=(224, 224)):
    # List all images in the test data directory
    images = []
    labels = []
    
    # Assuming the filenames represent the class labels
    class_labels = [
        "Andromeda", "Aquila", "Auriga", "CanisMajor", "Capricornus",
        "Cetus", "Columba", "Gemini", "Grus", "Leo",
        "Orion", "Pavo", "Pegasus", "Phoenix", "Pisces",
        "PiscisAustrinus", "Puppis", "UrsaMajor", "UrsaMinor", "Vela"
    ]

    for filename in os.listdir(test_data_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):  # Check for image files
            # Load and preprocess the image
            img_path = os.path.join(test_data_path, filename)
            img = load_img(img_path, target_size=img_size)
            img_array = img_to_array(img) / 255.0  # Normalize pixel values
            images.append(img_array)
            
            # Extract the label from the filename
            label = filename.split('.')[0]  # Remove the file extension
            labels.append(class_labels.index(label))  # Get the index of the class label

    return np.array(images), np.array(labels)

def evaluate_model(model, X_test, y_test):
    # Evaluate the model on the test data
    predictions = model.predict(X_test)
    predicted_classes = np.argmax(predictions, axis=1)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, predicted_classes)
    print(f'Accuracy: {accuracy:.2f}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', type=str, required=True, help='Path to the trained model file')
    parser.add_argument('--test_data_path', type=str, required=True, help='Path to the test data directory')
    args = parser.parse_args()

    # Load the Keras model
    model = load_model(args.model_path)

    # Load test data
    X_test, y_test = load_test_data(args.test_data_path)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)