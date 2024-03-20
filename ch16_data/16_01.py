import json 
import plotly.express as px
# json #load  - file
# json #loads - str -> dict, dict -> str

mag,lat,lon = [],[],[]

with open('ch16_data/b.geojson', 'r', encoding = 'utf-8') as f:
    data = json.load(f)
    for feature in data['features']:
        mag.append(feature['properties']['mag'])
        lon.append(feature['geometry']['coordinates'][0])
        lat.append(feature['geometry']['coordinates'][1])

fig = px.scatter_geo(lat=lat, lon=lon, size=mag)
fig.show()