import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Cargar el dataset en un DataFrame
data = pd.read_csv("housing.csv")

# Cargar el shapefile en un GeoDataFrame
california = gpd.read_file("California_Counties.shp")

# Verificar el CRS de california y asignar si es necesario
if california.crs is None:
    california.set_crs("EPSG:3857", inplace=True)  # Asumiendo que el shapefile está en un CRS proyectado (e.g., Web Mercator)


# print(california.head())

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

# Verificar el resultado
# print(data_joined.head(10000))

# Plotear los datos
# Asignar colores según index_right
unique_indices = data_joined['index_right'].unique()
colors = plt.get_cmap('tab20', len(unique_indices))  # Usar una paleta de colores con suficiente variedad

color_map = {index: colors(i) for i, index in enumerate(unique_indices)}

# Añadir la columna de colores a data_joined
data_joined['color'] = data_joined['index_right'].apply(lambda x: color_map[x])

# Plotear los datos
fig, ax = plt.subplots(figsize=(10, 10))

# Plotear el shapefile de California
california.plot(ax=ax, color='white', edgecolor='black')

# Plotear los puntos de data_joined con colores según index_right
for index, row in data_joined.iterrows():
    ax.plot(row.geometry.x, row.geometry.y, 'o', color=row['color'], markersize=5)

plt.show()