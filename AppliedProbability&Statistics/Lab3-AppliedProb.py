import math
import numpy as np
import scipy
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

'''
Instruction: For this assignment, you will generate datasets by drawing samples
from the Standard Normal distribution and the Uniform distribution and then will
compute various measures of center and dispersion on the datasets.

Generate 2000 samples from the Standard Normal distribution using the
function numpy.random.randn().

• Using the Sturges's rule for the number of classes, construct a frequency
distribution of the above dataset. Display the frequency table and show the
upper and lower class limits. You can assume that the class limits are the
same as the class boundaries in this case.

• Draw the histogram and frequency polygon of the frequency distribution.
Comment on the shape of the histogram. How does it look like?

• Generate the ogives (more than and less than types) in a single figure and
then find the median of the frequency distribution using the point of
intersection of the two ogives or using the formula to compute the median
for a frequency distribution (see updated Slides_3 on the Measures of
Central Tendency) and compare the same with the median of the 2000
samples.

• Calculate the Arithmetic Mean of the given dataset and then calculate the
same from the Frequency Distribution (using class marks). Display the
difference of the two.

• Calculate the following measures of dispersion: Range, Mean Absolute
Deviation about the mean, Mean Absolute Deviation about the median,
Standard Deviation, Coefficient of Variation.

• Increase the number of classes by a factor of 10 and comment on how the
distribution changes.

'''

n = 2000

# 2000 values
values = np.random.randn(n)


# number of class
K = math.ceil(3.322*(math.log10(n)))

print(values)

print(K)


#   ***-----------------------QUESTION 1-----------------------***

# CLASS WIDTH
def ClassWidth(values, K):
    classwidth = math.ceil((max(values) - min(values)) / K)
    return classwidth


classwidth = ClassWidth(values, K)


# CLASS BOUNDARIES
def ClassBoundaries(values, classwidth, K):
    lowerBoundary = min(values) - 0.5
    return [lowerBoundary + i * classwidth for i in range(K + 1)]


bins = ClassBoundaries(values, classwidth, K)   # this is used for both the table and the graph
frequencies, _ = np.histogram(values, bins=bins)

# FREQUENCY TABLE PLOT

def FrequencyTable():
    class_labels = [
        f"{bins[i]} - {bins[i+1]}"
        for i in range(len(bins)-1)]

    df = pd.DataFrame({"Class Interval": class_labels, "Frequency": frequencies})

    fig, ax = plt.subplots()
    ax.axis("off")

    table = pd.plotting.table(ax, df, loc="center",
                          cellLoc="center", colWidths=[0.3, 0.2])

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    plt.show()

FrequencyTable()     # all ya have to do is un-comment to show Frequency Table



#   ***-----------------------QUESTION 2-----------------------***

# HISTOGRAM AND FREQUENCY POLYGON

def ClassMidpoints(values, classwidth, K):
    L = 1   # local counter to represent the number of classes
    lowerClassLimit = min(values) - .5
    midPoints = []
    while L <= K:
        midPoint = lowerClassLimit + (L - 1/2)*classwidth
        midPoints.append(midPoint)
        L += 1
    return midPoints


def Histogram():

    midPoints = ClassMidpoints(values, classwidth, K)
    # print(midPoints)

    plt.hist(values, bins=bins, edgecolor='black', alpha=0.6)

    plt.xlabel("Class Intervals")
    plt.ylabel("Frequency/Tallies")
    plt.title("Histogram w/ Frequency Polygon")
    plt.xticks(bins)

    # Polygon Line and bringing it to the x-axis
    x_poly = [bins[0]] + midPoints + [bins[-1]]
    y_poly = [0] + list(frequencies) + [0]
    plt.plot(x_poly, y_poly, marker='o', color='red', linestyle='-')

    plt.show()
    
Histogram()

'''
The distribution is symetrical and is centered around Zero, as is expected for a Gaussian  distribution.
Even though a random number generator is used, / / / . . . .

'''

