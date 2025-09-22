"""
Se trata de incluir las opciones necesarias para los
CRUD de productos y clientes.
"""

import json
from productos import Productos

def crud_productos(listado, mis_productos):
    while True:
        print("GESTIÓN DE PRODUCTOS")
        print("1. Agregar")
        print("2. Buscar")
        print("3. Modificar")
        print("4. Borrar")
        print("5. Listar\n")
        print("0. Salir")
        opcion = input("Digite su opción: ")
        if opcion=="1":
            cod = input("Código: ")
            nom = input("Nombre: ")
            pre = float(input("Precio: "))
            sal = int(input("Saldo: "))
            nuevo_producto = {"codigo": cod,
                            "nombre": nom,
                            "precio": pre,
                            "saldo": sal}
            resultado = mis_productos.agregar(nuevo_producto)
            if resultado==0:
                print("Producto agregado satisfactoriamente!")
            else:
                print("Código de producto ya existe!")
        elif opcion=="2":
            cod = input("Digite código a buscar: ")
            resultado = mis_productos.buscar(cod)
            if resultado==-1:
                print("Producto no existe!")
            else:
                print(listado[resultado])
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
