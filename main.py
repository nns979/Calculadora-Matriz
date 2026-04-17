from matrices.operaciones import Operaciones
import os

while True:
    try:
        # 主菜单
        print("1) Suma de matriz")
        print("2) Resta de matriz")
        print("3) Multipicacion por escalar")
        print("4) Multiplicacion de matriz")
        print("7) Salir")
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

        if opcion == 4:
            columnas = int(input("Columnas de la matriz A: "))
            filas = int(input("Filas de la matriz A: "))

            m1 = Operaciones().matriz(filas, columnas)

            columnas = int(input("Columnas de la matriz B: "))
            filas = int(input("Filas de la matriz B: "))

            m2 = Operaciones().matriz(filas, columnas)

            os.system('cls')
            print("Matriz A: ")
            print(m1)
            print("Matriz B: ")
            print(m2)

            print(Operaciones().multiplicacion(m1, m2))

        if opcion == 7:
            break
    except ValueError:
        print("Error")
