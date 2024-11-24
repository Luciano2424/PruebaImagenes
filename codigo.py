import streamlit as st
from PIL import Image

# Definir la función para redimensionar la imagen
def imagenes_logos(image_path, width=200, height=200):
    img = Image.open(image_path)
    img_resized = img.resize((width, height))
    return img_resized

# Ruta de la imagen
image_LEV = "LEV.jpg"
image_DRX = "DRX.jpg"
image_XSET = "XSET.jpg"
image_FNC = "FNC.jpg"
iage_FPX = "FPX.jpg"
image_OPTC = "OPTC.jpg"
image_LOUD = "LOUD.jpg"
image_TL ="TL.jpg"

# Función para mostrar la imagen
def display_logos(image_path):
    img_resized = imagenes_logos(image_path)
    st.image(img_resized)

# Diseño piramidal
col1, col2, col3 = st.columns([1, 1, 1])  # Primera fila de 3 columnas
with col2:
    display_logos(image_LOUD)

# Segunda fila (2 imágenes)
col4, col5, col6 = st.columns([1, 1, 1])  # Segunda fila de 3 columnas
with col4:
    display_logos(image_OPTC)
with col6:
    display_logos(image_LEV)

# Tercera fila (3 imágenes)
col7, col8, col9 = st.columns([1, 1, 1])  # Tercera fila de 3 columnas
with col7:
    display_logos(image_LEV)
with col8:
    display_logos(image_LEV)
with col9:
    display_logos(image_LEV)
