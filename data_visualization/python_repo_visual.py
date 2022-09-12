import requests
from plotly.graph_objs import Bar, Layout
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/json'}
r= requests.get(url, headers= headers)
resp = r.json()
stars, names, labels = [], [], []
for item in resp['items']:
    stars.append(item['stargazers_count'])
    repo_url = item['url']
    x_axis_val = f"<a href='{item['url']}'>{item['name']}</a>"
    names.append(x_axis_val)
    owner = item['owner']['login']
    description = item['description']
    labels.append(f"{owner}</br>{description}")



data = [{
    'type' : 'bar',
    'x' : names,
    'y': stars,
    'hovertext' : labels,
    'marker' : {
        'color' : 'rgb(60,100, 150)',
        'line' : {
            'width' : 1.5, 'color' : 'rgb(25,25,25)'
        },
    },
    'opacity' : .5,
    }]

my_layout = {
    'title': 'Most stared projects on Github',
    'xaxis' : {
        'title': 'Repository',
        'titlefont' : {'size' : 24},
        'tickfont' : {'size' : 14},
    },
    'yaxis' : {
        'title': 'Stars',
        'titlefont' : {'size' : 24},
        'tickfont' : {'size' : 14},
    },
}
fig = {'data': data , 'layout': my_layout}
offline.plot(fig)
