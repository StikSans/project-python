from typing import List

def gaus(A: List[List[int]], b: List[int]):
    n = len(A)
    

    for i in range(n):

        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        

        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]
        

        if A[i][i] == 0:
            return None 
        
     
        for k in range(i+1, n):
            factor = A[k][i] / A[i][i]
            b[k] -= factor * b[i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
    
   
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = b[i] / A[i][i]
        for k in range(i-1, -1, -1):
            b[k] -= A[k][i] * x[i]
    
    return x

