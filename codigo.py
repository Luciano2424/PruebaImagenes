import streamlit as st
from PIL import Image

# Definir la función resize_image para cambiar el tamaño de la imagen
def resize_image(image_path, width=100, height=100):
    img = Image.open(image_path)
    img_resized = img.resize((width, height))
    return img_resized

# Ruta de la imagen
image_LEV = "LEV.jpg"

# Función para mostrar la imagen con el título/captura
def display_image_with_caption(image_path, caption):
    img_resized = resize_image(image_path)
    st.image(img_resized)
    st.markdown(f"**{caption}**", unsafe_allow_html=True)

# Diseño en columnas
col1, col2, col3 = st.columns([1, 2, 1])  # Columnas centradas: el medio más ancho

# Mostrar la imagen en el centro de la columna 2
with col2:
    st.subheader("Leviatan")  # Subtítulo
    display_image_with_caption(image_LEV, "Equipo Leviatan")  # Imagen y título
