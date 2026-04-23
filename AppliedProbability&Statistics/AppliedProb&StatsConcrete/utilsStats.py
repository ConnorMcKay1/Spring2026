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
    mean = (np.mean(data))
    return mean
    
def StandardDeviation(data):
    standard_deviation = (np.std(data))
    return standard_deviation
    
def Correlation(X, Y):
    matrix = np.corrcoef(X, Y)
    correlation = matrix[0, 1] 
    return correlation
    

def RegressionLine(X, Y):
    result = stats.linregress(X, Y)
    return result
    

def Covariance(X, Y):
    matrix = np.cov(X, Y, rowvar = False)
    covariance = matrix[0, 1] 
    return covariance

    # get the distribution of a SINGLE column
def Distribution(df):
    
    # number of columns in the dataFrams
    NumberOfColumns = (len(df.columns))
    
    print(NumberOfColumns)
    
    #strengthIndex = (len(df.columns)-1)  # this can be used to manually select what column to check the distribution of
    
    # for column in enumerate(df.columns):
    #     data = df.iloc[:, column]
    #     mu, sigma = stats.norm.fit(data)
    #     print("this is the mean(mu): ", mu, " this is the variance(sigma): ", sigma)



    # mu, sigma = stats.norm.fit(data)
    
    # print("this is the mean(mu): ", mu, " this is the variance(sigma): ", sigma)
    
    # return mu, sigma
    

def heynowMorningGloryOasis():
    print()


    ''' LEGACY '''
    ## This was for printing all of the REGRESSION LINES for all of the INGREDIENTS
    # creates the window with all the X ingrediantes against output Y (strength)
def LinearRegression_AllColumns(df):

    y_col_name = df.columns[-1]
    x_columns = df.columns[:-1]

    num_plots = len(x_columns)

    cols = 3
    rows = (num_plots + cols - 1) // cols

    fig, axes = plt.subplots(
        rows,
        cols,
        figsize=(18, 6 * rows),
        constrained_layout=True
    )

    axes = axes.flatten()

    for i, col_name in enumerate(x_columns):
        x = df[col_name]
        y = df[y_col_name]

        result = RegressionLine(x, y)

        ax = axes[i]

        ax.scatter(x, y)

        slope = result.slope
        intercept = result.intercept
        ax.plot(x, slope * x + intercept, color='red')      # the regression line itself 

        ax.set_title(col_name)
        ax.set_xlabel(col_name)
        ax.set_ylabel(y_col_name)

    for j in range(num_plots, len(axes)):
        fig.delaxes(axes[j])

    plt.show()