import streamlit as st
from PIL import Image

image_LEV = "LEV.jpg"

col1, col2, col3 = st.columns([1,2,3])
with col2:
    st.subhead("Leviatan")
    display_image_with_caption(image_Lev)
