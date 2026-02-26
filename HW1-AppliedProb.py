import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import gmean


print("AUKUS")

'''

Exponent
KCI/McLaren
Jacobs Solutions
Joseph B Callaghan, Inc
Urban Engineers



Consider the breast cancer dataset we considered in class showing ages of patients detected
with breast cancer in a city hospital:
{36, 59, 78, 35, 53, 44, 19, 88, 39, 47,
44, 62, 31, 56, 25, 71, 66, 61, 50, 77,
61, 58, 73, 52, 67, 49, 33, 70, 55, 64,
49, 67, 41, 56, 75, 66, 37, 47, 84, 73,
57, 38, 48, 69, 86, 81, 72, 65, 53, 41}


$S--> Write a small program to compute the average value of the dataset and the median.
--> Construct a frequency distribution of the dataset using Sturges's rule for the number of
classes and rounding up the obtained expression.
--> Draw histogram of the frequency distribution and the frequency polygon.
--> Draw histogram of the cumulative frequency distribution and the ogive (less than type).
--> Illustrate how you would find the median of the frequency distribution you constructed.
How does it compare with the true median that you get from the above dataset (provide
the absolute value of the difference of the two)?
--> Compute the arithmetic average of the frequency distribution using class marks and compare the value with the true average of the dataset you computed with your program.

'''

UnSortedDataSet = [36, 59, 78, 35, 53, 44, 19, 88, 39, 47,
44, 62, 31, 56, 25, 71, 66, 61, 50, 77,
61, 58, 73, 52, 67, 49, 33, 70, 55, 64,
49, 67, 41, 56, 75, 66, 37, 47, 84, 73,
57, 38, 48, 69, 86, 81, 72, 65, 53, 41]



# list of ages in ascending order
dataSet = sorted(UnSortedDataSet)
print(dataSet)



# finds the Arithmetic Mean:  (sum of values)/(N)
def ArithmeticMean(dataSet):
    total = sum(dataSet)
    print(total)
    return total/len(dataSet)

'''
arithmeticMean = ArithmeticMean(dataSet)
print(arithmeticMean)
'''


# finds the Median of the dataSet
def Median(dataSet):
    N = len(dataSet)
    print(N)

    if N % 2 != 0:
        # if N is odd
        medianIndex = int((N+1)/2)
        median = dataSet[medianIndex-1]
        print(f"Number of values: {N} , Median: {median}")
    else:
        # if N is even
        medianIndex = ((N/2)+((N/2)+1))/2
        upper = dataSet[math.ceil(medianIndex)]
        lower = dataSet[math.floor(medianIndex)]

        median = ((upper-1) + (lower-1))/2
        
        print(f"Number of values: {N} , Upper/Lower Index {math.ceil(medianIndex)} , {math.floor(medianIndex)} , Upper/Lower Element: {upper} , {lower} , Median: {median}")


'''
Median(dataSet)
'''


def FrequencyDistribution(dataSet):
    N = len(dataSet)

    # Number of classes
    K = math.ceil(1 + 3.322*(math.log(N)))

    # Range
    R = max(dataSet) - min(dataSet)

    # Class size
    C = math.ceil(R/K)

    return C




classwidth = FrequencyDistribution(dataSet)


    # CLASS MIDPOINT
    # create a list of the midpoints?
    # midPoint = lowBound + (K - 1/2)*classWidth
def ClassMidpoints(values, classwidth, K):
    L = 1   # local counter to represent the number of classes
    lowerClassLimit = min(values) - .5
    midPoints = []
    while L <= K:
        midPoint = lowerClassLimit + (L - 1/2)*classwidth
        midPoints.append(midPoint)
        L +=1
    return midPoints

midPoints = ClassMidpoints(values, classwidth, K)
print(midPoints)



    #CLASS BOUNDARIES
def ClassBoundaries(values, classwidth, K):
    lowerBoundary = min(values) - 0.5
    return [lowerBoundary + i * classwidth for i in range(K + 1)]

print(ClassBoundaries(values, classwidth, K), "\n")



    # FREQUENCY TABLE
bins = ClassBoundaries(values, classwidth, K)
frequencies, _ = np.histogram(values, bins=bins)

class_labels = [
    f"{bins[i]} - {bins[i+1]}"
    for i in range(len(bins)-1)]

df = pd.DataFrame({"Class Interval": class_labels, "Frequency": frequencies})

fig, ax = plt.subplots()
ax.axis("off")

table = pd.plotting.table(ax, df, loc="center", cellLoc="center", colWidths=[0.3, 0.2])

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.show()         # Just un-comment to display the table







