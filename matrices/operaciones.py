from matrices.matriz import Matriz

class Operaciones:

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

    def suma(self, m1, m2):
        suma_m = []

        if m1.filas != m2.filas or m1.columnas != m2.columnas:
            return print("Error, Las columnas y filas debe de ser igua para hacer suma!")
            
        for i in range(m1.filas):
            temp = []
            for j in range(m1.columnas):
                temp.append(m1.valores[i][j] + m2.valores[i][j])

            suma_m.append(temp)
            
        return suma_m

