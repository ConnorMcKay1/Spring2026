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


def DistributionPlot(df, mu, sigma):
    print("plot the damn distributions!")
    
    
  
    x = np.linspace(data.min(), data.max(), 100)

    plt.hist(data, bins=30, density=True, alpha=0.6, label='Data Histogram') # Plot the histogram of the data

    plt.plot(x, Distribution(x, mu, sigma), 'r-', label='Fitted Normal PDF') # Plot the fitted normal PDF (prob density func)

    plt.title(f'Histogram with Fitted Normal Distribution for Column: {strengthIndex}' )
    plt.xlabel(df.columns[strengthIndex] if len(df.columns) > 9 else 'Column 9 Value') # Use column name if available
    plt.ylabel('Density')
    plt.legend()
    plt.show()    
  
  




if __name__ == "__main__":
    print("hop on the dot")
    DistributionPlot()