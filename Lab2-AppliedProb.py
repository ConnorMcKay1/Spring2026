import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


print("test test \n")

'''
create histograms, frequency polygons and ogives programmatically

{83, 93, 85, 71, 72, 98, 69, 73, 74, 83,
73, 82, 63, 79, 66, 88, 96, 63, 100, 77,
107, 81, 81, 89, 75, 92, 88, 70, 74, 80,
74, 77, 73, 94, 87, 95, 81, 82, 78, 80,
95, 73, 85, 84, 76, 82, 92, 73, 91, 71,
92, 88, 59, 73, 86, 72, 77, 81, 74, 74,
73, 75, 78, 98, 91, 66, 80, 82, 78, 80,
87, 88, 79, 85, 76, 90, 85, 86, 84, 63,
97, 93, 79, 78, 72, 89, 78, 89, 90, 63,
86, 84, 89, 64, 79, 83, 87, 68, 76, 87}

1--> Using the 2k rule for the number of classes, construct a frequency distribution
of the above dataset. Display the frequency table and show the upper and lower
class limits, class marks and class boundaries.
    upper/lower class limits, class marks, class boudaries

2-->Draw the histogram and frequency polygon of the frequency distribution.

3--> Draw ogives for the more-than type and the less-than type cumulative frequencies in a single figure.

4--> Display the median of the dataset and the mode(s). Compare the calculated
median with the value obtained from the point of intersection of the two ogives.

5--> Calculate the Arithmetic Mean of the given dataset and then calculate the same
from the Frequency Distribution (using class marks). Display the difference of
the two.

6--> Calculate and display the Geometric Mean of the given dataset.

7--> Calculate and display the Harmonic Mean of the given dataset.
'''

values = [83, 93, 85, 71, 72, 98, 69, 73, 74, 83,
73, 82, 63, 79, 66, 88, 96, 63, 100, 77,
107, 81, 81, 89, 75, 92, 88, 70, 74, 80,
74, 77, 73, 94, 87, 95, 81, 82, 78, 80,
95, 73, 85, 84, 76, 82, 92, 73, 91, 71,
92, 88, 59, 73, 86, 72, 77, 81, 74, 74,
73, 75, 78, 98, 91, 66, 80, 82, 78, 80,
87, 88, 79, 85, 76, 90, 85, 86, 84, 63,
97, 93, 79, 78, 72, 89, 78, 89, 90, 63,
86, 84, 89, 64, 79, 83, 87, 68, 76, 87]


N = 0  # number of values/observations
K = 0   # number of classes


    # NUMBER OF CLASSES
def ClassNumber(values, N, K):
    N = len(values)
    print("Number of Observations: ", N)
    while 2**K <= N:
        K += 1 
    print("Number of Classes: ", K)
    return N, K

    # returns the Number of Observations & Classes to the global variables
N, K = ClassNumber(values, N, K)



    # CLASS WIDTH
def ClassWidth(values, K):
    classwidth = math.ceil((max(values) - min(values)) / K)
    return classwidth

classwidth = ClassWidth(values, K)
print("Class Width:", classwidth)



    # CLASS MIDPOINT
    # create a list of the midpoints?
def ClassMidpoints(values, K):
    
    #min(values)+(((2*K-1)d-1)/2)
    print()




    # FREQUENCY TABLE
                            # tuples                 tallies 
# df = pd.DataFrame({"Classes": [1, 2], "Frequencies": [3, 4]})
# fig, ax = plt.subplots()
# ax.axis("off")
# (np.float64(0.0), np.float64(1.0), np.float64(0.0), np.float64(1.0))
# table = pd.plotting.table(
#     ax, df, loc="center", cellLoc="center", colWidths=[0.2, 0.2]
# )
# plt.show()



