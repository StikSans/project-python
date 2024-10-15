from typing import List

def gaus(A: List[List[int]], b: List[int]):
    n = len(A)
    
    # Приведение системы к верхнетреугольному виду
    for i in range(n):
        # Поиск максимального элемента в текущем столбце для избежания деления на ноль
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        
        # Обмен строк
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]
        
        # Проверка на нулевой элемент на главной диагонали
        if A[i][i] == 0:
            return None  # Нет решения (система несовместна или имеет бесконечное множество решений)
        
        # Приведение текущего элемента на диагонали к 1 и зануление элементов ниже диагонали
        for k in range(i+1, n):
            factor = A[k][i] / A[i][i]
            b[k] -= factor * b[i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
    
    # Обратный ход для нахождения решения
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = b[i] / A[i][i]
        for k in range(i-1, -1, -1):
            b[k] -= A[k][i] * x[i]
    
    return x

