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
            return print("Error! Para hacer suma, Las columnas y filas debes de ser igual!")
            
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
            return print("Error! Para hacer resta, Las columnas y filas debes de ser igual!")
            
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
    
    # 矩阵互乘
    def multiplicacion(self, m1, m2):
        multipicar = []
        
        if m1.columnas != m2.filas:
            return print("Error! Columna de primer matriz y la fila de 2 matriz debe de ser igual!")
        
        for i in range(m1.filas):
            temp = []
    
            for j in range(m2.columnas):
                suma = 0

                for k in range(m1.columnas):
                    suma += m1[i][k] * m2[k][j]
                temp.append(suma)

            multipicar.append(temp)
        
        return Matriz(multipicar)
    
    # 矩阵逆转
    def inversa(self, matriz):
        n = matriz.filas
        
        if n != matriz.columnas:
            print("Error! Debe ser matriz cuadrada")
            return None

        aug = []
        for i in range(n):
            fila = []
            for j in range(n):
                fila.append(matriz[i][j])
            
            for j in range(n):
                fila.append(1 if i == j else 0)
            
            aug.append(fila)

        for i in range(n):
            
            if aug[i][i] == 0:
                for k in range(i+1, n):
                    if aug[k][i] != 0:
                        aug[i], aug[k] = aug[k], aug[i]
                        break
                else:
                    print("No tiene inversa")
                    return None
            
            pivote = aug[i][i]
            for j in range(2*n):
                aug[i][j] /= pivote

            for k in range(n):
                if k != i:
                    factor = aug[k][i]
                    for j in range(2*n):
                        aug[k][j] -= factor * aug[i][j]

        inversa = []
        for i in range(n):
            inversa.append(aug[i][n:])

        return Matriz(inversa)

    # 矩阵转置
    def transpuesta(self, matriz):
        temp = []
        for i in range(matriz.filas):
            for j in range(matriz.columnas):
                temp.append(matriz[j][i])

        transpuesta = []
        cont = 0
        for i in range(matriz.columnas):
            fila = []
            for j in range(matriz.filas):
                fila.append(temp[cont])
                cont += 1
            transpuesta.append(fila)

        return Matriz(transpuesta)