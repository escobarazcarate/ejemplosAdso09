import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
from productos import Productos

class AplicacionProductos:
    def __init__(self, ventana, listado):
        # Se crea la interface o ventana principal
        self.ventana = ventana
        self.ventana.title("Gestión de Productos")
        self.ventana.geometry("700x500")
        # Se simula la base de datos
        self.productos_db = Productos(listado)
        # Se crean los frame's contenedores
        self.frame_entrada = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame_entrada.pack()
        self.frame_botones = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame_botones.pack()
        self.frame_salida = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame_salida.pack()

        self.crear_entrada()
        self.crear_botones()
        self.crear_salida()

    def crear_entrada(self):
        tk.Label(self.frame_entrada, text="Código:", width=10).grid(row=0, column=0, pady=5, sticky="w")
        self.entrada_codigo = tk.Entry(self.frame_entrada, width=30)
        self.entrada_codigo.grid(row=0, column=1, pady=5)
        tk.Label(self.frame_entrada, text="Nombre:", width=10).grid(row=1, column=0, pady=5, sticky="w")
        self.entrada_nombre = tk.Entry(self.frame_entrada, width=30)
        self.entrada_nombre.grid(row=1, column=1, pady=5)
        tk.Label(self.frame_entrada, text="Precio:", width=10).grid(row=2, column=0, pady=5, sticky="w")
        self.entrada_precio = tk.Entry(self.frame_entrada, width=30)
        self.entrada_precio.grid(row=2, column=1, pady=5)
        tk.Label(self.frame_entrada, text="Saldo:", width=10).grid(row=3, column=0, pady=5, sticky="w")
        self.entrada_saldo = tk.Entry(self.frame_entrada, width=30)
        self.entrada_saldo.grid(row=3, column=1, pady=5)

    def crear_botones(self):
        estilo = ttk.Style()
        estilo.configure('TButton', font=('Helvetica', 10), padding=5)
        ttk.Button(self.frame_botones, text="Agregar", command=self.agregar_producto).grid(row=0, column=0, padx=5)
        ttk.Button(self.frame_botones, text="Buscar", command=self.buscar_producto).grid(row=0, column=1, padx=5)
        ttk.Button(self.frame_botones, text="Modificar", command=self.modificar_producto).grid(row=0, column=2, padx=5)
        ttk.Button(self.frame_botones, text="Borrar", command=self.borrar_producto).grid(row=0, column=3, padx=5)
        ttk.Button(self.frame_botones, text="Listar", command=self.listar_productos).grid(row=0, column=4, padx=5)
        ttk.Button(self.frame_botones, text="Limpiar", command=self.limpiar_campos).grid(row=0, column=5, padx=5)

    def crear_salida(self):
        self.salida_texto = tk.Text(self.frame_salida, wrap="word", state="disabled")
        self.salida_texto.pack(expand=True, fill="both")

    def _mostrar_mensaje(self, mensaje):
        self.salida_texto.config(state="normal")
        self.salida_texto.delete("1.0", tk.END)
        self.salida_texto.insert(tk.END, mensaje)
        self.salida_texto.config(state="disabled")

    def limpiar_campos(self):
        self.entrada_codigo.delete(0, tk.END)
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_precio.delete(0, tk.END)
        self.entrada_saldo.delete(0, tk.END)

    def obtener_datos(self):
        try:
            codigo = self.entrada_codigo.get()
            nombre = self.entrada_nombre.get()
            precio = float(self.entrada_precio.get())
            saldo = int(self.entrada_saldo.get())
            return {"codigo": codigo, "nombre": nombre, "precio": precio, "saldo": saldo}
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número y el saldo un entero.")
            return None

    def agregar_producto(self):
        producto = self.obtener_datos()
        if producto:
            resultado = self.productos_db.agregar(producto)
            if resultado == 0:
                self._mostrar_mensaje(f"Producto '{producto['nombre']}' agregado exitosamente.")
            else:
                self._mostrar_mensaje(f"Error: El producto con el código '{producto['codigo']}' ya existe.")

    def buscar_producto(self):
        codigo = self.entrada_codigo.get()
        posicion = self.productos_db.buscar(codigo)
        if posicion != -1:
            prod_encontrado = self.productos_db.listado[posicion]
            self.limpiar_campos()
            self.entrada_codigo.insert(0, prod_encontrado['codigo'])
            self.entrada_nombre.insert(0, prod_encontrado['nombre'])
            self.entrada_precio.insert(0, prod_encontrado['precio'])
            self.entrada_saldo.insert(0, prod_encontrado['saldo'])
            self._mostrar_mensaje(f"Producto '{prod_encontrado['nombre']}' encontrado y cargado en los campos.")
        else:
            messagebox.showinfo("Búsqueda", f"No se encontró un producto con el código '{codigo}'.")
            self._mostrar_mensaje(f"No se encontró un producto con el código '{codigo}'.")

    def modificar_producto(self):
        producto = self.obtener_datos()
        if producto:
            posicion = self.productos_db.buscar(producto['codigo'])
            if posicion != -1:
                self.productos_db.modificar(producto)
                self._mostrar_mensaje(f"Producto '{producto['nombre']}' modificado exitosamente.")
            else:
                messagebox.showerror("Error", "El producto a modificar no existe.")

    def borrar_producto(self):
        codigo = self.entrada_codigo.get()
        posicion = self.productos_db.buscar(codigo)
        if posicion != -1:
            self.productos_db.borrar(codigo)
            self._mostrar_mensaje(f"Producto con código '{codigo}' borrado exitosamente.")
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "El producto a borrar no existe.")

    def listar_productos(self):
        lista_str = "--- LISTADO DE PRODUCTOS ---\n"
        if not self.productos_db.listado:
            lista_str += "No hay productos registrados."
        else:
            for prod in self.productos_db.listado:
                lista_str += f"\nCódigo: {prod['codigo']}, Nombre: {prod['nombre']}, Precio: {prod['precio']}, Saldo: {prod['saldo']}"
        self._mostrar_mensaje(lista_str)

if __name__ == "__main__":
    try:
        with open("productos.json", "r", encoding="utf-8") as archivop:
            listadop = json.load(archivop)
    except FileNotFoundError:
        listadop = []
    gui_productos = tk.Tk()
    app = AplicacionProductos(gui_productos, listadop)
    gui_productos.mainloop()
    with open("productos.json", "w", encoding="utf-8") as archivop:
        json.dump(listadop, archivop, indent=4, ensure_ascii=False)
