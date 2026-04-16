from matrices.operaciones import Operaciones

columnas = int(input("Columnas de la matriz: "))
filas = int(input("Filas de la matriz: "))

m = Operaciones().matriz(filas, columnas)
x = print(str(m))