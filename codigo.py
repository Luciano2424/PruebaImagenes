import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

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

def mostrar_grafico2():
    st.subheader("¿Quién es el Rey de las Bajas?")
    st.text("Este gráfico destaca la acumulación de kills de cada jugador a lo largo del torneo. Si estás buscando al jugador con más acción en el campo de batalla, aquí puedes ver quién se lleva la corona de las eliminaciones. ¡El jugador más letal está aquí!")
    plt.figure(figsize=(15, 6))
    kills = df.groupby('Player')['Kill'].mean().sort_values(ascending=False)
    plt.bar(kills.index, kills.values)
    plt.xlabel('Jugador')
    plt.ylabel('Kills')
    plt.title('Jugador con más kills')
    plt.xticks(rotation=45, ha='right')
    st.pyplot() 

def mostrar_grafico3():
    st.subheader("¡Las Muertes también Hablan!")
    st.text("A veces el precio del juego es alto, y este gráfico muestra la cantidad de muertes de cada jugador. Aunque no es lo más positivo, saber quién lidera en esta categoría puede dar pistas sobre el estilo de juego o los desafíos a los que se enfrentan los jugadores. ¡Entérate de quiénes son los más golpeados en el torneo!")
    plt.figure(figsize=(15, 6))
    deaths = df.groupby('Player')['Death'].mean().sort_values(ascending=False)
    plt.bar(deaths.index, deaths.values, color="red")
    plt.xlabel('Jugador')
    plt.ylabel('Muertes')
    plt.title('Jugador con más muertes')
    plt.xticks(rotation=45, ha='right')
    st.pyplot() 

def mostrar_grafico4():
    st.subheader("Equipos Triunfadores: ¿Quién Tiene la Mayor Cantidad de Victorias?")
    st.text("El éxito no solo se mide en kills, sino también en victorias. Este gráfico revela a los equipos que más veces han salido victoriosos durante el torneo, mostrando quién tiene el control total en el campo de juego. ¡Descubre al equipo imbatible de esta edición!")
    plt.figure(figsize=(15, 6))
    victories = df.groupby('Team')['Rounds Win'].mean()
    plt.bar(victories.index, victories.values, color="green")
    plt.xlabel('Equipo')
    plt.ylabel('Victorias')
    plt.title('Equipo con más victorias')
    plt.xticks(rotation="horizontal", ha="center")
    st.pyplot() 

def mostrar_grafico5():
     # Gráfico de Derrotas por equipo
    st.subheader("¿Quién Sufrió Más Derrotas?")
    st.text("Aunque cada derrota es una oportunidad para aprender, algunos equipos han tenido más dificultades que otros. Este gráfico muestra a los equipos con más derrotas, lo que podría reflejar puntos débiles o dificultades para adaptarse al estilo del torneo. ¡Descubre qué equipos tuvieron más trabajo durante la competencia!")
    plt.figure(figsize=(15, 6))
    defeats = df.groupby('Team')['Rounds Lose'].mean()
    plt.bar(defeats.index, defeats.values, color="cyan")
    plt.xlabel('Equipo')
    plt.ylabel('Derrotas')
    plt.title('Equipo con más derrotas')
    plt.xticks(rotation="horizontal", ha="center")
    st.pyplot() 

col1, col2, col3, col4, col5 = st.columns(5)  # Corrección de los parámetros de columnas
# Redirigir con el botón
with col1:
    if st.button("¡Descubre el Poder de los Equipos!"):
        mostrar_grafico()
with col2:
    if st.button("¿Quién es el Rey de las Bajas?"):
        mostrar_grafico2()
with col3:
    if st.button("¡Las Muertes también Hablan!"):
        mostrar_grafico3()
with col4:
    if st.button("¿Quién Tiene la Mayor Cantidad de Victorias?"):
        mostrar_grafico4()
with col5:  # Cambié col4 por col5, ya que el índice col4 ya estaba siendo utilizado.
    if st.button("¿Quién Sufrió Más Derrotas?"):
        mostrar_grafico5()

