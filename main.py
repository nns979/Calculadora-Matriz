from matrices.operaciones import Operaciones
import os

while True:
    try:
        columnas = int(input("Columnas de la matriz 1: "))
        filas = int(input("Filas de la matriz 1: "))

        m1 = Operaciones().matriz(filas, columnas)

        columnas = int(input("Columnas de la matriz 2: "))
        filas = int(input("Filas de la matriz 2: "))

        m2 = Operaciones().matriz(filas, columnas)

        os.system('cls')
        print("Matriz 1: ")
        print(m1)
        print("Matriz 2: ")
        print(m2)

        print(Operaciones().suma(m1, m2))
        break
    except ValueError:
        print("Error")
