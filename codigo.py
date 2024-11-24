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

def imagenes_logos2(image_path, width=100, height=100):
    img = Image.open(image_path)
    img_resized = img.resize((width, height))
    return img_resized
    
def display_58(image_path):
    img_reasized = imagenes_logos2(image_path)
    st.image(img_resized)


#Piramide logos top1-8
col1, col2, col3 = st.columns([1, 1, 1]) 
with col2:
    display_logos(image_LOUD)

col4, col5, col6 = st.columns([1, 1, 1])  
with col4:
    display_logos(image_OPTC)
with col6:
    display_logos(image_DRX)

col7, col8, col9, col10= st.columns([1, 1, 1, 1])  
with col7:
    display_logos2(image_FPX)
with col8:
    display_logos2(image_XSET)
with col9:
    display_logos2(image_TL)
with col10:
    display_logos2(image_LEV)

