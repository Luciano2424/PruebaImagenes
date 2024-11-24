import streamlit as st
import pandas as pd
from PIL import Image  
import matplotlib.pyplot as plt

df = pd.read_csv("valorant champions istanbul.csv")

# Rutas de las imágenes
image_yay = "yay.jpeg"
image_Cryocells = "Cryocells.jpg"
image_ANGE1 = "ANGE1.jpg"
image_Derke = "Derke.jpg"
image_MaKo = "MaKo.jpg"
image_Scream = "Scream.jpg"
image_kiNgg = "kiNgg.jpg"
image_suygetsu = "suygetsu.jpg"
image_Less = "Less.jpeg"
image_LEV = "LEV.jpg"
image_DRX = "DRX.jpg"
image_XSET = "XSET.jpg"
image_FNC = "FNC.jpg"
image_FPX = "FPX.jpg"
image_OPTC = "OPTC.jpg"
image_TL = "TL.jpg"
image_LOUD = "LOUD.jpg"

# Funciones para mostrar datos específicos
def mejor_rendimiento():
    filas_seleccionadas = df.iloc[[5]]  
    st.dataframe(filas_seleccionadas)

def peor_rendimiento():
    filas_seleccionadas = df.iloc[[19]]  
    st.dataframe(filas_seleccionadas)

def mas_kills():
    filas_seleccionadas = df.iloc[[5]]  
    st.dataframe(filas_seleccionadas)

def mejor_rendimiento_por_equipo():
    filas_seleccionadas = df.iloc[[3, 5, 10, 17, 22, 25, 32, 35]]  
    st.dataframe(filas_seleccionadas)

# Aseguramos que "page" esté en el estado de sesión
if "page" not in st.session_state:
    st.session_state.page = "home"

# Función para redimensionar imágenes
def resize_image(image_path, width=130, height=152):
    img = Image.open(image_path)  
    img_resized = img.resize((width, height))  
    return img_resized

# Función para mostrar imágenes con su título
def display_image_with_caption(image_path, caption):
    img_resized = resize_image(image_path)
    st.image(img_resized)
    st.markdown(
        f"""
        <style>
        .caption {{
            font-family: 'Arial Black', sans-serif;
            font-size: 15px;
            font-weight: bold;
        }}
        </style>
        <p class="caption">{caption}</p>
        """, unsafe_allow_html=True
    )

# Definir display_logo() como una función alternativa, si es necesario
def display_logo(image_path, caption):
    display_image_with_caption(image_path, caption)  # Usa la función ya definida

