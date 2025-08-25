from principal_productos import *
from principal_clientes import *
from principal_ventas import *

try:
    with open("productos.json", "r", encoding="utf-8") as archivop:
        listadop = json.load(archivop)
except FileNotFoundError:
    listadop = []
mis_productos = Productos(listadop)

try:
    with open("clientes.json", "r", encoding="utf-8") as archivoc:
        listadoc = json.load(archivoc)
except FileNotFoundError:
    listadoc = []
mis_clientes = Clientes(listadoc)

try:
    with open("ventas.json", "r", encoding="utf-8") as archivov:
        listadov = json.load(archivov)
except FileNotFoundError:
    listadov = []
mis_Ventas = Ventas(listadov)

while True:
    print("1. Gestión de productos")
    print("2. Gestión de clientes")
    print("3. Gestión de ventas")
    print("\n0. Salir")
    opcion = input("Qué opción desea: ")
    if opcion=="1":
        crud_productos(listadop, mis_productos)
    elif opcion=="2":
        crud_clientes(listadoc, mis_clientes)
    elif opcion=="3":
        crud_ventas(listadop,mis_productos,listadoc,mis_clientes,listadov,mis_Ventas)
    elif opcion=="0":
        break

with open("productos.json", "w", encoding="utf-8") as archivop:
    json.dump(listadop, archivop, indent=4, ensure_ascii=False)

with open("clientes.json", "w", encoding="utf-8") as archivoc:
    json.dump(listadoc, archivoc, indent=4, ensure_ascii=False)

with open("ventas.json", "w", encoding="utf-8") as archivov:
    json.dump(listadov, archivov, indent=4, ensure_ascii=False)
