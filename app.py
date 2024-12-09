
import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

class ImageClassifier:
    def __init__(self):
        # Load pre-trained ResNet50 model
        self.model = ResNet50(weights='imagenet')

    def classify_image(self, pil_image, top_k=5):
        """
        Classify a PIL image using pre-trained ResNet50 model
        
        Args:
            pil_image (PIL.Image): Input image
            top_k (int): Number of top predictions to return
        
        Returns:
            list: Top k predictions with class names and confidence scores
        """
        # Resize and preprocess image
        img = pil_image.resize((224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Make prediction
        predictions = self.model.predict(img_array)
        
        # Decode and return top predictions
        return decode_predictions(predictions, top=top_k)[0]

def main():
    # Initialize classifier
    classifier = ImageClassifier()

    # Streamlit app configuration
    st.title('Image Classification App')
    st.write('Upload an image to get its top 5 predictions')

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Classify image
        try:
            predictions = classifier.classify_image(image)

            # Display predictions
            st.subheader('Top 5 Predictions:')
            for (imagenet_id, label, score) in predictions:
                st.write(f"{label.capitalize()}: {score * 100:.2f}%")

        except Exception as e:
            st.error(f"Error classifying image: {e}")

if __name__ == "__main__":
    main()
