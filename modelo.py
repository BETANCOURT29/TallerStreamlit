# Importamos las bibliotecas necesarias
import pandas as pd

# Leemos el dataset
data = pd.read_csv('heart.csv')

# Importamos la clase LabelEncoder de la biblioteca scikit-learn
from sklearn.preprocessing import LabelEncoder

# Convertimos la columna 'Familia' en valores numéricos utilizando LabelEncoder
encoder = LabelEncoder()
data['Familia'] = encoder.fit_transform(data['Familia'])

# Separamos las características (X) y la variable objetivo (y)
X = data.drop('chd', axis=1)  # Eliminar la columna 'chd' de las características
y = data['chd']  # Variable objetivo

# Importamos la función train_test_split de la biblioteca scikit-learn
from sklearn.model_selection import train_test_split

# Dividimos el conjunto de datos en conjuntos de entrenamiento y prueba (70% entrenamiento, 30% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Importamos la clase RandomForestClassifier de la biblioteca scikit-learn
from sklearn.ensemble import RandomForestClassifier

# Creamos una instancia del clasificador RandomForest
clf = RandomForestClassifier()

# Entrenamos el modelo
clf.fit(X_train, y_train)

# Importamos las bibliotecas necesarias
import pickle

# Guardamos el modelo entrenado en un archivo 'heart.pkl'
pickle.dump(clf, open('heart.pkl', 'wb'))