import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

'''

SIMPLE RELATIONSHIPS:
    Which variables are related to the output?
    Are relationships linear or monotonic?
        
PREDICTIVE MODELING:
    How well can I predict the output from the inputs?
    ****Which variables matter most?****  use this to find out which variable affects strenght the most?

EFFECTS OF INTERACTION:
    Do variables combine in not obvious ways?


  ***************************
** OvEr ArChInG ReSeArCh AiM **

PREDICT CONCRETE STRENGHT based on the ingredient input amounts/auntities?
    --> Wounldn't this just yield the "ideal"
    *   concrete mix? (ignoring prediction errors obviously)    *
    **************************************************************

'''
        #   SciPy Documentation Recomended
    # Make All 8 Variables in Scatter Plots
    # Look into Correlation Coefficient (r)
    #   (Measures the Strgth & dir. of linear relationship)
    # Regression Analysis: would create a "line of best fit"
    #                      to model the relationship & make predictions                      
##################################################################

from utilsStats import *


print("test test turnip \n")

    # This is 'concrete_compresssive_strencth.csv
#dataFile = "C:/Users/cmcka/OneDrive/Desktop/Spring2026/AppliedProbability&Statistics/AppliedProb&StatsConcrete/concrete_compressive_strength.csv"

    # This is 'concrete_resistance.csv
#dataFile = "C:/Users/cmcka/OneDrive/Desktop/Spring2026/AppliedProbability&Statistics/AppliedProb&StatsConcrete/Concrete_Resistance.csv"

    # This is Dataset2 - Data.csv
dataFile = "C:/Users/cmcka/OneDrive/Desktop/Spring2026/AppliedProbability&Statistics/AppliedProb&StatsConcrete/Dataset2 - Data.csv"


    # just reading in the 1 of the data sets to get the 2 columns for the scatter
    # for the scatter plot method below
def DataReadIn(csvFile):
    df = pd.read_csv(csvFile)
    
    xAxis_Column = df.iloc[:, 0].tolist()
    yAxis_Column = df.iloc[:, 8].tolist()
    return xAxis_Column, yAxis_Column, df

xAxis_Column, yAxis_Column, df = DataReadIn(dataFile)


    # this is just a method for taking the 2 columns from the csv file
    # and plotting them using ScatterPlot to look for any relationships
def ScatterPlot(xAxis_Column, yAxis_Column, df):
    x = np.array([xAxis_Column])
    y = np.array([yAxis_Column])
    print(df)
    plt.scatter(x, y, s=10)
    plt.xlabel('Cement')
    plt.ylabel('Concrete Strength')
    plt.title('Cement --> Concrete Strength')
    plt.show()


#ScatterPlot(xAxis_Column, yAxis_Column, df)



def LinearRegression(xAxis_Column, yAxis_Column, ax, title=""):
    result = stats.linregress(xAxis_Column, yAxis_Column)

    x = np.array(xAxis_Column)
    y = np.array(yAxis_Column)

    m = result.slope
    b = result.intercept
    regressionLine = m * x + b  

    ax.plot(x, y, 'bo', markersize=3)
    ax.plot(x, regressionLine, 'r')
    ax.set_title(title)
    ax.set_title(title, fontsize = 10)

    return result

def UtilsPrinter():
    print(xAxis_Column)
    print("----------------------------------------------------------------------------------------")
    print(yAxis_Column)
    print("------------------")
    Mean(xAxis_Column)
    print("------------------")
    StandardDeviation(xAxis_Column)
    print("------------------")
    Correlation(xAxis_Column, yAxis_Column)
    print("------------------")
    RegressionLine(xAxis_Column, yAxis_Column)
    print("------------------")
    Covariance(xAxis_Column, yAxis_Column)


def test(df):
    data = df.iloc[:, 8]
    
    mu, sigma = stats.fit(data)

    x = np.linspace(min(data), max(data), 100)

    plt.hist(data, bins=30, density=True, alpha=0.6)
    plt.plot(x, stats.pdf(x, mu, sigma), 'r')
    plt.title("Histogram + Fitted Normal")
    plt.show()
    
    


if __name__ == "__main__":
    test(df)
    print()


    #LinearRegression(xAxis_Column, yAxis_Column)