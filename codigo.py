import streamlit as st

# Título de la página
st.title("Botón de selección en Streamlit")

# Crear el grupo de botones de selección
opcion_seleccionada = st.radio(
    "Selecciona una opción",  # Etiqueta
    ("Opción 1", "Opción 2", "Opción 3")  # Opciones
)

# Mostrar la opción seleccionada
st.write(f"Has seleccionado: {opcion_seleccionada}")
