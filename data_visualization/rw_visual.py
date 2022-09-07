import matplotlib.pyplot as plt
from random_walk import RandomWalk

plt.style.use('seaborn')
# while True:

fig, ax = plt.subplots(figsize=(15,9))
rw = RandomWalk()
rw.fill_walk()
point_number = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues ,  s = 15)
# ax.plot(rw.x_values, rw.y_values)
ax.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
# res = input("Do you want to make one more walk ? (y/ n) \n")
    # if res == 'n' or res == 'N' :
    #     break
