'''
I think I'm going to make this a file for doing the line regression of the graphs produced in main.py
'''

# or import the df/results you need and call plotting functions from test1.py
from scipy import stats


def LinearRegression(xAxis_Column, yAxis_Column):
    results = stats.linregress(xAxis_Column, yAxis_Column)
    
    print(f"R-squared: {results.rvalue**2:.6f}")

