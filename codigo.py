import streamlit as st
from PIL import Image

# Función para mostrar la imagen dentro de un 'expander' (showbox)
def showbox_with_image(image_path, label):
    # Cargar la imagen
    img = Image.open(image_path)
    
    # Crear un expander (showbox) con el título de la imagen
    with st.expander(label):
        # Mostrar la imagen dentro del expander
        st.image(img, use_column_width=True)

# Título de la aplicación
st.title("Showbox con Imagen en Streamlit")

# Llamada a la función para mostrar la imagen en un expander
showbox_with_image("ANGE1.jpg", "Haz clic para ver la imagen ANGE1")

