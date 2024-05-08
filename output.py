import streamlit as st
from PIL import Image

def output():
    return "Hello World"

def out(number):
    if number == 1 :
        return "Hi"
    else :
        return "World"

if __name__ == '__main__':
    st.set_option('deprecation.showfileUploaderEncoding', False)
    word = output()
    st.header(word)
    file = st.file_uploader("Upload Image")
    if file is None : 
        st.text("Plese upload the image file first")
    else :
        image = Image.open(file)
        st.image(image, use_column_width=True)
