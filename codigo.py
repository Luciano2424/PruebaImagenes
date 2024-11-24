import streamlit as st
from PIL import Image

# Función para redimensionar la imagen
def imagenes_logos(image_path, width=200, height=200):
    try:
        img = Image.open(image_path)
        img_resized = img.resize((width, height))
        return img_resized
    except Exception as e:
        st.error(f"Error al cargar la imagen {image_path}: {e}")
        return None

# Rutas de las imágenes
image_LEV = "LEV.jpg"
image_DRX = "DRX.jpg"
image_XSET = "XSET.jpg"
image_FNC = "FNC.jpg"
image_FPX = "FPX.jpg"
image_OPTC = "OPTC.jpg"
image_TL = "TL.jpg"
image_LOUD = "LOUD.jpg"

# Función para mostrar la imagen
def display_logos(image_path):
    img_resized = imagenes_logos(image_path)
    if img_resized:
        st.image(img_resized)

# Pirámide logos top1-8
col1, col2, col3 = st.columns([1, 1, 1]) 
with col2:
    display_logos(image_LOUD)

col4, col5, col6 = st.columns([1, 1, 1])  
with col4:
    display_logos(image_OPTC)
with col6:
    display_logos(image_DRX)

col7, col8, col9, col10 = st.columns([1, 1, 1, 1])  
with col7:
    display_logos(image_FPX)
with col8:
    display_logos(image_XSET)
with col9:
    display_logos(image_TL)
with col10:
    display_logos(image_LEV)
