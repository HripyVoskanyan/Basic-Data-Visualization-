import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Spectral, edgecolors= 'none', s = 40 )

plt.title('Cubic Numbers', fontsize = 30)
plt.xlabel('Values', fontsize = 15)
plt.ylabel('Cubes of Values', fontsize = 15)

plt.axis([0, 5100, 0, 125100000000])
plt.show()