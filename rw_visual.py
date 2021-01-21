import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    #set size
    plt.figure(dpi = 128, figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap=plt.cm.Spectral, edgecolors='none', s = 1)

    #first and last points
    plt.scatter(0, 0, c = 'blue', edgecolors='none', s = 80)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'violet', edgecolors='none', s = 80)

    #title
    plt.title('Random Walk', fontsize = 35)
    #remove axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Do you want to make another walk? (yes/no)')
    if keep_running == 'no':
        break