import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


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




print("test test turnip \n")

    # This is currently 'concrete_compresssive_strencth.csv
dataFile = "C:/Users/cmcka/OneDrive/Desktop/Spring2026/AppliedProbability&Statistics/AppliedProb&StatsConcrete/concrete_compressive_strength.csv"


    # just reading in the 1 of the data sets to get the 2 columns for the scatter
    # for the scatter plot method below
def DataReadIn(csvFile):
    df = pd.read_csv(csvFile)
    selected_columns = df[['Cement', 'Concrete Compressive Strength']]
    xAxis_Column = df['Cement'].tolist()
    yAxis_Column = df['Concrete Compressive Strength'].tolist()
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

#good night 
ScatterPlot(xAxis_Column, yAxis_Column, df)
