import random as r

iterNum = 1000
minimo = 1
massimo = 0

for i in range(0, iterNum):
    n = r.random()
    if n > massimo:
        massimo = n
    if n < minimo:
        minimo = n

print("Il minimo è: " + str(minimo))
print("Il massimo è: " + str(massimo))
