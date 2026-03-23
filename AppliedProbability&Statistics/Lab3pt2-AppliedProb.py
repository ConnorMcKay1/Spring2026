import numpy as np
import matplotlib.pyplot as plt
import math

n = 2000
values = np.random.randn(n)


K = math.ceil(3.322 * (math.log10(n)))
classwidth = math.ceil((max(values) - min(values)) / K)


K_new = K * 10
classwidth_new = (max(values) - min(values)) / K_new


bins_new = [min(values) + i * classwidth_new for i in range(K_new + 1)]
frequencies_new, _ = np.histogram(values, bins=bins_new)

# Create midpoints for the new frequency distribution
midpoints_new = [(bins_new[i] + bins_new[i + 1]) / 2 for i in range(K_new)]

# Plot the original histogram and the new histogram with more classes
plt.figure(figsize=(10, 6))

# Original histogram
plt.subplot(2, 1, 1)
plt.hist(values, bins=bins_new, edgecolor='black', alpha=0.6)
plt.title('Histogram with Original Number of Classes')
plt.xlabel('Value')
plt.ylabel('Frequency')

# New histogram with more classes (10x)
plt.subplot(2, 1, 2)
plt.hist(values, bins=bins_new, edgecolor='black', alpha=0.6)
plt.title(f'Histogram with {K_new} Classes (10x More)')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Now we can calculate the measures of dispersion for both the original and new number of classes.
def MeasuresOfDispersion(values, frequencies, bins, classwidth, K, classwidth_new, K_new):
    print("\n--- MEASURES OF DISPERSION ---\n")
    
    # Original Data (Raw Values)
    mean_value = np.mean(values)
    mad_mean = np.mean(np.abs(values - mean_value))
    mad_median = np.mean(np.abs(values - np.median(values)))
    std_dev = np.std(values, ddof=0)
    
    print("Mean (Raw Data):", mean_value)
    print("Mean Absolute Deviation about the mean (Raw Data):", mad_mean)
    print("Mean Absolute Deviation about the median (Raw Data):", mad_median)
    print("Standard Deviation (Raw Data):", std_dev)
    
    # Coefficient of Variation (CV) - Raw Data
    if mean_value != 0:
        cv = std_dev / abs(mean_value) * 100
        print("Coefficient of Variation (Raw Data):", cv)
    else:
        print("Coefficient of Variation (Raw Data): undefined (mean = 0)")

    # --- Using the New Frequency Distribution (more classes)
    bins_new = np.linspace(min(values), max(values), K_new + 1)
    frequencies_new, _ = np.histogram(values, bins=bins_new)
    
    # Calculate midpoints for new bins
    midpoints_new = [(bins_new[i] + bins_new[i + 1]) / 2 for i in range(K_new)]
    
    # Weighted mean for new classes
    mean_grouped = np.sum(midpoints_new * frequencies_new) / np.sum(frequencies_new)
    mad_mean_grouped = np.sum(frequencies_new * np.abs(midpoints_new - mean_grouped)) / np.sum(frequencies_new)
    variance_grouped = np.sum(frequencies_new * (midpoints_new - mean_grouped)**2) / np.sum(frequencies_new)
    std_dev_grouped = np.sqrt(variance_grouped)
    
    print("\n Using New Frequency Distribution with More Classes ")
    print("Mean (Grouped with more classes):", mean_grouped)
    print("MAD about mean (Grouped with more classes):", mad_mean_grouped)
    print("Standard Deviation (Grouped with more classes):", std_dev_grouped)
    
    # Coefficient of Variation (CV) - Grouped Data
    if mean_grouped != 0:
        cv_grouped = std_dev_grouped / abs(mean_grouped) * 100
        print("Coefficient of Variation (Grouped with More Classes):", cv_grouped)
    else:
        print("Coefficient of Variation (Grouped with More Classes): undefined (mean = 0)")

# runs the functions for both original and new classes
MeasuresOfDispersion(values, frequencies_new, bins_new, classwidth, K, classwidth_new, K_new)