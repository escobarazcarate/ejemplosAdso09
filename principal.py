"""
Se trata de incluir las opciones necesarias para los
CRUD de productos y clientes.
"""

import json
from productos import Productos

try:
    with open("productos.json", "r", encoding="utf-8") as archivo:
        listado = json.load(archivo)
except FileNotFoundError:
    listado = []

mis_productos = Productos(listado)

while True:
    print("1. Agregar")
    print("2. Buscar\n")
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
    elif opcion=="0":
        break

with open("productos.json", "w", encoding="utf-8") as archivo:
    json.dump(listado, archivo, indent=4, ensure_ascii=False)
