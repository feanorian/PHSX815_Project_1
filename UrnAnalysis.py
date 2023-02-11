import sys
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import seaborn as sns
sys.path.append(".")

def green_success(color_list):    
    green_index = []
    for item in color_list:
        for j in range(len(item)):
            if item[j] == "Green":
                green_index.append(j+1)
                break
    return green_index

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    # Opens the datafile and reads it into array   
    
    with open(InputFile) as file:
        greens = [line.rstrip().split() for line in file]
        print(greens[:5])    
        
    success = green_success(greens)
    
    # plots a histogram for the urn 
    sns.histplot(success, stat='probability', discrete=True)
    plt.suptitle(f'# of Picks Until Green for {len(greens)} experiments')
    plt.xlabel('Pick #')
    plt.savefig(f'probs')