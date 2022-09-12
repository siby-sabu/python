from plotly.graph_objects import Scattergeo, Layout
from plotly import offline
import json
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    file_cnt = json.load(f)
    features_dict = file_cnt['features']

    mag, lon, lat, text = [], [], [], []
    for feature in features_dict:
        mag.append(feature['properties']['mag'])
        text.append(feature['properties']['title'])
        lon.append(feature['geometry']['coordinates'][0])
        lat.append(feature['geometry']['coordinates'][1])

    # data =[Scattergeo(lat=lat, lon=lon)]
    data =[{
        'type' :'scattergeo',
        'lat': lat,
        'lon': lon,
        'text': text,
        'marker':{
            'size' : [5* m for m in mag],
            'color': mag,
            'colorscale' : 'Hot',
            'reversescale' : True,
            'colorbar': {'title': 'Magnitude'}
        }
    }]

    my_layout = Layout(title="Global Earthquakes")
    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename="global_earthquakes.html")
