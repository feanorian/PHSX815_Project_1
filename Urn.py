import sys
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import seaborn as sns
import random
from random import sample

np.random.seed(546)
colors = ['Black', 'White', 'Green']
# The number of marbles in each urn
N = 100000
#The probability of picking white, green, or black for urn 1
urn_1 = [.25, .35, .4]
#The probability of picking white, green, or black for urn 2
pick = 20
urn_2 = [.37, .25, .38]
outcomes = []
occurences = []
N_Trials = 1000

# Function that constructs an urn  passing the number of trials and probability array for the urn. 
def Category(trials, prob):
        x = np.random.multinomial(trials, prob, 1)
        return x

# Function that picks random samples for N_Trials with N_picks per trial
def color_samplings(N_Trials, N_picks):
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
occurences = Category(N, urn_2)[0]
for i in range(len(occurences)):
    outcomes += str(i+1)*occurences[i]
# converts the strings to ints to plot in the histogram
count_list = [int(i) for i in outcomes]
summary_dic = {'white':occurences[0], 'green': occurences[1], 'black':occurences[2]}
labels = [summary_dic.keys()]
white, green, black= occurences[0], occurences[1], occurences[2]
# counts the total rolls of the die
count = sum(occurences)
success_list = [white/count, green/count, black/count]

#color_data = 

# Function call to generate the random sample
greens = color_samplings(N_Trials, pick)
# Function call to compute the first successful green pick for N_Trials
success = green_success(greens)

# writes the outcomes to a file
InputFile = 'pick2.txt'
doOutputFile = True
if doOutputFile:
    outfile = open(InputFile, 'w')
    #for e in range(0,Nexp):
    for item in greens:
        item = ' '.join(item)
        outfile.write(item+"\n")
    #outfile.write(str(success_list)+" ")
        
    outfile.close()
else:
    print(greens[:3])