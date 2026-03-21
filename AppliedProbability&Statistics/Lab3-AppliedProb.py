import math
import numpy as np
import scipy

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



sampleList = np.random.randn(2000)


print(len(sampleList))

print(sampleList)






