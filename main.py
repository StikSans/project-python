from typing import List
from kramosa import kramosa
from gaus import gaus
from revers_matrica import inverse_matrix_method

A = [
  [2, -3, 1],
  [-3, 5, 3],
  [1, 1, -5]
  ]
B = [-1, -3, 2]



def main():
  # A, B = value_console()

  x, y, z = kramosa(A, B)
  # x, y, z = gaus(A, B) g
  # x, y, z = inverse_matrix_method(A, B)

  # print(result)
  print(f'Ответ: x: {x}, y: {y}, z: {z}')


def value_console():
  A: List[List[int]] = [
      [int(input('a11: ')), int(input('a12: ')), int(input('a13: ')),],
      [int(input('a21: ')), int(input('a22: ')), int(input('a23: ')),],
      [int(input('a31: ')), int(input('a32: ')), int(input('a33: ')),],
    ]

  B: List[int] = [int(input('b1: ')), int(input('b2: ')), int(input('b3: ')),]

  return A, B



main()