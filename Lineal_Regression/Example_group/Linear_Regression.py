import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

from shapely.geometry import Point

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler

import joblib

# Cargar el dataset en un DataFrame
data = pd.read_csv("housing.csv")

# Cargar el shapefile en un GeoDataFrame
california = gpd.read_file("California_Counties.shp")

# Verificar el CRS de california y asignar si es necesario
if california.crs is None:
    california.set_crs("EPSG:3857", inplace=True)  # Asumiendo que el shapefile está en un CRS proyectado (e.g., Web Mercator)

# Convertir las coordenadas de latitud y longitud en geometrías Point
data['geometry'] = data.apply(lambda row: Point(row['longitude'], row['latitude']), axis=1)
data_geo = gpd.GeoDataFrame(data, geometry='geometry')

# Verificar el CRS de data_geo y asignar si es necesario
if data_geo.crs is None:
    data_geo.set_crs("EPSG:4326", inplace=True)  # Asumiendo que los puntos están en WGS84

# Transformar CRS de data_geo para que coincida con california
data_geo = data_geo.to_crs(california.crs)

# Realizar la unión espacial
data_joined = gpd.sjoin(data_geo, california, how="inner", predicate="within")


# Plotear los datos
# Asignar colores según index_right utilizando una paleta de colores de Matplotlib
num_categories = len(data_joined['index_right'].unique())
cmap = plt.get_cmap('tab20', num_categories)  # Paleta de colores con suficientes categorías

# Plotear los datos
fig, ax = plt.subplots(figsize=(10, 10))

# Plotear el shapefile de California
california.plot(ax=ax, color='white', edgecolor='black')

# Plotear los puntos de data_joined con colores según index_right
data_joined.plot(ax=ax, column='index_right', categorical=True, legend=True, cmap=cmap, markersize=5, legend_kwds={'title': 'County', 'fontsize': 'x-small', 'bbox_to_anchor': (1.02, 1)})

plt.show()

#Realizamos una limpieza de los datos redundantes o que no aportan información
data_joined = data_joined.drop(columns=['longitude', 'latitude', 'geometry', 'ocean_proximity'])

data_joined = data_joined.rename(columns={'index_right': 'county'})

data_joined = data_joined.dropna()

data_joined

# Inicializar el objeto MinMaxScaler
scaler = MinMaxScaler()

# Ajustar y transformar los datos
data_normalized = scaler.fit_transform(data_joined)

data_normalized = pd.DataFrame(data_normalized, columns=data_joined.columns)

print(data_normalized.corr())

# Convertir 'county' en variables dummy con un sufijo
dummy_county = pd.get_dummies(data_normalized['county'], prefix='county', drop_first=True)

# Eliminar la columna 'county' original del DataFrame X
X = data_normalized.drop('county', axis=1)

# Unir las características originales con las variables dummy
X = pd.concat([X, dummy_county], axis=1)

# Separar las características (variables independientes) y la variable objetivo (precio de la vivienda)
X = X[['housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income'] + dummy_county.columns.tolist()]
y = data_joined['median_house_value']

# # Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# # Inicializar el modelo de regresión lineal
model = LinearRegression()

# # Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# # Realizar predicciones sobre los datos de prueba
y_pred = model.predict(X_test)

# # Calcular el error cuadrático medio (MSE)
mse = mean_squared_error(y_test, y_pred)
print("\n\nError cuadrático medio (MSE):", mse)

# Calcular el coeficiente de determinación (R^2)
r_squared = model.score(X_test, y_test)

print("Porcentaje de variabilidad explicada:", r_squared)

# Exportar el modelo a un archivo
joblib.dump(model, 'linear_regression_model.pkl')

# Visualizar los datos y la línea de regresión
# Suponiendo que queremos visualizar median_income vs median_house_value

# Ordenar los datos para una mejor visualización
sorted_index = X_test['median_income'].argsort()
X_test_sorted = X_test.iloc[sorted_index]
y_test_sorted = y_test.iloc[sorted_index]
y_pred_sorted = y_pred[sorted_index]

plt.figure(figsize=(10, 6))
plt.scatter(X_test_sorted['median_income'], y_test_sorted, color='blue', label='Datos reales')
plt.plot(X_test_sorted['median_income'], y_pred_sorted, color='red', linewidth=2, label='Línea de regresión')
plt.xlabel('Ingreso mediano')
plt.ylabel('Valor mediano de la casa')
plt.title('Ingreso mediano vs Valor mediano de la casa')
plt.legend()
plt.show()

