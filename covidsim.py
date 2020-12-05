import random
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np

class Person:
    def __init__(self, id, age, relations, distance):
        self.id = id
        self.age = age
        self.sick = False
        self.days = 0
        self.relations = relations
        self.distance = distance
        self.immune = False
        self.dead = False
    def getSick(self):
        chance = random.randint(1,4)
        if chance == 1:
            self.sick = True
            person.days +=1
        if self.sick == True and self.age > 70:
            self.dead = True
def genRel(id):
    rangeids = []
    for i in range(100):
        i = random.randint(max(0,id - 50), min(popSize - 1, id + 50))
        if not i in rangeids:
            rangeids.append(i)
    rels = random.randint(5,len(rangeids))
    ids = np.random.choice(rangeids, rels, replace=False)
    return ids

popSize = 10000
duration = 10
socialDistRate = 80
pop = []
population = []
sick = []
daySicks = []
immRate = []

for i in range(popSize):
    population.append(i)
    relations = genRel(i)
    age = random.randint(10,95)
    d = random.randint(0,100)
    if d <= socialDistRate:
        d = 1
    else:
        d = 0
    pop.append(Person(i, age, relations, d))
ptZero = random.randint(0,popSize-1)
pop[ptZero].sick = True
sick.append(ptZero)
del population[ptZero]
days = []
errors = 0
immune = 0
count = 0
dayRate = 0.
i = 1
popMrate = 0.
deceased = 0
while dayRate < .8:
    days.append(i)
    i +=1
    for person in pop:
        if person.sick == False and person.immune == False:
            for j in person.relations:
                rnd = random.randint(0,100)
                contact = False
                if person.distance == 1:
                    if rnd <= 5:
                        contact = True
                else:
                    if rnd <= 90:
                        contact = True
                if pop[j].sick == True and contact == True:
                    if person.sick == False:
                        person.getSick()
                        if person.sick == True:
                            sick.append(person.id)
                            del population[population.index(person.id)]
        else:
            if person.days >= duration and person.sick == True:
                person.sick = False
                person.immune = True
                immune +=1 
                del sick[sick.index(person.id)]
            else:
                person.days +=1
    daySicks.append(len(sick))
    dayRate = immune / len(pop)
    immRate.append(dayRate)
    count +=1
plt.plot(days,daySicks)
plt.show()
