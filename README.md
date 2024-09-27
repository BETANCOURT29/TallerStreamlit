# Predicción de Enfermedades Cardíacas con Streamlit

Esta aplicación permite predecir si una persona tiene una enfermedad cardíaca basándose en un conjunto de datos ingresados por el usuario. La predicción se realiza utilizando un modelo de **RandomForest**.

## Características

- **Formulario interactivo**: Permite a los usuarios ingresar datos manualmente utilizando deslizadores y cuadros de selección.
- **Carga de archivo CSV**: Los usuarios pueden cargar un archivo CSV con datos y obtener la predicción.
- **Visualización de resultados**: Muestra si una persona tiene o no una enfermedad cardíaca y la probabilidad asociada.
- **Gráfico de compatibilidad**: Visualiza los resultados de compatibilidad basados en los datos proporcionados.

## Instalación y Configuración

Sigue estos pasos para ejecutar la aplicación en tu máquina local:

### 1. Clonar el Repositorio

Primero, clona el repositorio en tu máquina local:

    git clone https://github.com/tu-usuario/taller-streamlit-app.git
    cd taller-streamlit-app

### 2. Crear y Activar un Entorno Virtual

Para mantener las dependencias organizadas, debes crear un entorno virtual.

**Crear el entorno virtual**:

Ejecuta el siguiente comando para crear un entorno virtual llamado `streamlit-entorno`:

    python -m venv streamlit-entorno

**Activar el entorno virtual**:

Luego, debes activar el entorno virtual. Usa el comando correspondiente a tu sistema operativo:

**Windows**:

    streamlit-entorno\Scripts\activate

**macOS/Linux**:

    source streamlit-entorno/bin/activate

### 3. Instalar Dependencias

Una vez que el entorno virtual esté activado, instala las dependencias necesarias utilizando el archivo `requirements.txt`:

    pip install -r requirements.txt

### 4. Ejecutar la Aplicación

Para ejecutar la aplicación de Streamlit, utiliza el siguiente comando:

    streamlit run app.py

Esto abrirá la aplicación en tu navegador, donde podrás interactuar con los datos y ver los resultados.

## Estructura del Proyecto

      📁 taller-streamlit-app/
      │
      ├── 📄 app_streamlit.py          # Aplicación principal en Streamlit
      ├── 📄 modelo.py                 # Entrenamiento y serialización del modelo RandomForest (genera 'heart.pkl')
      ├── 📄 heart.csv                 # Dataset original para entrenar el modelo
      ├── 📄 datos_nuevos.csv          # Datos nuevos para predicciones
      ├── 📄 heart.pkl                 # Modelo entrenado guardado en formato pickle
      ├── 📄 requirements.txt          # Lista de dependencias necesarias para ejecutar la aplicación


## Uso de la Aplicación

### Ingresar datos manualmente:

Utiliza los deslizadores y las selecciones en la barra lateral para ingresar datos como la presión arterial, consumo de tabaco, niveles de colesterol, etc.

### Subir un archivo CSV:

Carga un archivo CSV con datos de pacientes para realizar predicciones en bloque.

### Ver predicciones:

La aplicación mostrará si la persona tiene problemas cardíacos y la probabilidad de dicha condición.

## Dataset

El dataset utilizado para entrenar el modelo está compuesto por varios factores como:

- Presión arterial sistólica
- Consumo de tabaco
- Niveles de colesterol
- Adiposidad
- Antecedentes familiares de enfermedad cardíaca
- Edad, entre otros.


¡Gracias por revisar este proyecto!
