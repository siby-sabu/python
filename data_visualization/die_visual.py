from die import Die
from plotly.graph_objects import Bar, Layout
from  plotly import offline

d6_1 = Die(6)
d6_2 = Die(10)
# die_results = {'d1': [], 'd2': []}

# frequencies = {'d1':[], 'd2': []}

# die_results =[]
# frequencies = []
die_digits = d6_1.num_sides + d6_2.num_sides

die_results = [(d6_1.roll() + d6_2.roll()) for r in range(5000) if True]

# for result in range(50000):
#     die_sum = d6_1.roll() + d6_2.roll()
#     die_results.append(die_sum)
    # die_results['d1'].append(d6_1.roll())
    # die_results['d2'].append(d6_2.roll())
# for pos in range(1, d6_1.num_sides+1):

frequencies = [die_results.count(x) for x in range(2, die_digits+1) if True]

# for pos in range(2, die_digits+1):
    # pos_count = die_results['d1'].count(pos)
    # frequencies['d1'].append(pos_count)
    # pos_count = die_results['d2'].count(pos)
    # frequencies['d2'].append(pos_count)
    # frequencies.append(die_results.count(pos))

# x_values = list(range(1, d6_1.num_sides+1))
x_values = list(range(2, die_digits+1))
# data = [Bar(x= x_values, y =  frequencies['d1']), Bar(x= x_values, y =  frequencies['d2'])]
data = [Bar(x= x_values, y =  frequencies)]
x_axis_config = {"title": "Result", 'dtick': 1}
y_axis_config = {'title': 'Frequence of Result'}
my_layout = Layout(title= "Result of rolling two D6 1000 times", xaxis=x_axis_config, yaxis= y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='dice2.html')