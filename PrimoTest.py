import random
import Costants as c
import Functions as f
from matplotlib import pyplot as plt

len = 1024

population = range(0, len)

weightList = f.weight_builder(len, c.m1, c.q1, c.m2, c.q2)

print(weightList)
plt.plot(weightList)
plt.show()

# generate n numbers using the probability density function just created
n = 100000

dict_results1 = dict.fromkeys(population, 0)

for i in range(0,n):
    # estraggo n numeri e li stampo giusto per vedere se funziona.
    dict_results1[f.custom_pdf_number_generator(population, weightList)[0]] += 1

plt.plot(dict_results1.keys(), dict_results1.values())
plt.show()

dict_results2 = dict.fromkeys(population, 0)
maxInt = 50
for i in range(0, n):
    dict_results2[f.adjusted_number_generator(maxInt, population, weightList)] += 1

smaller_dict = dict((key,value) for key, value in dict_results2.items() if key < maxInt)

plt.plot(smaller_dict.keys(), smaller_dict.values())
plt.show()