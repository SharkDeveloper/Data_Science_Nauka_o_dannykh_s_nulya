from cProfile import label
from matplotlib import pyplot

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67] # Друзья 
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190] # Минуты 
labels = ['а', "b", 'с', 'd', 'е', 'f', 'g', 'h', 'i'] # Метки 

pyplot.scatter(friends,minutes)
for label,friend_count,minut_count in zip(labels,friends,minutes):
    pyplot.annotate(label,xy=(friend_count,minut_count),xytext = (5,-5),textcoords=("offset points"))
pyplot.show()