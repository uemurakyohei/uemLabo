import matplotlib.pyplot as plt
from random import random

denominator = 100

x_values = range(1,denominator)
y_values = [random() for x in x_values]

y_rd_values = [[0,0] for _ in range(100)]

for y in y_values:
	yindex = int(y*10)
	x = y_rd_values[yindex][1] + 1
	y_rd_values[yindex][1] = x

x_list = [range(0,100,1)]
y_list = []
for num in range(0,100,1):
	print(y_rd_values[num][1])
	y_list.append(y_rd_values[num][1])

print(y_list,y_rd_values)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_list,y_list,s=10)

ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Value",fontsize=14)

ax.tick_params(axis='both',which='major',labelsize=14)

#軸の範囲
ax.axis([0,100,0,1])

plt.show()