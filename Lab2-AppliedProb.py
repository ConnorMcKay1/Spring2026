#import counter
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import gmean


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


#   ***-----------------------QUESTION 1-----------------------***

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
print("Class Width:", classwidth, "\n")



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





#   ***-----------------------QUESTION 2-----------------------***

    # FREQUENCY HISTOGRAM
plt.hist(values, bins=bins, edgecolor='black', alpha=0.6)

plt.xlabel("Class Intervals")
plt.ylabel("Frequency/Tallies")
plt.title("Histogram w/ Frequency Polygon")
plt.xticks(bins)

x_poly = [bins[0]] + midPoints + [bins[-1]]     # Polygon Line and bringing it to the x-axis
y_poly = [0] + list(frequencies) + [0]
plt.plot(x_poly, y_poly, marker='o', color='red', linestyle='-')

plt.show()     # Just un-comment to display the histogram





#   ***-----------------------QUESTION 3-----------------------***
    # LESS THAN / MORE THAN
lessThan = []
lessTotal = 0
for f in frequencies:
    lessTotal += f
    lessThan.append(lessTotal)


moreThan = []
moreTotal = 0
for f in reversed(frequencies):
    moreTotal += f
    moreThan.append(moreTotal)
moreThan.reverse()      

upper_bounds = bins[1:]  
lower_bounds = bins[:-1]


plt.figure(figsize=(8,5))

plt.plot(upper_bounds, lessThan, marker='o', color='blue', linestyle='-', label='Less-than')
plt.plot(lower_bounds, moreThan, marker='s', color='red', linestyle='--', label='More-than')

plt.xlabel('Value')
plt.ylabel('Cumulative Frequency')
plt.title('Less-than and More-than Ogives')
plt.legend()
plt.grid(True)

plt.show()     # Same deal with the Ojive





#   ***-----------------------QUESTION 4-----------------------***

'''
FINNISH THE CALCULATIONS BY FINDING THE INTERSECTION OF THE 2 OJIVE LINES

'''


medianValue = np.median(values)

modeResult = stats.mode(values, keepdims=True)
modeValues = modeResult.mode
modeCount = modeResult.count

print("Median:", medianValue)
print("Mode(s):", modeValues, "with frequency:", modeCount, "\n")





#   ***-----------------------QUESTION 5-----------------------***
arithmeticMean = np.mean(values)
print("Exact Arithmetic Mean:", arithmeticMean)

frequencySum = sum(f * m for f, m in zip(frequencies, midPoints))
groupedMean = frequencySum / sum(frequencies)

print("Grouped Arithmetic Mean:", groupedMean)
difference = arithmeticMean - groupedMean
print("Difference (Arithmetic Mean - Grouped Mean):", difference, '\n')





#   ***-----------------------QUESTION 6-----------------------***
geometricMean = gmean(values)
print("Geometric Mean:", geometricMean)





#   ***-----------------------QUESTION 7-----------------------***
harmonic_mean = len(values) / np.sum(1/np.array(values))
print("Harmonic Mean:", harmonic_mean)













