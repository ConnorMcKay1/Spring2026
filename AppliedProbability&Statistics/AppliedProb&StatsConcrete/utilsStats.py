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


    ''' LEGACY '''
    ## This was for printing all of the REGRESSION LINES for all of the INGREDIENTS
    # creates the window with all the X ingrediantes against output Y (strength)
def LinearRegression_AllColumns(df):
    num_plots = len(df-1)
    strengthIndex = df[num_plots]
    
    y_col_name = df.columns[strengthIndex]              # change based on # of ingredients
    x_columns = df.columns.drop(y_col_name)         #                    (for Strength)

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

        RegressionLine(x, y, axes[i], title=col_name)


    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # plt.savefig(f"Concrete_Resistance.png")
    # plt.close()
    plt.show()
    
