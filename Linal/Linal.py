from collections import Counter
from tkinter import Y
from matplotlib import pyplot


num_friends = [100,64,20,12,100,64,20,12,100,64,20,12,100,64,20,12,100,64,100,64,20,12,100,64,20,12,100,64,20,12,100,64,20,12,100,64100,64,20,12,100,64,20,12,100,64,20,12,100,64,20,12,100,64100,64,20,12,100,64,20,12,100,64,20,12,100,64,20,12,100,64100,64,20,12,100,64,20,12,100,64,20,12,100,64,20,12,100,6420,12,100,64,20,12,73]
friends_counts = Counter(num_friends)
xs = [i for i in range(101)]                              #max
ys = [friends_counts[i] for i in xs] # высота - это число друзей

num_points = len(num_friends)
largest_value = max(num_friends) # Наибольшее значение равно 100 
smallest_value = min(num_friends) # Наименьшее значение равно 1

sorted_values = sorted(num_friends) # Отсортированные значения 
smallest_value = sorted_values[0]  # Минимум равен 1 
second_smallest_value = sorted_values[1] # Следу1С1ЦИй минимум равен 1 
second_largest_value = sorted_values[-2] # Следу1С1ЦИй максимум равен 49
#Среднее значение 
def mean(xs: list[float]) -> float: 
    return sum(x) / len(x) 
mean(num_friends) 

pyplot.bar(xs,ys)
pyplot.axis([0,101,0,25])
pyplot.title("Гистограмма колличеств друзей")
pyplot.xlabel("Число друзей")
pyplot.ylabel("Число людей")
pyplot.show()