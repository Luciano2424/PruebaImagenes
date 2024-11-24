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
def display_logos2(image_path, name, width=100, height=1100):
    img_resized = imagenes_logos(image_path)
    if img_resized:
        st.image(img_resized)
        st.caption(name)  # Esto muestra el nombre debajo de la imagen

# Pirámide logos top1-8
col1, col2, col3 = st.columns([1, 1, 1]) 
with col2:
    display_logos(image_LOUD, "   1 LOUD")

col4, col5, col6 = st.columns([1, 1, 1])  
with col4:
    display_logos(image_OPTC, "   2 OPTC")
with col6:
    display_logos(image_DRX, "   3 DRX")

col7, col8, col9, col10, col11= st.columns([1, 1, 1, 1,1])  
with col7:
    display_logos(image_FPX, "   4 FPX")
with col8:
    display_logos(image_XSET, "   5 XSET")
with col9:
    display_logos(image_FNC, "   6 FNC")
with col10:
    display_logos(image_TL, "   7 TeamLiquid")
with col11:
    display_logos(image_LEV, "   8 Leviatán")