# Lógica de la aplicación principal
if st.session_state.page == "home":  
    st.title("Datos que creemos te gustarán saber")
    
    # URL del video de YouTube
    video_presentación_ = "https://www.youtube.com/watch?v=j2Z4qYJ3Jtc&ab_channel=VALORANTChampionsTour"
    st.video(video_presentación_)

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.subheader("Presentación de los equipos participantes del torneo")

    # Mostrar logos de los equipos
    col1, col2, col3 = st.columns([1, 1, 1]) 
    with col2:
        display_logo(image_LOUD, "1 LOUD")

    col4, col5, col6 = st.columns([1, 1, 1])  
    with col4:
        display_logo(image_OPTC, "2 OPTC")
    with col6:
        display_logo(image_DRX, "3 DRX")

    col7, col8, col9, col10, col11 = st.columns([1, 1, 1, 1, 1])  
    with col7:
        display_logo(image_FPX, "4 FPX")
    with col8:
        display_logo(image_XSET, "5 XSET")
    with col9:
        display_logo(image_FNC, "6 FNC")
    with col10:
        display_logo(image_TL, "7 TeamLiquid")
    with col11:
        display_logo(image_LEV, "8 Leviatán")

    col1, col2, col3 = st.columns([1, 3, 1])  

    with col2:
        st.subheader("Presentación de los equipos participantes del torneo")
        page_selection = st.selectbox(
            "Datos que creemos te gustarán saber",
            ["Ház click para desplegar las opciones", 
             "Cuál fue el jugador con mejor rendimiento global del torneo", 
             "Cuál fue el jugador con peor rendimiento global del torneo", 
             "Cuál fue el jugador con más kills?", 
             "Cuáles fueron los jugadores con mejor rendimiento de cada equipo?"]
        )

        if page_selection == "Cuál fue el jugador con mejor rendimiento global del torneo":
            st.session_state.page = "mejor_rendimiento"
        elif page_selection == "Cuál fue el jugador con peor rendimiento global del torneo":
            st.session_state.page = "peor_rendimiento"
        elif page_selection == "Cuál fue el jugador con más kills?":
            st.session_state.page = "mas_kills"
        elif page_selection == "Cuáles fueron los jugadores con mejor rendimiento de cada equipo?":
            st.session_state.page = "mejor_rendimiento_por_equipo"

    st.subheader("Mejores momentos del torneo")

    st.subheader("¡Descubre el Poder de los Equipos!")
    st.text("Este gráfico muestra cómo se desempeñan los equipos en cuanto a su ratio de Kills/Deaths (K/D)...")
    plt.figure(figsize=(10, 6))
    kd = df.groupby('Team')['K/D'].mean().sort_values(ascending=False)
    plt.bar(kd.index, kd.values, color="purple")
    plt.xlabel('Equipo')
    plt.ylabel('Promedio K/D')
    plt.title('K/D promedio por equipo')
    plt.xticks(rotation="horizontal", ha='right')
    st.pyplot()

    # Gráfico de kills
    st.subheader("¿Quién es el Rey de las Bajas?")
    st.text("Este gráfico destaca la acumulación de kills de cada jugador...")
    plt.figure(figsize=(15, 6))
    kills = df.groupby('Player')['Kill'].mean().sort_values(ascending=False)
    plt.bar(kills.index, kills.values)
    plt.xlabel('Jugador')
    plt.ylabel('Kills')
    plt.title('Jugador con más kills')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()

    # Gráfico de KD/Rendimiento
    st.subheader("¡Descubre el Poder de los Equipos!")
    st.text("Este gráfico muestra cómo se desempeñan los equipos en cuanto a su ratio de Kills/Deaths (K/D)...")
    plt.figure(figsize=(10, 6))
    kd = df.groupby('Team')['K/D'].mean().sort_values(ascending=False)
    plt.bar(kd.index, kd.values, color="purple")
    plt.xlabel('Equipo')
    plt.ylabel('Promedio K/D')
    plt.title('K/D promedio por equipo')
    plt.xticks(rotation="horizontal", ha='right')
    st.pyplot()  # Muestra el gráfico en Streamlit

    # Gráfico de kills
    st.subheader("¿Quién es el Rey de las Bajas?")
    st.text("Este gráfico destaca la acumulación de kills de cada jugador a lo largo del torneo...")
    plt.figure(figsize=(15, 6))
    kills = df.groupby('Player')['Kill'].mean().sort_values(ascending=False)
    plt.bar(kills.index, kills.values)
    plt.xlabel('Jugador')
    plt.ylabel('Kills')
    plt.title('Jugador con más kills')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()  # Muestra el gráfico en Streamlit

    # Gráfico de Muertes
    st.subheader("¡Las Muertes también Hablan!")
    st.text("A veces el precio del juego es alto...")
    plt.figure(figsize=(15, 6))
    deaths = df.groupby('Player')['Death'].mean().sort_values(ascending=False)
    plt.bar(deaths.index, deaths.values, color="red")
    plt.xlabel('Jugador')
    plt.ylabel('Muertes')
    plt.title('Jugador con más muertes')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()  # Muestra el gráfico en Streamlit

    # Gráfico de Victorias por equipo
    st.subheader("Equipos Triunfadores: ¿Quién Tiene la Mayor Cantidad de Victorias?")
    st.text("Este gráfico revela a los equipos que más veces han salido victoriosos...")
    plt.figure(figsize=(15, 6))
    victories = df.groupby('Team')['Rounds Win'].mean()
    plt.bar(victories.index, victories.values, color="green")
    plt.xlabel('Equipo')
    plt.ylabel('Victorias')
    plt.title('Equipo con más victorias')
    plt.xticks(rotation="horizontal", ha="center")
    st.pyplot()  # Muestra el gráfico en Streamlit

    # Gráfico de puntos
    st.subheader("Jugadores más destacados por puntos")
    st.text("¿Quién está acaparando la atención? El gráfico muestra quién tiene más puntos...")
    plt.figure(figsize=(10, 6))
    points = df.groupby('Player')['Points'].mean()
    plt.bar(points.index, points.values, color="blue")
    plt.xlabel('Jugador')
    plt.ylabel('Puntos')
    plt.title('Jugador con más puntos')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()
