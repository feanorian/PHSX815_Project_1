# PHSX815_Project_1
This is the repository for Project 1 for PHSX 815 at KU.

## Urn.Py and UrnAnalysis

`Urn.py` generates multinomial variates representing two Urns of marbles of three colors (`White`, `Green`, and `Black`) from two different ratios and writes the data to files `Urn_1.txt` and `Urn_2.txt`. It will run 10000 trials of 20 draws each.

`UrnAnalysis.py` reads the data from `Urn_1.txt` and `Urn_2.txt`, determines which draw the first green marble occcurs, and calculates the mean, median, and log likelihood of the null hypothesis. In addition, it plots histograms of each distribution and then plots a bar and whisker plot illustrating the media and interquartile range for each pick.
