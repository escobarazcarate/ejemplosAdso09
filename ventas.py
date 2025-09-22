class Ventas:
    def __init__(self, listado):
        self.listado = listado
    def buscar(self, num):
        posicion = -1
        for i in range(len(self.listado)):
            if self.listado[i]["numero"]==num:
                posicion = i
                break
        return posicion
    def agregar(self,venta):
        pos = self.buscar(venta["numero"])
        if pos==-1:
            self.listado.append(venta)
            return 0
        else:
            return 1
    def listar(self):
        print("LISTADO DE VENTAS")
        for i in range(len(self.listado)):
            print(self.listado[i])