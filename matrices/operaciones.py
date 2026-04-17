from matrices.matriz import Matriz

class Operaciones:

    # 创建矩阵，也就是初始矩阵
    def matriz(self, filas, columnas):
        while True:
            matriz = []

            for i in range(filas):
                
                while True:

                    try:
                        fila_matriz_2 = []
                        fila_matriz = input(f"Fila Numero {i} (Todos debe de tener el mismo COLUMNA): ").split()
                        if len(fila_matriz) != columnas:
                            raise ValueError("Número incorrecto de columnas")

                        for j in range(len(fila_matriz)):
                            fila_matriz_2.append(int(fila_matriz[j]))

                        matriz.append(fila_matriz_2)
                        print("")
                        break
                            
                    except Exception:
                        print("Entrada inválida, intenta otra vez")

            try:
                m = Matriz(matriz)
                print("Matriz válida")
                break
            except ValueError as e:
                print(e)

        self.matriz = m
        return m

    # 矩阵相加
    def suma(self, m1, m2):
        suma_m = []

        if m1.filas != m2.filas or m1.columnas != m2.columnas:
            return print("Error, Las columnas y filas debe de ser igua para hacer suma!")
            
        for i in range(m1.filas):
            temp = []
            for j in range(m1.columnas):
                temp.append(m1.valores[i][j] + m2.valores[i][j])

            suma_m.append(temp)

        return Matriz(suma_m)

    # 矩阵相减
    def resta(self, m1, m2):
        resta_m = []

        if m1.filas != m2.filas or m1.columnas != m2.columnas:
            return print("Error, Las columnas y filas debe de ser igua para hacer reta!")
            
        for i in range(m1.filas):
            temp = []
            for j in range(m1.columnas):
                temp.append(m1.valores[i][j] - m2.valores[i][j])

            resta_m.append(temp)
            
        return Matriz(resta_m)
    
    # 向量矩阵
    def multi_escalar(self, c1, matriz):
        escalar = []
        for i in range(matriz.filas):
            temp = []
            for j in range(matriz.columnas):
                temp.append(c1 * matriz.valores[i][j])

            escalar.append(temp)
        return Matriz(escalar)