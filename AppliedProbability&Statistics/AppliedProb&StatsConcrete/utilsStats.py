import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


'''
mean, variance  ->~done
correlation     ->~done
regression slope
covariance
'''

def Mean(data):
    print(np.mean(data))
    
    
def StandardDeviation(data):
    print(np.std(data))
    
def Correlation(X, Y):
    matrix = np.corrcoef(X, Y)
    correlation = matrix[0, 1] 
    print(correlation)
    

def RegressionLine(X, Y):
    result = stats.linregress(X, Y)
    print(result)
    

def Covariance(X, Y):
    matrix = np.cov(X, Y, rowvar = False)
    covariance = matrix[0, 1] 
    print(covariance)

