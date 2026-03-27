import numpy as np
import matplotlib.pyplot as plt
import math

n = 2000
values = np.random.randn(n)

K = math.ceil(3.322 * (math.log10(n)))
classWidth = math.ceil((max(values) - min(values)) / K)

KNew = K * 10
classWidthNew = (max(values) - min(values)) / KNew

binsNew = [min(values) + i * classWidthNew for i in range(KNew + 1)]
frequenciesNew, _ = np.histogram(values, bins=binsNew)

# Create midpoints for the new frequency distribution
midpointsNew = [(binsNew[i] + binsNew[i + 1]) / 2 for i in range(KNew)]

# Plot the original histogram and the new histogram with more classes
plt.figure(figsize=(10, 6))

# Original histogram
plt.subplot(2, 1, 1)
plt.hist(values, bins=binsNew, edgecolor='black', alpha=0.6)
plt.title('Histogram with Original Number of Classes')
plt.xlabel('Value')
plt.ylabel('Frequency')

# New histogram with more classes (10x)
plt.subplot(2, 1, 2)
plt.hist(values, bins=binsNew, edgecolor='black', alpha=0.6)
plt.title(f'Histogram with {KNew} Classes (10x More)')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Now we can calculate the measures of dispersion for both the original and new number of classes.
def measuresOfDispersion(values, frequencies, bins, classWidth, K, classWidthNew, KNew):
    print("\n--- *** MEASURES OF DISPERSION *** ---\n")
    
    # Original Data (generated values)
    meanValue = np.mean(values)
    madMean = np.mean(np.abs(values - meanValue))
    madMedian = np.mean(np.abs(values - np.median(values)))
    stdDev = np.std(values, ddof=0)
    
    print("Mean (Raw Data):", meanValue)
    print("Mean Absolute Deviation about the mean (Raw Data):", madMean)
    print("Mean Absolute Deviation about the median (Raw Data):", madMedian)
    print("Standard Deviation (Raw Data):", stdDev)
    
    # Coefficient of Variation (CV) - Raw Data
    if meanValue != 0:
        cv = stdDev / abs(meanValue) * 100
        print("Coefficient of Variation (Raw Data):", cv)
    else:
        print("Coefficient of Variation (Raw Data): undefined (mean = 0)")

    # --- Using the New Frequency Distribution (more classes)
    binsNew = np.linspace(min(values), max(values), KNew + 1)
    frequenciesNew, _ = np.histogram(values, bins=binsNew)
    
    # Calculate midpoints for new bins
    midpointsNew = [(binsNew[i] + binsNew[i + 1]) / 2 for i in range(KNew)]
    
    # Weighted mean for new classes
    meanGrouped = np.sum(midpointsNew * frequenciesNew) / np.sum(frequenciesNew)
    madMeanGrouped = np.sum(frequenciesNew * np.abs(midpointsNew - meanGrouped)) / np.sum(frequenciesNew)
    varianceGrouped = np.sum(frequenciesNew * (midpointsNew - meanGrouped)**2) / np.sum(frequenciesNew)
    stdDevGrouped = np.sqrt(varianceGrouped)
    
    print("\n Using New Frequency Distribution with More Classes ")
    print("Mean (Grouped with more classes):", meanGrouped)
    print("MAD about mean (Grouped with more classes):", madMeanGrouped)
    print("Standard Deviation (Grouped with more classes):", stdDevGrouped)
    
    # Coefficient of Variation (CV) - Grouped Data
    if meanGrouped != 0:
        cvGrouped = stdDevGrouped / abs(meanGrouped) * 100
        print("Coefficient of Variation (Grouped with More Classes):", cvGrouped)
    else:
        print("Coefficient of Variation (Grouped with More Classes): undefined (mean = 0)")

# runs the function
measuresOfDispersion(values, frequenciesNew, binsNew, classWidth, K, classWidthNew, KNew)