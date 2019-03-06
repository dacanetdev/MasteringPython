import folium
from folium.plugins import MarkerCluster
import pandas as pd

data = pd.read_csv("Volcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']
name = data['NAME']

def change_color(elev):
  if(elev < 1000):
    return ("green")
  elif(1000 <= elev < 3000):
    return ("orange")
  else:
    return ("red")

map = folium.Map(location=[37.296933,-121.9574983], zoom_start=5, tiles="CartoDB dark_matter")

marker_cluster = MarkerCluster().add_to(map)

for lat, lon, elevation, name in zip(lat, lon, elevation, name):
  folium.CircleMarker(location=[lat, lon], radius=9, popup=f"{name}, {elevation} mts", fill_color=change_color(elevation), color="gray", fill_opacity=0.9).add_to(marker_cluster)

map.save("map1.html")