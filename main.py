from matrices.operaciones import Operaciones
import os

while True:
    try:
        # 主菜单
        print("1) Suma de matriz")
        print("2) Resta de matriz")
        print("3) Multipicacion por escalar")
        opcion = int(input(""))

        if opcion == 1 or opcion == 2:

            # 输入矩阵filas和columnas
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

            if opcion == 1:
                print(Operaciones().suma(m1, m2))
            if opcion == 2:
                print(Operaciones().resta(m1, m2))

        if opcion == 3:
            columnas = int(input("Columnas de la matriz 1: "))
            filas = int(input("Filas de la matriz 1: "))
            matriz = Operaciones().matriz(filas, columnas)

            c1 = int(input("Escalar: "))
            
            os.system('cls')
            print("Matriz Original:")
            print(matriz)
            print("Escalar: ", c1, sep = "")
            print("")
            print(Operaciones().multi_escalar(c1, matriz))
        break
    except ValueError:
        print("Error")
