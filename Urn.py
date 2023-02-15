"""
Name: Craig Brooks
PHSX 815 Spring 2023
Project # 1
Due Date 2/14/2023

This code creates the urns to sample from, then draws from them and writes the outcomes from the drawings from each urn to a file
"""


import sys
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import seaborn as sns
import random
from random import sample

np.random.seed(546)

# stores the colors available
colors = ['Black', 'White', 'Green']
# The number of marbles in each urn
N = 100000

#The probabilities of picking white, green, or black for urn 1
urn_H0 = [.25, .35, .4]

#The probabilities of picking white, green, or black for urn 2
urn_H1 = [.42, .20, .38]

#number of times to draw for each trial
pick = 100

# Stores the multinomial variates representing the outcomes for Dist A
outcomes_H0 = []

# Stores all the outcomes for Dist A
occurences_H0 = []

# Stores multinomial variates representing the outcome for Dist B
outcomes_H1 = []

# Stores the position of first success for Dist B
occurences_H1 = []

#Number of Trials to run 
N_Trials = 10000

# Function that constructs an urn  passing the number of trials and probability array for the urn. 
def Category(trials, prob):
        x = np.random.multinomial(trials, prob, 1)
        return x

# Function that picks random samples for N_Trials with N_picks per trial
def color_samplings(N_Trials, N_picks, outcomes):
    color_lists = []
    for _ in range(N_Trials):
        samples = random.choices(outcomes, k=N_picks)
        color=[]
        for item in samples:
            if item == '1':
                color.append('White')
            elif item == '2':
                color.append('Green')
            else:
                color.append('Black')
        color_lists.append(color)
    return color_lists
    
# Determines the number of picks until a successful green pick, then appends to the array green_index
def green_success(color_list):    
    green_index = []
    for item in color_list:
        for j in range(len(item)):
            if item[j] == "Green":
                green_index.append(j+1)
                break
    return green_index
    

    
# constructs an urn  passing the number of rolls and the probability. Here, the number of marbles is set to N = 100000
occurences_H0 = Category(N, urn_H0)[0]
occurences_H1 = Category(N, urn_H1)[0]
for i in range(len(occurences_H0)):
    outcomes_H0 += str(i+1)*occurences_H0[i]
    outcomes_H1 += str(i+1)*occurences_H1[i]


# Function call to generate the random sample
greens_H0 = color_samplings(N_Trials, pick, outcomes_H0)
# Function call to compute the first successful green pick for N_Trials
success_H0 = green_success(greens_H0)

greens_H1 = color_samplings(N_Trials, pick, outcomes_H1)
# Function call to compute the first successful green pick for N_Trials
success_H1 = green_success(greens_H1)



# writes the outcomes to a file
InputFile_H0 = 'urn_H0.txt'
InputFile_H1 = 'urn_H1.txt'
doOutputFile = True


if doOutputFile:
    
    outfile_H0 = open(InputFile_H0, 'w')
    for item in greens_H0:
        item = ' '.join(item)
        outfile_H0.write(item+"\n")
    outfile_H0.close()

    outfile_H1 = open(InputFile_H1, 'w')
    for item in greens_H1:
        item = ' '.join(item)
        outfile_H1.write(item+"\n") 
    outfile_H1.close()
else:
    print(greens[:3])
