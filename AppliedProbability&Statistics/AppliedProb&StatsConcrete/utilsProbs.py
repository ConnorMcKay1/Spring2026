import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

#  https://cs229.stanford.edu/lectures-spring2022/main_notes.pdf  pg.15
#  θ = (((X^T)*X)^-1)*(X^T)*(~>y)


def MatrixCreator(df):    
    matrix = df.to_numpy()
    return matrix
    
    
def MatrixTranspose(df):    
    matrix = MatrixCreator(df)
    transposedMatrix = np.transpose(matrix)
    return transposedMatrix


# for non-square matrix:
#     numpy.linalg.pinv (Moore-Penrose Pseudoinverse) --> np.linalg.pinv(A)
#     numpy.linalg.lstsq (Least-Squares Solution)     --> np.linalg.lstsq(A, b)
def MatrixInverse(df):
    matrix = MatrixCreator(df)
    inversedMatrix = np.linalg.pinv(matrix)
    return inversedMatrix
    
    