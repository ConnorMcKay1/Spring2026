import math
import numpy as np
import scipy
from scipy.interpolate import interp1d
from scipy.optimize import brentq
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import sympy

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

#FrequencyTable()     # all ya have to do is un-comment to show Frequency Table



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
    
#Histogram()    # same deal with the Histogram

'''
The distribution is symetrical and is centered around Zero, as is expected for a Gaussian  distribution.
Even though a random number generator is used, / / / . . . .

'''


#   ***-----------------------QUESTION 3-----------------------***

# OGIVE (LESS & MORE THAN)

def Ogive():
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

    #plt.show()     # just so it doesn't pop-up
    
    return lessThan, moreThan
    
#Ogive()    # allas with the Ogive

lessThan, moreThan = Ogive()





def OgiveIntersection(lessThan, moreThan):
    print("INSIDE THE OGIVE MODULE")
    #print("LESS THAN: ", lessThan, "\n")
    print()
    #print("MORE THAN: ", moreThan)
    
    
    # turns the lessThan/moreThan List into a Numpy Array
    lessArray = np.array(lessThan)
    moreArray = np.array(moreThan)
    print("LESS THAN NUMPY: ", lessArray)
    print("MORE THAN NUMPY: ", moreArray)

    midPoints = ClassMidpoints(values, classwidth, K)
    x = np.array(midPoints)


    moreArray_shifted = np.roll(moreArray, -1)
    moreArray_shifted[-1] = 0

    lessLinear = interp1d(x, lessArray)
    moreLinear = interp1d(x, moreArray_shifted)

    def Difference(x):
        return lessLinear(x) - moreLinear(x)

    # find crossing interval
    diff = lessArray - moreArray
    # finds the index where the curves intersect (sign change)
    index = np.where(np.diff(np.sign(diff)) != 0)[0][0]

    intersection = brentq(Difference, x[index-1], x[index+2])
    print("X value at intersection: " ,intersection)
        
        
    yValue = lessLinear(intersection)   # or g_interp(x_cross), same value
    print("Y value at intersection:", yValue)


OgiveIntersection(lessThan, moreThan)


#plt.show()     # this was put here becuase I had to look at the graph after the data was outputted to terminal to check for accuracy


#   ***-----------------------QUESTION 4-----------------------***


def CompareMeans(values, frequencies, bins, classwidth, K):
    
    print("MEAN COMPARISON \n")

    # mean
    mean_raw = np.mean(values)
    print("Mean from data:", mean_raw)

    # mean from frequency distribution
    midPoints = ClassMidpoints(values, classwidth, K)
    midPoints = np.array(midPoints)

    frequencies_array = np.array(frequencies)

    mean_grouped = np.sum(midPoints * frequencies_array) / np.sum(frequencies_array)
    print("Mean from frequency distribution:", mean_grouped)

    # difference between freq mean and data mean
    difference = abs(mean_grouped - mean_raw)
    print("Difference:", difference)



#CompareMeans(values, frequencies, bins, classwidth, K)


def MeasuresOfDispersion(values, frequencies, bins, classwidth, K):
    print("\n--- MEASURES OF DISPERSION ---\n")
    
    # range
    data_range = np.max(values) - np.min(values)
    print("Range:", data_range)

    # Mean Absolute Deviation about the mean
    mean_value = np.mean(values)
    mad_mean = np.mean(np.abs(values - mean_value))
    print("Mean Absolute Deviation about the mean:", mad_mean)

    # Mean Absolute Deviation about the median
    median_value = np.median(values)
    mad_median = np.mean(np.abs(values - median_value))
    print("Mean Absolute Deviation about the median:", mad_median)

    # Standard Deviation
    std_dev = np.std(values, ddof=0)   # population standard deviation
    print("Standard Deviation:", std_dev)

    # Coefficient of Variation (CV = SD / mean)
    # making sure mean is not zero
    if mean_value != 0:
        cv = std_dev / abs(mean_value) * 100  # as percentage
        print("Coefficient of Variation (%):", cv)
    else:
        print("Coefficient of Variation (%): undefined (mean = 0)")

    # using frequency distribution from grouped data
    midPoints = np.array(ClassMidpoints(values, classwidth, K))
    frequencies_array = np.array(frequencies)

    # weighted mean
    mean_grouped = np.sum(midPoints * frequencies_array) / np.sum(frequencies_array)
    # weighted MAD about mean
    mad_mean_grouped = np.sum(frequencies_array * np.abs(midPoints - mean_grouped)) / np.sum(frequencies_array)
    # weighted standard deviation
    variance_grouped = np.sum(frequencies_array * (midPoints - mean_grouped)**2) / np.sum(frequencies_array)
    std_dev_grouped = np.sqrt(variance_grouped)

    print("\n Using Frequency Distribution")
    print("MEAN for grouped data:", mean_grouped)
    print("MAD about mean for grouped data:", mad_mean_grouped)
    print("STANDARD DEVIATION for grouped data:", std_dev_grouped)
    
    
MeasuresOfDispersion(values, frequencies, bins, classwidth, K)





