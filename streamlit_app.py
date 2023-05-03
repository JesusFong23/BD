import streamlit as st
from PIL import Image

image = Image.open('IMG_5452.JPG')

st.image(image, caption='Sunrise by the mountains')
