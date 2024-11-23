import streamlit as st
from PIL import Image

# Cargar la imagen
image_ANGE1 = "ANGE1.jpg"
img = Image.open(image_ANGE1)

# Redimensionar la imagen a 113x152 píxeles (aproximadamente 3cm x 4cm)
img_resized = img.resize((113, 152))

# Mostrar la imagen redimensionada
st.image(img_resized)
