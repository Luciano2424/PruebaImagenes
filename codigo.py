import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Asegúrate de que el DataFrame df esté cargado
# df = pd.read_csv("valorant champions istanbul.csv")  # Este es el CSV de tu DataFrame

# Gráfico de KD/Rendimiento
st.subheader("K/D Promedio por Equipo")
plt.figure(figsize=(10, 6))
kd = df.groupby('Team')['K/D'].mean().sort_values(ascending=False)
plt.bar(kd.index, kd.values, color="purple")
plt.xlabel('Equipo')
plt.ylabel('Promedio K/D')
plt.title('K/D promedio por equipo')
plt.xticks(rotation="horizontal", ha='right')
st.pyplot()  # Muestra el gráfico en Streamlit

# Gráfico de kills
st.subheader("Jugador con Más Kills")
plt.figure(figsize=(15, 6))
kills = df.groupby('Player')['Kill'].mean().sort_values(ascending=False)
plt.bar(kills.index, kills.values)
plt.xlabel('Jugador')
plt.ylabel('Kills')
plt.title('Jugador con más kills')
plt.xticks(rotation=45, ha='right')
st.pyplot()  # Muestra el gráfico en Streamlit

# Gráfico de Muertes
st.subheader("Jugador con Más Muertes")
plt.figure(figsize=(15, 6))
deaths = df.groupby('Player')['Death'].mean().sort_values(ascending=False)
plt.bar(deaths.index, deaths.values, color="red")
plt.xlabel('Jugador')
plt.ylabel('Muertes')
plt.title('Jugador con más muertes')
plt.xticks(rotation=45, ha='right')
st.pyplot()  # Muestra el gráfico en Streamlit

# Gráfico de Victorias por equipo
st.subheader("Equipo con Más Victorias")
plt.figure(figsize=(15, 6))
victories = df.groupby('Team')['Rounds Win'].mean()
plt.bar(victories.index, victories.values, color="green")
plt.xlabel('Equipo')
plt.ylabel('Victorias')
plt.title('Equipo con más victorias')
plt.xticks(rotation="horizontal", ha="center")
st.pyplot()  # Muestra el gráfico en Streamlit

# Gráfico de Derrotas por equipo
st.subheader("Equipo con Más Derrotas")
plt.figure(figsize=(15, 6))
defeats = df.groupby('Team')['Rounds Lose'].mean()
plt.bar(defeats.index, defeats.values, color="cyan")
plt.xlabel('Equipo')
plt.ylabel('Derrotas')
plt.title('Equipo con más derrotas')
plt.xticks(rotation="horizontal", ha="center")
st.pyplot()  # Muestra el gráfico en Streamlit
