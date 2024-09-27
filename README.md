# Búsqueda de Inquilinos Compatibles con Streamlit

Esta aplicación permite buscar inquilinos compatibles para compartir una propiedad, utilizando un cuestionario de características y gustos. La aplicación se basa en la similitud de vectores para encontrar los inquilinos más compatibles con los ya existentes en una vivienda.

## Características

- **Formulario interactivo**: Permite a los usuarios ingresar información sobre los inquilinos actuales.
- **Selección del número de nuevos compañeros**: Los usuarios pueden elegir cuántos nuevos inquilinos desean buscar.
- **Visualización de compatibilidad**: Muestra un gráfico de compatibilidad entre los inquilinos actuales y los nuevos posibles.
- **Tabla comparativa**: Proporciona una tabla detallada de características de cada inquilino para ayudar a la selección manual.

## Instalación y Configuración

Sigue estos pasos para ejecutar la aplicación en tu máquina local:

### 1. Clonar el Repositorio

Primero, clona el repositorio en tu máquina local:

    git clone https://github.com/tu-usuario/taller-inquilinos-streamlit.git
    cd taller-inquilinos-streamlit

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

Una vez que el entorno virtual esté activado, instala las dependencias necesarias utilizando el archivo `requerimientos.txt`:

    pip install -r requerimientos.txt

### 4. Ejecutar la Aplicación

Para ejecutar la aplicación de Streamlit, utiliza el siguiente comando:

    streamlit run app.py

Esto abrirá la aplicación en tu navegador, donde podrás interactuar con los datos y ver los resultados.

## Estructura del Proyecto

        📁 taller-inquilinos-streamlit/
    │
    ├── 📄 app.py                     # Aplicación principal en Streamlit
    ├── 📄 logica.py                  # Lógica de cálculo de compatibilidad
    ├── 📄 ayudantes.py               # Funciones para gráficos y tablas
    ├── 📄 dataset_inquilinos.csv      # Dataset con características de los inquilinos
    ├── 📄 librerias.txt              # Lista de dependencias necesarias para ejecutar la app
    ├── 📄 metadatos.csv              # Preguntas realizadas en la encuesta
    ├── 📁 Media/
    │   └── 📄 imagen.png             # Imagen utilizada en la aplicación

## Uso de la Aplicación

### Ingresar datos sobre inquilinos actuales:

Utiliza el formulario en la barra lateral para ingresar los identificadores de los inquilinos actuales en la vivienda.

### Elegir cuántos nuevos compañeros buscar:

Selecciona cuántos nuevos compañeros quieres buscar para la vivienda.

### Ver los resultados:

La aplicación mostrará los nuevos inquilinos compatibles en función de la similitud con los inquilinos actuales, utilizando un gráfico y una tabla comparativa.

## Dataset

El dataset utilizado en la aplicación incluye información sobre:

- Horarios de los inquilinos
- Gustos personales (cine, lectura, etc.)
- Estilo de vida (animación, visitas, etc.)
- Características personales (nivel educativo, deportes, dieta)

## Funcionalidad de la Aplicación

### 1. Gráfico de Compatibilidad

Se genera un gráfico que muestra el nivel de similitud entre los inquilinos actuales y los potenciales nuevos compañeros. Este gráfico ayuda a identificar rápidamente los inquilinos más compatibles.

### 2. Tabla Comparativa

La tabla compara en detalle las características de los inquilinos actuales con las de los nuevos candidatos, lo que permite un análisis más profundo y manual para seleccionar los mejores compañeros.

¡Gracias por revisar este proyecto!
