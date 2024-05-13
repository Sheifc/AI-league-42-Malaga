import pandas as pd
import geopandas as gpd

from shapely.geometry import Point

# Cargar el dataset en un DataFrame
data = pd.read_csv("housing.csv")

# Cargar el shapefile en un GeoDataFrame
california = gpd.read_file("California_Counties.shp")

california["id"] = california.index

print(california.head())
# Convertir las coordenadas de latitud y longitud en geometrías Point
data['geometry'] = data.apply(lambda row: Point(row['longitude'], row['latitude']), axis=1)
data_geo = gpd.GeoDataFrame(data, geometry='geometry')

# Establecer el sistema de referencia de coordenadas
data_geo.crs = california.crs

# Realizar la unión espacial
data.join(california, lsuffix='geometry', rsuffix='geometry')




print(data_geo.head(1000))
# print(california.head())



# print(california.head())
