import random as r
import Costants as c
import Functions as f
from matplotlib import pyplot as plt

len = 1024

weightList = f.weight_builder(len, c.m1, c.q1, c.m2, c.q2)

plt.plot(weightList)
plt.show()  # Shows the plot of the distribution created
