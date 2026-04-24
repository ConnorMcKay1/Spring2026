import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

#  https://cs229.stanford.edu/lectures-spring2022/main_notes.pdf  pg.15
#  θ = (((X^T)*X)^-1)*(X^T)*(~>y)


def MatrixCreator(df):
    print("it's a dataFrame!")
    
    matrix = df.to_numpy()
    print(matrix)
    return matrix
    
    
def MatrixTranspose(matrix):
    print("it's a transpose!")