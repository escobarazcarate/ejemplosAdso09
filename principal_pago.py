class Pagos:
    def __init__(self, listado):
        self.listado = listado

    def agregar(self, pago):
        if self.buscar(pago["id_pago"]) == -1:
            self.listado.append(pago)
            return 0
        return -1

    def buscar(self, id_pago):
        for i, pag in enumerate(self.listado):
            if pag["id_pago"] == id_pago:
                return i
        return -1

    def modificar(self, pago):
        pos = self.buscar(pago["id_pago"])
        if pos != -1:
            self.listado[pos] = pago
            return True
        return False

    def borrar(self, id_pago):
        pos = self.buscar(id_pago)
        if pos != -1:
            del self.listado[pos]
            return True
        return False