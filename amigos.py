import json

with open("amigos.json", "r", encoding="utf-8") as archivo:
    amigos = json.load(archivo)

def buscar(nom):
    posicion = -1
    for i in range(len(amigos)):
        if a[i]["nombre"]==nom:
            posicion = i
            break
    if posicion==-1:
        print(f"No se encontró a {nom} en la lista")
    return posicion

while True:
    print("1. Agregar")
    print("2. Buscar")
    print("3. Modificar")
    print("4. Borrar")
    print("5. Listar\n")
    print("0. Salir")
    opcion = input("Que opción desea? ")
    if opcion=="1":
        nom = input("Digite el nombre: ")
        tel = input("Digitel el teléfono: ")
        amigos.append({"nombre": nom, "telefono": tel})
    elif opcion=="2":
        nom = input("Digite nombre del contacto a buscar: ")
        pos = buscar(nom)
        if(pos>=0):
            print(f"El telefono de {nom} es {amigos[pos]['telefono']}")
    elif opcion=="3":
        nom = input("Digite nombre del contacto a modificar: ")
        pos = buscar(nom)
        if(pos>=0):
            a[pos]["nombre"]=input("Digite el nombre: ")
            a[pos]["telefono"]=input("Digite el teléfono: ")
    elif opcion=="4":
        nom = input("Digite nombre del contacto a borrar: ")
        encontrado = False
        for a in amigos:
            if a["nombre"]==nom:
                encontrado = True
                amigos.remove(a)
                break
        if not encontrado:
            print(f"No se encontró a {nom} en la lista")
    elif opcion=="5":
        print("NOMBRE      TELEFONO")
        for a in amigos:
            print(a['nombre'],a['telefono'])
    elif opcion=="0":
        with open("amigos.json", "w", encoding="utf-8") as archivo:
            json.dump(amigos, archivo, indent=4, ensure_ascii=False)
        break
