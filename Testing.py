import streamlit as st
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model # type: ignore
from keras import layers
import os
import cv2
from PIL import Image, ImageOps
import numpy as np

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Smoker Detector AI")
def load():
    model = tf.keras.models.load_model('Smoking_kill_you.h5')
    return model

def scale(imag):
    return tf.image.resize(imag, (256,256))

def predict(img, forthemodel):
    resize = scale(img)
    testing = forthemodel.predict(np.expand_dims(resize/255,0))
    return testing

choice = ["Webcam", "Image Upload"]

with st.spinner("Loading the model") :
    model = load()

option = st.selectbox("Choose what Method that to be used", choice)

if option == "Webcam" : 
    file = st.camera_input("Upload a picture")
elif option == "Image Upload" :
    file = st.file_uploader("Upload a picture", type=["jpg", "png", "jpeg"])

if file is None : 
    st.text("Plese upload the image file first")
else :
    with st.spinner("Loading the picture") :
        image = Image.open(file)
        st.image(image, use_column_width=True)
    with st.spinner("Classfying") :
        result = predict(image, model)
    if result > 0.5 :
        string = "The picture shows is Smoking"
    else :
        string = "The picture shows is not Smoking"
    st.success(string)