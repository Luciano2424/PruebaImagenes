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

# Función para mostrar la imagen con su nombre
def display_logos(image_path, name):
    img_resized = imagenes_logos(image_path)
    if img_resized:
        st.image(img_resized)
        st.caption(name)  # Esto muestra el nombre debajo de la imagen

# Pirámide logos top1-8
col1, col2, col3 = st.columns([1, 1, 1]) 
with col2:
    display_logos(image_LOUD, "LOUD")

col4, col5, col6 = st.columns([1, 1, 1])  
with col4:
    display_logos(image_OPTC, "OPTC")
with col6:
    display_logos(image_DRX, "DRX")

col7, col8, col9, col10 = st.columns([1, 1, 1, 1])  
with col7:
    display_logos(image_FPX, "FPX")
with col8:
    display_logos(image_XSET, "XSET")
with col9:
    display_logos(image_TL, "TeamLiquid")
with col10:
    display_logos(image_LEV, "Leviatán")
