import math


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


--> Write a small program to compute the average value of the dataset and the median.
--> Construct a frequency distribution of the dataset using Sturges's rule for the number of
classes and rounding up the obtained expression.
--> Draw histogram of the frequency distribution and the frequency polygon.
--> Draw histogram of the cumulative frequency distribution and the ogive (less than type).
--> Illustrate how you would find the median of the frequency distribution you constructed.
How does it compare with the true median that you get from the above dataset (provide
the absolute value of the difference of the two)?
--> Compute the arithmetic average of the frequency distribution using class marks and compare the value with the true average of the dataset you computed with your program.

'''

# dataSet = [36, 59, 78, 35, 53, 44, 19, 88, 39, 47,
# 44, 62, 31, 56, 25, 71, 66, 61, 50, 77,
# 61, 58, 73, 52, 67, 49, 33, 70, 55, 64,
# 49, 67, 41, 56, 75, 66, 37, 47, 84, 73,
# 57, 38, 48, 69, 86, 81, 72, 65, 53, 41]

UnSortedDataSet = [36, 59, 78, 35, 53, 44, 19, 88, 39, 47,
44, 62, 31, 56, 25, 71, 66, 61, 50, 77,
61, 58, 73, 52, 67, 49, 33, 70, 55, 64,
49, 67, 41, 56, 75, 66, 37, 47, 84, 73,
57, 38, 48, 69, 86, 81, 72, 65, 53, 41, 69, 69, 69]



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



Median(dataSet)



