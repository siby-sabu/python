import matplotlib.pyplot as plt

keys = [-2, -1, 0, 1,2,3,4,5]
values = [4, 1, 0,1,4,9,16, 25]
# keys = range(1,1001)
# values = [k ** 2 for  k in keys]
plt.style.use("seaborn")
fig, ax = plt.subplots()
# ax.plot(inputs, squares)
ax.scatter(keys,values, c=values, cmap=plt.cm.Reds ,  s=100)
# ax.set_title("Square Numbers", fontsize = 24)
# ax.set_xlabel("Values", fontsize = 14)
# ax.set_ylabel("Square values", fontsize = 14)
# ax.axis([0,1100,0,1100000])
# plt.grid()

# ax.tick_params(axis="both", labelsize = 14)
# plt.show()
plt.savefig("suares_plot2.png", bbox_inches = 'tight')