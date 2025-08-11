"""
Se trata de escribir un programa con un CRUD para productos
Cada producto debe tener los siguientes datos:
Codigo (string), Nombre (string), precio (float), saldo (int)
"""
class Productos:
    def __init__(self, listado):
        self.listado = listado
    def buscar(self, cod):
        posicion = -1
        for i in range(len(self.listado)):
            if self.listado[i]["codigo"]==cod:
                posicion = i
                break
        return posicion
    def agregar(self,prod):
        pos = self.buscar(prod["codigo"])
        if pos==-1:
            self.listado.append(prod)
            return 0
        else:
            return 1
