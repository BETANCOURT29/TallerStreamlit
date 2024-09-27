# Taller de Streamlit - Presentación y Ejercicios

Este repositorio contiene una presentación sobre Streamlit, sus características, ventajas y limitaciones. Además, incluye dos ejercicios prácticos que muestran cómo utilizar Streamlit para crear aplicaciones interactivas con modelos de Machine Learning.

## 🌟 ¿Qué es Streamlit?

Streamlit es una herramienta de código abierto que permite crear aplicaciones web interactivas para proyectos de Machine Learning y Data Science de una manera sencilla y rápida. Con solo unas pocas líneas de código, puedes transformar tus scripts de Python en aplicaciones web completas, listas para ser utilizadas por usuarios no técnicos.

## 📝 Características de Streamlit

- **Interactividad rápida**: Puedes usar sliders, botones y otros widgets para crear interfaces interactivas sin experiencia en desarrollo web.
- **Actualización en tiempo real**: Los cambios en el código se reflejan instantáneamente, lo cual facilita el desarrollo rápido.
- **Integración directa con Python**: No necesitas aprender HTML, CSS o JavaScript. Todo se hace en Python.

## ✅ Ventajas de Streamlit

- **Fácil de usar**: No se requiere experiencia previa en desarrollo web.
- **Rápida implementación**: Permite crear prototipos y compartir modelos con otros fácilmente.
- **Código abierto**: Al ser una herramienta de código abierto, es completamente gratuita y tiene una gran comunidad.

## ❌ Limitaciones de Streamlit

- **Escalabilidad limitada**: No es ideal para aplicaciones web muy complejas o con necesidades de gran escalabilidad.
- **Interfaz simple**: Aunque es suficiente para aplicaciones pequeñas o prototipos, las opciones de personalización de la interfaz son limitadas.
- **Dependencia de Python**: Está orientado exclusivamente para desarrolladores de Python, por lo que no puede ser utilizado con otros lenguajes de programación.

## 🚀 Ejercicios en el Repositorio

Este repositorio contiene dos ejercicios prácticos que se encuentran en diferentes ramas del proyecto:

### 📂 Ramas del Repositorio

- **2024/sp1/feature/ejercicio-1**: Contiene el primer ejercicio en el que se desarrolla una aplicación de Streamlit para predecir enfermedades cardíacas basándose en un modelo de RandomForest.

  **Estructura del Proyecto**:
  - `app_streamlit.py`: Aplicación en Streamlit.
  - `modelo.py`: Código de entrenamiento del modelo.
  - `heart.csv`: Dataset utilizado para entrenar el modelo.
  - `datos_nuevos.csv`: Archivo con datos de ejemplo para realizar predicciones.
  - `heart.pkl`: Modelo entrenado y guardado.
  - `librerias.txt`: Archivo con las dependencias necesarias.

- **2024/sp1/feature/ejercicio-2**: Contiene el segundo ejercicio, donde se desarrolla una aplicación para encontrar la compatibilidad entre inquilinos usando un enfoque de recomendación basado en similitud.

  **Estructura del Proyecto**:
  - `app.py`: Aplicación principal de Streamlit.
  - `logica.py`: Contiene la lógica para calcular la similitud entre los inquilinos.
  - `ayudantes.py`: Funciones auxiliares para la visualización de datos (gráficos y tablas).
  - `dataset_inquilinos.csv`: Datos sobre las características de los inquilinos.
  - `metadatos.csv`: Preguntas de la encuesta realizadas a los inquilinos.
  - `Media/imagen.png`: Logo utilizado en la aplicación.

## 🔧 Cómo Usar este Repositorio

Para ejecutar cualquiera de las aplicaciones, puedes clonar este repositorio y seguir los siguientes pasos:

### 1. Clonar el repositorio

    git clone https://github.com/TuUsuario/TallerStreamlit.git

### 2. Cambiar a la rama del ejercicio que deseas ejecutar

    git checkout 2024/sp1/feature/ejercicio-1  # Para el primer ejercicio
    git checkout 2024/sp1/feature/ejercicio-2  # Para el segundo ejercicio

### 3. Crear un entorno virtual

    python -m venv streamlit-entorno

### 4. Activar el entorno virtual

**En Windows**:

    .\streamlit-entorno\Scripts\activate

**En Linux/macOS**:

    source streamlit-entorno/bin/activate

### 5. Instalar las dependencias

Dependiendo del ejercicio, el archivo de dependencias puede tener un nombre diferente:

    pip install -r librerias.txt

### 6. Ejecutar la aplicación de Streamlit

Para el primer ejercicio:

    streamlit run app_streamlit.py

Para el segundo ejercicio:

    streamlit run app.py

## 🌟 Recursos Adicionales

Para obtener más información sobre Streamlit y su uso, puedes visitar la [documentación oficial de Streamlit](https://docs.streamlit.io).
