class pago:
    def __init__(self,pago):
        self.pago = pago
         
    def bucar(self,id):
        for i in range(len(self.pago)):
            posicion = -1
            if self.pago[i]["identificacion"]==id:
                posicion = i
                break
        return posicion
    
    def agregar(self,prod):
        pos = self.buscar(prod["identificacion"])
        if pos==-1:
            self.listado.append(prod)
        return 1  

    
    def msotrar_pago(self):
        for pagos in self.pagos:
            print(pagos)
        
    
        
      