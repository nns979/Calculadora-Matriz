from matrices.operaciones import Operaciones
from matrices.matriz import Matriz
from pathlib import Path
import os

while True:
    try:
        # 主菜单
        print("1) Suma de matriz")
        print("2) Resta de matriz")
        print("3) Multipicacion por escalar")
        print("4) Multiplicacion de matriz")
        print("5) Matriz inversa")
        print("6) Matriz transpuesta")
        print("7) Sistema de ecuaciones lineales(No terminado)")
        print("8) Guadar mi respuesta")
        print("9) Leer matriz desde archivo")
        print("10) Salir")
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
                print("Suma de matriz")
                resultado = Operaciones().suma(m1, m2)
                print(resultado)
            if opcion == 2:
                print("Resta de matriz")
                resultado = Operaciones().resta(m1, m2)
                print(resultado)

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
            print("Multipicacion por escalar")
            resultado = Operaciones().multi_escalar(c1, matriz)
            print(resultado)

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
            print("")
            print("Matriz multiplicado: ")
            resultado = Operaciones().multiplicacion(m1, m2)
            print(resultado)

        if opcion == 5:
            columnas = int(input("Columnas de la matriz A: "))
            filas = int(input("Filas de la matriz A: "))

            matriz = Operaciones().matriz(filas, columnas)
            os.system('cls')
            print("Matriz Original:")
            print(matriz)
            print("")
            print("Matriz Inversa")
            resultado = Operaciones().inversa(matriz)
            print(resultado)
        
        if opcion == 6:
            columnas = int(input("Columnas de la matriz: "))
            filas = int(input("Filas de la matriz: "))
            matriz = Operaciones().matriz(filas, columnas)
            
            os.system('cls')
            print("Matriz Original:")
            print(matriz)
            print("")
            print("Matriz transpuesta")
            resultado = Operaciones().transpuesta(matriz)
            print(resultado)
        
        if opcion == 7:
            print("No terminado..")

        # 保存
        if opcion == 8:
            archivo = Path(__file__).parent / ".." / "resources" / "matrices" / "matriz.txt"
            with open(archivo, "w") as f:
                f.write(str(resultado))
            
            print("Su resultado guadardo en carpeta / .. / resources / matrices / matriz.txt")

        if opcion == 9:
            archivo = Path(__file__).parent / ".." / "Calculadora-Matriz" / "resources" / "matrices" / "matriz.txt"
            matriz = []

            with open(archivo, "r") as f:

                for linea in f:
                    if not linea.strip():
                        continue
                    
                    fila = linea.strip().replace("[","").replace("]","").replace(",","").split()
                    temp = []
                    for x in fila:
                        temp.append(float(x))

                    matriz.append(temp)

            os.system('cls')
            m = Matriz(matriz)
            print("Matriz del archivo:")
            print(m)

        if opcion == 10:
            break

    except ValueError:
        print("Error")

