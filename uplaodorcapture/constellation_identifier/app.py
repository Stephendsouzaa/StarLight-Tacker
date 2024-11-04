from flask import Flask, request, render_template, redirect, url_for
import os
import numpy as np
import cv2
import tensorflow as tf

app = Flask(__name__)

# Load the pre-trained model
model = tf.keras.models.load_model('constellation_model.keras')

# Function to predict the constellation from an image
def predict_constellation(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (224, 224))  # Resize to model's input shape
    img = img / 255.0  # Normalize the image
    img = np.expand_dims(img, axis=0)  # Add batch dimension

    # Make prediction
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction, axis=1)[0]

    # Map predicted class to constellation name
    class_names = ['Andromeda', 'Aquila', 'Auriga', 'CanisMajor', 'Capricornus', 
                   'Cetus', 'Columba', 'Gemini', 'Grus', 'Leo', 'Orion', 
                   'Pavo', 'Pegasus', 'Phoenix', 'Pisces', 'PiscisAustrinus', 
                   'Puppis', 'UrsaMajor', 'UrsaMinor', 'Vela']
    return class_names[predicted_class]

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling image uploads
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' in request.files:
        img = request.files['image']
        
        uploads_dir = os.path.join('static', 'uploads')
        os.makedirs(uploads_dir, exist_ok=True)

        img_path = os.path.join(uploads_dir, img.filename)
        img.save(img_path)

        predicted_constellation = predict_constellation(img_path)
        return render_template('result.html', constellation=predicted_constellation, image=img.filename)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=7000)
