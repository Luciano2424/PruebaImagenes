import streamlit as st
from PIL import Image

# Función para mostrar una imagen y actualizar el estado del checkbox simulado
def imagen_checkbox(image_path, label, key):
    # Cargar la imagen
    img = Image.open(image_path)
    
    # Mostrar la imagen
    st.image(img, use_column_width=True, caption=label)
    
    # Cuando se hace clic en la imagen, cambiar el estado
    if st.button(f"Marcar/Desmarcar {label}", key=key):
        if key in st.session_state:
            st.session_state[key] = not st.session_state[key]
        else:
            st.session_state[key] = True

# Definir un estado en la sesión para controlar el checkbox simulado
if "imagen_ANG1_checked" not in st.session_state:
    st.session_state["imagen_ANG1_checked"] = False

# Título
st.title("Simulando un Checkbox con la Imagen ANG1")

# Mostrar la imagen como un "checkbox"
imagen_checkbox("ANG1.jpg", "Imagen ANG1", "imagen_ANG1_checked")

# Mostrar el estado del checkbox simulado
if st.session_state["imagen_ANG1_checked"]:
    st.write("La imagen ANG1 está seleccionada.")
else:
    st.write("La imagen ANG1 no está seleccionada.")
