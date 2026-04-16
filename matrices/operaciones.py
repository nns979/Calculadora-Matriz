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

    
