import pygal
from die import Die

d6 = Die()
d10 = Die(10)

results = []
for roll_num in range(1000):
    result = d6.roll() + d10.roll()
    results.append(result)

frequencies = []
max_result = d6.num_sides + d10.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#making a histogram
hist = pygal.Bar()
hist.title = 'Results of rolling 2 6-sided dices'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Results'

hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice.svg')