class Clientes:
    def __init__(self, listado):
        self.listado = listado
    def buscar(self, id):
        posicion = -1
        for i in range(len(self.listado)):
            if self.listado[i]["id"]==id:
                posicion = i
                break
        return posicion
    def agregar(self,cli):
        pos = self.buscar(cli["id"])
        if pos==-1:
            self.listado.append(cli)
            return 0
        else:
            return 1
    def modificar(self,cli):
        pos = self.buscar(cli["id"])
        self.listado[pos]=cli
    def borrar(self,id):
        pos = self.buscar(id)
        self.listado.pop(pos)
    def listar(self):
        print("LISTADO DE CLIENTES")
        for i in range(len(self.listado)):
            print(self.listado[i])
