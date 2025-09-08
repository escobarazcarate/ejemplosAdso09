import json
from ventas import Ventas

def crud_ventas(listadop,mis_productos,listadoc,mis_clientes,listadov, mis_ventas):
    while True:
        print("GESTIÓN DE VENTAS")
        print("1. Agregar")
        print("2. Buscar")
        print("3. Listar\n")
        print("0. Salir")
        opcion = input("Digite su opción: ")
        if opcion=="1":
            num = input("Número de factura: ")
            resultadov = mis_ventas.buscar(num)
            if resultadov>-1:
                print("Factura ya existe!")
            else:
                id = input("Identificación: ")
                resultadoc = mis_clientes.buscar(id)
                if resultadoc==-1:
                    print("Cliente no existe!")
                else:
                    print(listadoc[resultadoc]["nombre"])
                    cod = ["","",""]
                    can = [0,0,0]
                    for i in range(3):
                        resultadop = -1
                        while True:
                            cod[i] = input(f"Código de producto {i+1}: ")
                            if cod[i]=="-1":
                                break
                            resultadop = mis_productos.buscar(cod[i])
                            if resultadop>-1:
                                break
                            else:
                                print("Código de producto no existe")
                        if cod[i]=="-1":
                            break
                        print(listadop[resultadop]["nombre"])
                        can[i] = int(input("Cantidad: "))
                        producto = {"codigo":cod[i],
                                    "nombre":listadop[resultadop]["nombre"],
                                    "precio":listadop[resultadop]["precio"],
                                    "stock":listadop[resultadop]["stock"]-can[i]}
                        mis_productos.modificar(producto)
            nueva_venta = {"numero":num,"id":id,
                           "codigo1":cod[0],"cantidad1":can[0],
                           "codigo2":cod[1],"cantidad2":can[1],
                           "codigo3":cod[2],"cantidad3":can[2],}
            mis_ventas.agregar(nueva_venta)
        elif opcion=="2":
            cod = input("Digite código a buscar: ")
            resultado = mis_productos.buscar(cod)
            if resultado==-1:
                print("Producto no existe!")
            else:
                print(listadop[resultado])
        elif opcion=="3":
            cod = input("Digite código a modificar")
            resultado = mis_productos.buscar(cod)
            if resultado>-1:
                nom = input("Nuevo nombre: ")
                pre = float(input("Nuevo precio: "))
                sal = int(input("Nuevo saldo: "))
                nuevo_producto = {"codigo": cod,
                                "nombre": nom,
                                "precio": pre,
                                "saldo": sal}
                mis_productos.modificar(nuevo_producto)
            else:
                print("Producto no existe!")
        elif opcion=="4":
            cod = input("Digite código a borrar")
            resultado = mis_productos.buscar(cod)
            if resultado>-1:
                mis_productos.borrar(cod)
            else:
                print("Producto no existe!")
        elif opcion=="5":
            mis_productos.listar()
        elif opcion=="0":
            break
        else:
            print("Opción inválida")

