import streamlit as st
from PIL import Image

image_LEV = "LEV.jpg"

def display_image_with_caption(image_path, caption):
    img_resized = resize_image(image_path)
    st.image(img_resized)

col1, col2, col3 = st.columns([1,2,3])
with col2:
    st.subheader("Leviatan")
    display_image_with_caption(image_LEV)
