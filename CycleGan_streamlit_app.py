# use  streamlit run app.py --server.enableXsrfProtection=false

import streamlit as st
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tensorflow_addons.layers import InstanceNormalization

def load_image(image_file):
    img = Image.open(image_file)
    return img

def show_image(image, title):
    st.image(image, caption=title, use_column_width=True)

def load_model(model_path):
    return tf.keras.models.load_model(model_path, custom_objects={'InstanceNormalization': InstanceNormalization})

def predict_and_show(model, image):
    image = image.resize((128, 128))
    image_array = np.array(image)
    image_array = image_array / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    pred = model.predict(image_array)[0]
    pred = (pred * 255).astype(np.uint8)
    pred_image = Image.fromarray(pred)
    return pred_image

st.title("CycleGAN Style Transfer")

# Upload image
uploaded_file = st.file_uploader("Choose a celebrity image...", type="jpg")

# Model selection
model_options = {
    "Van Gogh Style": "van_5.23/Generator_Celebrity_to_Style.h5",
    "Cartoon Style": "cartoon_5.23/Generator_Celebrity_to_Style.h5",
    "Sketch Style": "sketch_5.23/Generator_Celebrity_to_Style.h5"
}
selected_model = st.selectbox("Choose a style transfer model", list(model_options.keys()))

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    img = load_image(uploaded_file)
    
    if st.button("Generate Style Transferred Image"):
        model_path = model_options[selected_model]
        model = load_model(model_path)
        pred_image = predict_and_show(model, img)
        
        st.image(pred_image, caption='Style Transferred Image', use_column_width=True)
