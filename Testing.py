import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model # type: ignore
from PIL import Image, ImageOps
import numpy as np

def scale(imag):
    return tf.image.resize(imag, (256,256))

def predict(img, forthemodel):
    resize = scale(img)
    testing = forthemodel.predict(np.expand_dims(resize/255,0))
    return testing

if __name__ == '__main__':
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.title("Smoker Detector AI")
    with st.spinner("Loading the model") :
        model = tf.keras.models.load_model('Smoking_kill_you.h5')

    file = st.file_uploader("Upload a picture", type=["jpg", "png", "jpeg", "gif"])

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