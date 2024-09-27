# Importamos las bibliotecas necesarias
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Configuramos la página de Streamlit
st.set_page_config(
    page_title="App de predicción",
    page_icon="https://cdn-icons-png.flaticon.com/512/5935/5935638.png",
    layout="centered",
    initial_sidebar_state="auto"
)

# Definimos el título y la descripción de la aplicación
st.title("App de predicción de enfermedades cardíacas")
st.markdown("""
    Esta aplicación predice si tienes una enfermedad cardiaca basándose en tus datos ingresados.
""")

st.markdown("""---""")

# Cargamos y mostramos el logo en la barra lateral
logo = "imagen.png"
st.sidebar.image(logo, width=150)

# Añadimos un encabezado para la sección de datos del usuario en la barra lateral
st.sidebar.header("Datos ingresados por el usuario")

# Permitimos al usuario cargar un archivo CSV o ingresar datos manualmente
uploaded_file = st.sidebar.file_uploader("Cargue su archivo CSV", type=["csv"])

if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    # Definimos una función para capturar las entradas del usuario
    def user_input_features():
        # Creamos controles deslizantes y cuadros de selección para que el usuario ingrese datos
        sbp = st.sidebar.slider("Presión Arterial Sistólica", 101, 218, 150)
        Tabaco = st.sidebar.slider("Tabaco Acumulado (kg)", 0.00, 31.20, 2.00)
        ldl = st.sidebar.slider("Colesterol de Lipoproteínas de Baja Densidad", 0.98, 15.33, 4.34)
        Adiposidad = st.sidebar.slider("Adiposidad", 6.74, 42.49, 26.12)
        Familia = st.sidebar.selectbox("Antecedentes Familiares de Enfermedad Cardiaca", ('Presente', 'Ausente'))
        Tipo = st.sidebar.slider("Tipo", 13, 78, 53)
        Obesidad = st.sidebar.slider("Obesidad", 14.70, 46.58, 25.80)
        Alcohol = st.sidebar.slider("Consumo Actual de Alcohol", 0.00, 147.19, 7.51)
        Edad = st.sidebar.slider('Edad', 15, 64, 45)

        # Creamos un diccionario con los datos ingresados por el usuario
        data = {
            'sbp': sbp,
            'Tabaco': Tabaco,
            'ldl': ldl,
            'Adiposidad': Adiposidad,
            'Familia': Familia,
            'Tipo': Tipo,
            'Obesidad': Obesidad,
            'Alcohol': Alcohol,
            'Edad': Edad
        }

        # Convertimos el diccionario en un DataFrame
        features = pd.DataFrame(data, index=[0])
        return features

    # Si no se carga ningún archivo, usamos las entradas del usuario
    input_df = user_input_features()

# Aplicamos el LabelEncoder para convertir la columna 'Familia' en valores numéricos
encoder = LabelEncoder()
input_df['Familia'] = encoder.fit_transform(input_df['Familia'])

# Seleccionamos solo la primera fila
input_df = input_df[:1]

# Mostramos los datos ingresados por el usuario
st.subheader("Datos ingresados por el usuario")

# Mostramos los datos en la página principal
if uploaded_file is not None:
    st.write(input_df)
else:
    st.write("A la espera de que se cargue el archivo CSV. Actualmente usando parámetros de entrada de ejemplo (que se muestran a continuación).")
    st.write(input_df)

# Cargamos el modelo de clasificación previamente entrenado
load_clf = pickle.load(open('heart.pkl', 'rb'))

# Aplicamos el modelo para realizar predicciones en base a los datos ingresados
prediction = load_clf.predict(input_df)
prediction_proba = load_clf.predict_proba(input_df)

# Creamos dos columnas para mostrar los resultados de predicción
col1, col2 = st.columns(2)

# Mostramos la predicción y las probabilidades en las dos columnas creadas
with col1:
    st.subheader('Predicción')
    st.write(prediction)

with col2:
    st.subheader('Probabilidad de predicción')
    st.write(prediction_proba)

# Mostramos un mensaje personalizado en función de la predicción

# if prediction == 0:
#     st.subheader('La persona no tiene problemas cardíacos')
# else:
#     st.subheader('La persona tiene problemas cardíacos')

# Añadimos una línea divisoria al final
# st.markdown("""---""")

# Agregamos el gráfico de barras con las probabilidades de predicción
st.subheader('Probabilidades de predicción')

# Crear el gráfico de barras con matplotlib
fig, ax = plt.subplots()
ax.bar(['No tiene problemas cardíacos', 'Tiene problemas cardíacos'], prediction_proba[0])
ax.set_ylabel('Probabilidad')
ax.set_ylim(0, 1)  # Asegúrate de que el eje y vaya de 0 a 1

# Mostrar el gráfico en la aplicación
st.pyplot(fig)

# Mostramos un mensaje personalizado en función de la predicción
if prediction == 0:
    st.subheader('La persona no tiene problemas cardíacos')
else:
    st.subheader('La persona tiene problemas cardíacos')

# Añadimos una línea divisoria al final
st.markdown("""---""")