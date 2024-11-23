import streamlit as st
 
option = st.selectbox(
    '¿Cómo te gustaría ser contactado?',
    ('Correo electrónico', 'Teléfono de casa', 'Teléfono móvil')
)
st.write('Seleccionaste:', option)
