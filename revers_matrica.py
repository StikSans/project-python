from typing import List
from determinator import determinator, determinant_2x2


 
def minor(A: List[List[float]], i: int, j: int):
    submatrix = [row[:j] + row[j+1:] for k, row in enumerate(A) if k != i]
    return determinant_2x2(submatrix)

def cofactors_matrix(A: List[List[float]]):
    cofactors = []
    for i in range(3):
        row = []
        for j in range(3):
            sign = (-1) ** (i + j)
            cofactor = sign * minor(A, i, j)
            row.append(cofactor)
        cofactors.append(row)
    return cofactors


def transpose(A: List[List[float]]):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def inverse_matrix(A: List[List[float]]):
    det = determinator(A)
    if det == 0:
        return None 
    cofactors = cofactors_matrix(A)
    adjugate = transpose(cofactors)
    inverse = [[adjugate[i][j] / det for j in range(3)] for i in range(3)]
    return inverse



def multiply_matrix_vector(A: List[List[float]], b: List[float]):
    result = [round( sum(A[i][j] * b[j] for j in range(len(b))), 5) for i in range(len(A))]
    return result


def inverse_matrix_method(A: List[List[float]], b: List[float]):
    A_inv = inverse_matrix(A)
    if A_inv is None:
        return None 
    return multiply_matrix_vector(A_inv, b)
