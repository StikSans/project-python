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

  del_x = determinator(D_x)

  del_y = determinator(D_y)

  del_z = determinator(D_z)

  x = del_x / del_A
  y = del_y / del_A
  z = del_z / del_A

  return x, y, z