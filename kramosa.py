from determinator import determinator
from typing import List

def kramosa(a: List[List[int]], b: List['int']): 
  D_x = [
        [b[0], a[0][1], a[0][2]],
        [b[1], a[1][1], a[1][2]],
        [b[2], a[2][1], a[2][2]],
    ]

  D_y = [
        [a[0][0], b[0], a[0][2]],
        [a[1][0], b[1], a[1][2]],
        [a[2][0], b[2], a[2][2]],
    ]

  D_z = [
        [a[0][0], a[0][1], b[0]],
        [a[1][0], a[1][1], b[1]],
        [a[2][0], a[2][1], b[2]],
    ]


  del_A = determinator(a)
  if del_A == 0: return "Не льзя продожить" 
  del_x = determinator(D_x)
  del_y = determinator(D_y)
  del_z = determinator(D_z)

  

  x = del_x / del_A
  y = del_y / del_A
  z = del_z / del_A

  return x, y, z



def kramosa4_4(a: List[List[int]], b: List['int']): 
  D_x = [
        [b[0], a[0][1], a[0][2], a[0][3]],
        [b[1], a[1][1], a[1][2], a[0][3]],
        [b[2], a[2][1], a[2][2], a[0][3]],
        [b[3], a[3][1], a[3][2], a[3][3]],
    ]

  D_y = [
        [a[0][0], b[0], a[0][2], a[0][3]],
        [a[1][0], b[1], a[1][2], a[1][2]],
        [a[2][0], b[2], a[2][2], a[2][2]],
        [a[3][0], b[3], a[3][2], a[3][3]],
    ]

  D_z = [
        [a[0][0], a[0][1], b[0], a[0][3]],
        [a[1][0], a[1][1], b[1], a[1][3]],
        [a[2][0], a[2][1], b[2], a[2][3]],
        [a[2][0], a[2][1], b[3], a[3][3]],
    ]
  
  D_t = [
        [a[0][0], a[0][1], a[0][2], b[0]],
        [a[1][0], a[1][1], a[1][2], b[1]],
        [a[2][0], a[2][1], a[2][2], b[2]],
        [a[2][0], a[2][1], a[3][2], b[3]],
    ]


  # del_A = determinator(a)
  # del_x = determinator(D_x)
  # del_y = determinator(D_y)
  # del_z = determinator(D_z)
  # del_t = determinator(D_t)

  # x = del_x / del_A
  # y = del_y / del_A
  # z = del_z / del_A
  # t = del_t / del_A

  # return x, y, z, t