import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

#  https://cs229.stanford.edu/lectures-spring2022/main_notes.pdf  pg.15
#  θ = (((X^T)*X)^-1)*(X^T)*(~>y)


def MatrixCreator(df):    
    matrix = df.to_numpy()
    return matrix


def MatrixMultiplier(matrix1, matrix2):
    result = np.matmul(matrix1, matrix2)
    
    print("rows times columns is how you do it, or just use numpy")
    print(result)
    
    
def MatrixTranspose(df):    
    matrix = MatrixCreator(df)
    transposedMatrix = np.transpose(matrix)
    return transposedMatrix


# for non-square matrix:
#     numpy.linalg.pinv (Moore-Penrose Pseudoinverse) --> np.linalg.pinv(A)
#     numpy.linalg.lstsq (Least-Squares Solution)     --> np.linalg.lstsq(A, b)
def MatrixInverse(matrix):
    inversedMatrix = np.linalg.pinv(matrix)
    return inversedMatrix



#   this if for y (target vector)
def TargetVector(df):
    y = df.iloc[:, -1].to_numpy()
    return y
    


#  θ = (((X^T)*X)^-1)*(X^T)*(~>y)
def ThetaFinder(df):
    X = MatrixCreator(df)
    X_T = MatrixTranspose(df)
    y = TargetVector(df)
    
    X_T_mult_X =  MatrixMultiplier(X_T, X)
    X_T_mult_y = MatrixMultiplier(X_T, y)
    
    
    
    theta = (MatrixInverse((X_T*X)))*(X_T)*(TargetVector(df))
    
    theta = ()
    
        
    print("Theta is worse than Beta")