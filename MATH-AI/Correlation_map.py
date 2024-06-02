import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from shapely.geometry import Point

# Cargar el archivo CSV
df = pd.read_csv('housing.csv')

print("Número de entradas antes de la limpieza:", df.shape[0])

# Creamos una lista que contiene los nombres de las columnas que queremos verificar
cols_to_check = ['total_rooms', 'median_house_value']

# Iteramos por todas las columnas y nos quedamos sólo con aquellas cuyos valores sean mayores que cero
for col in cols_to_check:
    df = df[df[col] >= 0]

# Además, limpiamos los valores de longitud y latitud para que estén dentro de los rangos adecuados
df = df[(df['longitude'] >= -180) & (df['longitude'] <= 180)]
df = df[(df['latitude'] >= -90) & (df['latitude'] <= 90)]

# También limpiamos las filas que no contienen los valores específicos en la columna 'ocean_proximity'
valid_values = ['INLAND', '<1H OCEAN', 'NEAR BAY', 'NEAR OCEAN']
df = df[df['ocean_proximity'].isin(valid_values)]

# Finalmente mostramos de nuevo por pantalla el número de entradas tras la limpieza
print("Número de entradas después de la limpieza:", df.shape[0])

# Crear un GeoDataFrame a partir del DataFrame original
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))

# Definir la proyección adecuada, por ejemplo, WGS 84
gdf.crs = "EPSG:4326"

# Cargar el archivo de shapefile para dibujar los límites geográficos de California
california = gpd.read_file("./tl_2019_06_cousub")

# Filtrar las geometrías que no están en el rango correcto
california = california.to_crs(gdf.crs)

# Creamos una nueva columna en el GeoDataFrame de California para almacenar la correlación
california['correlation'] = np.nan

# Iteramos sobre cada área en el GeoDataFrame de California
for index, row in california.iterrows():
    # Obtener la geometría del área actual
    geometry = row['geometry']

    # Filtrar el GeoDataFrame para obtener solo las entradas dentro del área actual
    filtered_data = gdf[gdf.within(geometry)]

    # Calcular la correlación entre 'total_rooms' y 'median_house_value' dentro de esta área
    area_correlation = filtered_data[['population', 'latitude']].corr().iloc[0, 1]

    # Almacenar la correlación calculada en la columna 'correlation' del GeoDataFrame
    california.loc[index, 'correlation'] = area_correlation

# Configuración para el mapa
vmin = -1.0
vmax = 1.0
cmap = plt.cm.seismic

# Crear la figura
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# Dibujar el mapa de California con colores basados en la correlación
california.plot(column='correlation', cmap=cmap, vmin=vmin, vmax=vmax, ax=ax, edgecolor='black', linewidth=0.5)

# Añadir barra de color
sm = ScalarMappable(cmap=cmap, norm=Normalize(vmin=vmin, vmax=vmax))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('Correlación')

# Añadir título
plt.title('Correlación entre population y latitude en áreas de California')

# Mostrar el mapa
plt.show()
