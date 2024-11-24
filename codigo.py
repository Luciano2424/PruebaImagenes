import streamlit as st
from PIL import Image
import os

# Verificar si la imagen existe
if os.path.exists("imagenes/ANGE1.jpg"):
    st.write("La imagen ANGE1.jpg fue encontrada.")
else:
    st.write("No se encontró la imagen ANGE1.jpg. Asegúrate de que esté en el directorio correcto.")

# Función para mostrar una imagen y actualizar el estado del checkbox
def imagen_checkbox(image_path, label, key):
    # Cargar la imagen
    img = Image.open(image_path)
    
    # Mostrar la imagen
    st.image(img, use_column_width=True, caption=label)
    
    # Usar un checkbox para marcar/desmarcar la selección
    checked = st.checkbox(f"Marcar/Desmarcar {label}", key=key)
    
    # Cambiar el estado de la sesión con el checkbox
    if checked:
        st.session_state[key] = True
    else:
        st.session_state[key] = False

# Asegurarse de que el estado existe en la sesión
if "imagen_ANGE1_checked" not in st.session_state:
    st.session_state["imagen_ANGE1_checked"] = False

# Título
st.title("Simulando un Checkbox con la Imagen ANGE1")

# Mostrar la imagen como un "checkbox"
imagen_checkbox("imagenes/ANGE1.jpg", "Imagen ANGE1", "imagen_ANGE1_checked")

# Mostrar el estado del checkbox simulado
if st.session_state["imagen_ANGE1_checked"]:
    st.write("La imagen ANGE1 está seleccionada.")
else:
    st.write("La imagen ANGE1 no está seleccionada.")
