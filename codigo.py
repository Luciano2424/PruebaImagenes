import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

# Cargar el DataFrame
df = pd.read_csv("valorant champions istanbul.csv")

# Rutas de imágenes
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

# Función para redimensionar imágenes
def resize_image(image_path, width=130, height=152):
    img = Image.open(image_path)
    img_resized = img.resize((width, height))
    return img_resized

# Función para mostrar la imagen con su nombre
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

# Función para mostrar los logos de los equipos
def display_logo(image_path, name, width=100, height=100):
    img_resized = resize_image(image_path, width, height)
    st.image(img_resized)
    st.caption(name)

# Inicialización de página en sesión de estado
if "page" not in st.session_state:
    st.session_state.page = "home"

# Función para mostrar gráficos de desempeño por jugador
def plot_performance(df, column, title, xlabel, ylabel, color="blue"):
    plt.figure(figsize=(15, 6))
    stats = df.groupby('Player')[column].mean().sort_values(ascending=False)
    plt.bar(stats.index, stats.values, color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    st.pyplot()

# Mostrar la página de inicio
if st.session_state.page == "home":
    st.title("Análisis y Estadísticas del VCT Masters Reykjavik 2022")
    st.video("https://www.youtube.com/watch?v=j2Z4qYJ3Jtc&ab_channel=VALORANTChampionsTour")

    col1, col2, col3 = st.columns([1, 3, 1])  
    with col2:
        st.subheader("Presentación de los equipos participantes del torneo")

    # Mostrar logos de los equipos
    display_logo(image_LOUD, "LOUD", 100, 100)
    display_logo(image_OPTC, "OPTC", 100, 100)
    display_logo(image_DRX, "DRX", 100, 100)
    display_logo(image_FPX, "FPX", 100, 100)
    display_logo(image_XSET, "XSET", 100, 100)
    display_logo(image_FNC, "FNC", 100, 100)
    display_logo(image_TL, "Team Liquid", 100, 100)
    display_logo(image_LEV, "Leviatán", 100, 100)

    # Selección de equipo para mostrar más detalles
    paginas_equipos = st.selectbox("¿Qué equipo te gustaría ver?", 
                                   ["Selecciona el equipo", "LOUD", "OPTC", "DRX", "FPX", "XSET", "FNC", "TL", "LEV"])
    
    if paginas_equipos != "Selecciona el equipo":
        st.session_state.page = f"{paginas_equipos}_page"

    # Mostrar gráficos
    plot_performance(df, "Kill", "Jugador con más kills", "Jugador", "Kills", "green")
    plot_performance(df, "K/D", "K/D promedio por equipo", "Equipo", "K/D", "purple")

# Otras páginas según la selección
elif st.session_state.page == "LOUD_page":
    st.title("Página de LOUD")
    st.video("https://www.youtube.com/watch?v=CSyGWW305M8&ab_channel=LOUDVALORANT")
    display_image_with_caption(image_Less, "Less Top 1")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

# Repite el bloque de páginas para OPTC, DRX, etc.

# Si seleccionaron una página de estadística
elif st.session_state.page == "mejor_rendimiento":
    st.title("Jugador con mejor rendimiento")
    mejor_rendimiento()  # Aquí la función para mostrar estadísticas
    display_image_with_caption(image_yay, "Presentación yay")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"
