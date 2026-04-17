

class Matriz:
    def __init__(self, valores):

        # 计算矩阵(Matriz)所有的列数是否一样
        columnas = None
        for filas in valores:
            if columnas == None:

                columnas = len(filas)
            elif columnas != len(filas):
                raise ValueError("La matriz debe tener las mismas columnass en cada fila!")
            
        
        if columnas == 0:
            raise ValueError("Las filas deben tener al menos una columnas.")
        
        self.columnas = columnas
        self.filas = len(valores)
        self.valores = valores
        
    # 获取idx位置的数据
    def __getitem__(self, idx):
        if idx < 0 or idx >= self.filas:
            raise IndexError(f"Indice para fila fuera de rango: ({idx})")
        
        return self.valores[idx]
    

    def __str__(self):
        imprimir = ""
        for i in range(len(self.valores)):
            imprimir += str(self.valores[i])
            imprimir += "\n"
        return imprimir


        