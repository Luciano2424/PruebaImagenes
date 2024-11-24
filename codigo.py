import streamlit as st
import pandas as pd

df = pd.read_csv("valorant champions istanbul.csv")

# Gráfico de KD/Rendimiento
plt.figure(figsize=(10, 6))
kd = df.groupby('Team')['K/D'].mean().sort_values(ascending=False)
plt.bar(kd.index, kd.values, color="purple")
plt.xlabel('Equipo')
plt.ylabel('Promedio K/D')
plt.title('K/D promedio por equipo')
plt.xticks(rotation="horizontal", ha='right')
plt.show()

# Gráfico de kills
plt.figure(figsize=(15, 6))
kills = df.groupby('Player')['Kill'].mean().sort_values(ascending=False)
plt.bar(kills.index, kills.values)
plt.xlabel('Jugador')
plt.ylabel('Kills')
plt.title('Jugador con más kills')
plt.xticks(rotation=45, ha='right')
plt.show()

# Gráfico de Muertes
plt.figure(figsize=(15, 6))
deaths = df.groupby('Player')['Death'].mean().sort_values(ascending=False)
plt.bar(deaths.index, deaths.values, color="red")
plt.xlabel('Jugador')
plt.ylabel('Muertes')
plt.title('Jugador con más muertes')
plt.xticks(rotation=45, ha='right')
plt.show()

# Gráfico de Victorias por equipo
plt.figure(figsize=(15, 6))
victories = df.groupby('Team')['Rounds Win'].mean()
plt.bar(victories.index, victories.values, color="green")
plt.xlabel('Equipo')
plt.ylabel('Victorias')
plt.title('Equipo con más victorias')
plt.xticks(rotation="horizontal", ha="center")
plt.show()

# Gráfico de Derrotas por equipo
plt.figure(figsize=(15, 6))
defeats = df.groupby('Team')['Rounds Lose'].mean()
plt.bar(defeats.index, defeats.values, color="cyan")
plt.xlabel('Equipo')
plt.ylabel('Derrotas')
plt.title('Equipo con más derrotas')
plt.xticks(rotation="horizontal", ha="center")
plt.show()
