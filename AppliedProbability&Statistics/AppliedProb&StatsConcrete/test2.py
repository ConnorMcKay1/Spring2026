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

from main import LinearRegression


dataFile = "C:/Users/cmcka/OneDrive/Desktop/Spring2026/AppliedProbability&Statistics/AppliedProb&StatsConcrete/concrete_compressive_strength.csv"


listOfColumns = []

def DataReadIn(dataFile):
    df = pd.read_csv(dataFile)

    yAxis_columnIndex = 8

    # Y column (target)
    yAxis_Column = df.iloc[:, yAxis_columnIndex].tolist()

    # All other columns as X candidates
    listOfColumns = []
    for col_idx in range(len(df.columns)):
        if col_idx != yAxis_columnIndex:
            listOfColumns.append(df.iloc[:, col_idx].tolist())

    return listOfColumns, yAxis_Column, df


    # creates the window with all the X ingrediantes against output Y (strength)
def LinearRegression_AllColumns(listOfColumns, df):
    num_plots = len(listOfColumns)
    
    y_col_name = df.columns[8]
    x_columns = df.columns.drop(y_col_name)

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

        LinearRegression(x, y, axes[i], title=col_name)


    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # plt.savefig(f"concrete_compressive_strenght.png")
    # plt.close()
    plt.show()
    

if __name__ == "__main__":
    listOfColumns, yAxis_Column, df = DataReadIn(dataFile)
    LinearRegression_AllColumns(listOfColumns, df)