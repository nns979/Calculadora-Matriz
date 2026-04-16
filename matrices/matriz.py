
class Matriz:
    def __init__(self, values):

        # 计算矩阵(Matriz)所有的列数是否一样
        cols = None
        for row in values:
            if cols == None:

                cols = len(row)
            elif cols != len(row):
                raise ValueError("La matriz debe tener las mismas columnas en cada fila!")
            
        
        if cols == 0:
            raise ValueError("Las filas deben tener al menos una columna.")
        
        self.cols = cols
        self.rows = len(values)
        self.values = values
        
    # 获取idx位置的数据
    def __getitem__(self, idx):
        if idx < 0 or idx >= self.rows:
            raise IndexError(f"Indice para fila fuera de rango: ({idx})")
        
        return self.values[idx]
    
    def __str__(self):
        imprimir = ""
        for i in range(self.matriz.values):
            imprimir += str(self.matriz.values[i])
            imprimir += "\n"
        
        return imprimir

        