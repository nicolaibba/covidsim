import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(0)
class Person:
    def __init__(self, name = ''):
        self.name = name
        self.is_sick = False
        self.day_sick = None
        self.contageous = False
        self.quarantined = False
        self.recovered = False
    
    def getSick(self, day):
        if self.recovered == False:
            if self.is_sick == False:
                if random.random() < .50:
                    self.is_sick = True
                    self.day_sick = day
    
    def quarantine(self):
        self.quarantined = True
        
    def contageous(self):
        self.contageous = True
    
    def recover(self):
        self.is_sick = False
        self.recovered = True
        self.quarantined = False
        self.contegeous = False
   
class Population:
    def __init__(self, size = None, recovery_time = 10, quarantine_time = 2, social_rate = .8):
        self.size = size
        self.recovery_time = recovery_time
        self.quarantine_time = quarantine_time
        self.distancing_rate = social_rate
        self.people = []
        self.day = 0
        self.pzero = None
        self.sicks = []
        self.recovered = []
        self.create()
        self.patientZero()
        self.contact()
        
    def create(self):
        for i in range(self.size):
            self.people.append(Person(name=i))
            
    def patientZero(self):
        # Randomize patient 0:
        s = random.choice(self.people)
        s.is_sick = True
        s.contageous = True
        s.day_sick = 0
        self.sicks.append(s.name)
        #s.quarantined = True
        self.pzero = s
        
    def newDay(self):
        self.day +=1
        for person in self.people:
            if person.is_sick == True:
                if self.day == person.day_sick + 1: person.contageous = True
                if self.day == person.day_sick + self.quarantine_time + 1: person.quarantine()
                if self.day == person.day_sick + self.recovery_time: person.recover()
        self.contact()
        self.sicks = [i.name for i in self.people if i.is_sick == True]
        self.recovered = [i.name for i in self.people if i.recovered == True]


    def contact(self):
        basket = []
        for person in self.people:
            if person.quarantined == False: basket.append(person)
        basket = random.sample(basket, round(len(basket)* self.distancing_rate))
        random.shuffle(basket)
        for p in basket:
            pickfrom = [i for i in basket if i != p]
            samplesize = 2
            if samplesize > len(pickfrom): samplesize = len(pickform)
            if samplesize > 0:
                contacts = random.sample(pickfrom, samplesize)

                for person in contacts:
                    if p.contageous:
                        if person.recovered == False: person.getSick(self.day)
                    if person.contageous:
                        if p.recovered == False: p.getSick(self.day)
                            
    def run(self):
        dailySicks = [1]
        while True:
            self.newDay()
            dailySicks.append(len(self.sicks))
            if dailySicks[-1] == 0: break
        return dailySicks

def runs(size = 500, social_rate = [.3], quarantine_time = [2]):
    try:
        output = {}
        
        for time in quarantine_time:
            output[time] = [[], [], []]
            
            for rate in social_rate:
        
                pop = Population(size = size, recovery_time = 10, quarantine_time = time, social_rate = rate)
                a = np.array(pop.run())
                output[time][0].append(rate)
                output[time][1].append(np.max(a))
                output[time][2].append(a)
                
        return output
    
    except Exception as e:
        print(e)
     
    
QUARANTINE_TIME = [i for i in range(1,5)]
SOCIAL_RATE = [i / 10 for i in range(3, 10, 1)]

data = runs(size = 500, social_rate = SOCIAL_RATE, quarantine_time = QUARANTINE_TIME)

number_of_subplots= len(QUARANTINE_TIME)+1
x = SOCIAL_RATE
v = 0
fig = plt.figure(figsize=(20, 18), dpi=80, facecolor='w', edgecolor='k')
for i in range(1, number_of_subplots):
    v = v+1
    ax = fig.add_subplot(number_of_subplots,1,v)
    
    y = data[i][1]
    ax.plot(x,y)
    ax.title.set_text("Days before quarantining: "+ str(i))
plt.show()

plt.figure()
plt.plot(data[1][2][1])
plt.show()
