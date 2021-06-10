# covidsim
A quick simulator in Python to show the effects of social distancing during a pandemic.

This program simulates the spread of a contageuous agent in a small community. The model is a simplification of what happens in reality, however it returns a realistic dynamic of the spread.

I use two parameters to regulate the dynamic of the simulated pandemic: the social rate and time to quarantine.

The social rate represent the rate or probability that a person has contacts with other persons in the generated population. The lower the rate, the lower the sample of people from which the programs generates a basket of potential new contacts.

The second parameter is the time before entering a quarantine. The program assume that a quarantined member of the population won't have further contacts until fully recovered. However, by regulating the time before quaranting, we can "expose" a member to new contacts.

Other parameters, like the probability of infection after a new contact, are used and can be manually modified.

The output of the program is data about the "daily" number of infected people, and can be represented with bell curve like this:

![image](https://user-images.githubusercontent.com/68285957/121511593-cb7b0500-c9b6-11eb-8a00-10e4c38ec26e.png)

