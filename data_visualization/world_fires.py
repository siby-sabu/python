from plotly.graph_objects import Scattergeo, Layout
import csv
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    next(reader)
    lat, lon,fires = [], [], []
    for world_fire in reader:
        lat.append(world_fire[0])
        lon.append(world_fire[1])
        brightness = float(world_fire[2])
        fires.append(brightness)
    min_fire = min(fires)
    data = {
    'type' : "scattergeo",
    'lat' : lat,
    'lon' : lon,
    'marker': {
        'size' : [fire - min_fire for fire in fires],
        'color' : fires,
        'colorscale' : 'Hot',
        'colorbar' : {'title' : "Magniture"}

    }
    }
    my_layout = Layout(title="World fires")
    graph = {
        'data' : data,
        'layout': my_layout
    }

    offline.plot(graph , filename= "world_fires.html")
    

