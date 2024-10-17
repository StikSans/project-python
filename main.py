from typing import List
from kramosa import kramosa, kramosa4_4
from gaus import gaus
from revers_matrica import inverse_matrix_method


#2 ВАРИАНТ под цыфрой 2
# A = [
#   [2, -3, 1],
#   [-3, 5, 3],
#   [1, 1, -5]
#   ]
# B = [-1, -3, 2]



def main():
  A, B = value_console()
  # A, B = value_console4()
  a = kramosa(A, B)
  # x, y, z = gaus(A, B) 
  # x, y, z, t = gaus(A, B) 
  # x, y, z = inverse_matrix_method(A, B)

  # print(result)

  if type(a) != str:
     print(f'Ответ: {a[0]}, y: {a[1]}, z: {a[2]} ')
  else:
    print("Нельзя найти det_A = 0")
  # print(f'Ответ: x: {x}, y: {y}, z: {z} t: {t}')


def value_console():
  A: List[List[int]] = [
      [int(input('a11: ')), int(input('a12: ')), int(input('a13: ')),],
      [int(input('a21: ')), int(input('a22: ')), int(input('a23: ')),],
      [int(input('a31: ')), int(input('a32: ')), int(input('a33: ')),],
    ]

  B: List[int] = [int(input('b1: ')), int(input('b2: ')), int(input('b3: ')),]

  return A, B

def value_console4():
  A: List[List[int]] = [
      [int(input('a11: ')), int(input('a12: ')), int(input('a13: ')), int(input('a14: '))],
      [int(input('a21: ')), int(input('a22: ')), int(input('a23: ')), int(input('a24: '))],
      [int(input('a31: ')), int(input('a32: ')), int(input('a33: ')), int(input('a34: '))],
      [int(input('a41: ')), int(input('a42: ')), int(input('a43: ')), int(input('a44: '))],
    ]

  B: List[int] = [int(input('b1: ')), int(input('b2: ')), int(input('b3: ')), int(input('b4: '))]

  return A, B



main()