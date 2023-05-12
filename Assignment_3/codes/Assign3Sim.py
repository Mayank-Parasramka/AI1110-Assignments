import numpy as np
import matplotlib.pyplot as plt
import random
#from scipy.stats import bernoulli
#from scipy.stats import norm
#from scipy.stats import binom
#import seaborn as sns

#Number of letters and envelopes
n =  3
#Possible number of tuples when the letters and envelopes are randomly arranged = 3! = 6
n_ss = 6
#number of tuples with atleast one letter in correct envelope
n_ev = 4
#printing the probability
y=n_ev/n_ss
print("Probability =",y)

def check_envelopes():
#consider a list [0,1,2] where value indicates letters and index of the list indicates the corresponding envelopes.
    r = [0,1,2]
    random.shuffle(r)
    for i in range(len(r)):
        if r[i] == i:
            return True
    return False

#Simulating the probability using the random variable

num_trials = 100000
num_successes = 0

for i in range(num_trials):
    if check_envelopes():
        num_successes += 1
print("Simulation result:", num_successes/num_trials)
