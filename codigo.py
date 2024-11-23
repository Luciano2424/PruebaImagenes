import streamlit as st
 
## Define las opciones
options = ['Opción 1', 'Opción 2', 'Opción 3']
 
## Crea la caja de selección
selected_option = st.selectbox('Elige una opción:', options)
 
## Muestra la opción seleccionada
st.write('Seleccionaste:', selected_option)
