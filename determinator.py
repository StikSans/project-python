from typing import List

def determinator(a: List[List[int]]) -> int:
  return(a[0][0] * a[1][1] * a[2][2] + a[0][1] * a[1][2] * a[2][0] + a[0][2] * a[1][0] * a[2][1] 
          - a[0][2] * a[1][1] * a[2][0] - a[0][1] * a[1][0] * a[2][2] - a[0][0] * a[1][2] * a[2][1])

def determinant_2x2(A: List[List[int]]):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]