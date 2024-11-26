import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv("valorant champions istanbul.csv")

# Función que muestra el gráfico
def mostrar_grafico():
    st.subheader("¡Descubre el Poder de los Equipos!")
    st.text("Este gráfico muestra cómo se desempeñan los equipos en cuanto a su ratio de Kills/Deaths (K/D). Los equipos con el mejor desempeño suelen tener una mayor proporción de muertes por baja, lo que refleja una ejecución más eficiente en el juego. ¡Ve quién lidera el torneo en rendimiento!")
    
    # Gráfico
    plt.figure(figsize=(10, 6))
    kd = df.groupby('Team')['K/D'].mean().sort_values(ascending=False)  # Asegúrate de tener el dataframe 'df' cargado
    plt.bar(kd.index, kd.values, color="purple")
    plt.xlabel('Equipo')
    plt.ylabel('Promedio K/D')
    plt.title('K/D promedio por equipo')
    plt.xticks(rotation="horizontal", ha='right')
    st.pyplot()

# Redirigir con el botón
if st.button('Ver gráfico de K/D promedio'):
    mostrar_grafico()
