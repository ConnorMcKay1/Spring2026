'''
create a linear regression method that will take the regressionLine of all the columns of each file:
  EXAMPLE -->     xAxis_Column = df.iloc[:, FOR N-1  in File].tolist() yAxis_Column = df.iloc[:, 8].tolist()
'''
'''
then do this for each of the graphs; so just 'For N .csv files in directory, run NewRegressionLine method'
'''



import pandas as pd
import io
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from utilsStats import *


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

    #fig.savefig("my_plot.png")
    plt.show()




def DistributionPlot(df):
    print("plot the damn distributions!")

    num_plots = len(df.columns)

    cols = 3
    rows = (num_plots + cols - 1) // cols

    fig, axes = plt.subplots(
        rows,
        cols,
        figsize=(18, 6 * rows),
        constrained_layout=True
    )

    axes = axes.flatten()

    for i, col_name in enumerate(df.columns):
        ax = axes[i]

        data = df[col_name].dropna()  # safer

        mu, sigma = stats.norm.fit(data)

        x = np.linspace(data.min(), data.max(), 100)

        ax.hist(data, bins=30, density=True, alpha=0.6, label='Data Histogram')
        ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', label='Fitted Normal PDF')

        ax.set_title(f'Column: {col_name}')
        ax.set_xlabel(col_name)
        ax.set_ylabel('Density')
        ax.legend()

    for j in range(num_plots, len(axes)):
        fig.delaxes(axes[j])

    #fig.savefig("my_plot.png")
    plt.show()

