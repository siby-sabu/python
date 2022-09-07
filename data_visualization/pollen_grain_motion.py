import matplotlib.pyplot as plt
from random_walk import RandomWalk

grain_path = RandomWalk(6000)
grain_path.fill_walk()

fig, ax = plt.subplots(figsize = (10,8), )
plot_val = range(grain_path.num_points)
ax.scatter(grain_path.x_values, grain_path.y_values, c= plot_val, cmap=plt.cm.Reds, s=10)
ax.scatter(grain_path.x_values[0], grain_path.y_values[0], c='green', s = 100)
ax.scatter(grain_path.x_values[-1], grain_path.y_values[-1], c='green', s=100)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()

