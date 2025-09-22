import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
from clientes import Clientes

class AplicacionClientes:
    def __init__(self, ventana, listado):
        self.ventana = ventana
        self.ventana.title("Gestión de Clientes")
        self.ventana.geometry("700x500")

        self.clientes_db = Clientes(listado)

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
        tk.Label(self.frame_entrada, text="Cédula:", width=10).grid(row=0, column=0, pady=5, sticky="w")
        self.entrada_cedula = tk.Entry(self.frame_entrada, width=30)
        self.entrada_cedula.grid(row=0, column=1, pady=5)

        tk.Label(self.frame_entrada, text="Nombre:", width=10).grid(row=1, column=0, pady=5, sticky="w")
        self.entrada_nombre = tk.Entry(self.frame_entrada, width=30)
        self.entrada_nombre.grid(row=1, column=1, pady=5)

        tk.Label(self.frame_entrada, text="Teléfono:", width=10).grid(row=2, column=0, pady=5, sticky="w")
        self.entrada_telefono = tk.Entry(self.frame_entrada, width=30)
        self.entrada_telefono.grid(row=2, column=1, pady=5)

        tk.Label(self.frame_entrada, text="Correo:", width=10).grid(row=3, column=0, pady=5, sticky="w")
        self.entrada_correo = tk.Entry(self.frame_entrada, width=30)
        self.entrada_correo.grid(row=3, column=1, pady=5)

    def crear_botones(self):
        estilo = ttk.Style()
        estilo.configure('TButton', font=('Helvetica', 10), padding=5)
        ttk.Button(self.frame_botones, text="Agregar", command=self.agregar_cliente).grid(row=0, column=0, padx=5)
        ttk.Button(self.frame_botones, text="Buscar", command=self.buscar_cliente).grid(row=0, column=1, padx=5)
        ttk.Button(self.frame_botones, text="Modificar", command=self.modificar_cliente).grid(row=0, column=2, padx=5)
        ttk.Button(self.frame_botones, text="Borrar", command=self.borrar_cliente).grid(row=0, column=3, padx=5)
        ttk.Button(self.frame_botones, text="Listar", command=self.listar_clientes).grid(row=0, column=4, padx=5)
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
        self.entrada_cedula.delete(0, tk.END)
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_telefono.delete(0, tk.END)
        self.entrada_correo.delete(0, tk.END)

    def obtener_datos(self):
        cedula = self.entrada_cedula.get()
        nombre = self.entrada_nombre.get()
        telefono = self.entrada_telefono.get()
        correo = self.entrada_correo.get()
        if not cedula or not nombre:
            messagebox.showerror("Error", "La cédula y el nombre son obligatorios.")
            return None
        return {"cedula": cedula, "nombre": nombre, "telefono": telefono, "correo": correo}

    def agregar_cliente(self):
        cliente = self.obtener_datos()
        if cliente:
            resultado = self.clientes_db.agregar(cliente)
            if resultado == 0:
                self._mostrar_mensaje(f"Cliente '{cliente['nombre']}' agregado exitosamente.")
            else:
                self._mostrar_mensaje(f"Error: Ya existe un cliente con la cédula '{cliente['cedula']}'.")

    def buscar_cliente(self):
        cedula = self.entrada_cedula.get()
        posicion = self.clientes_db.buscar(cedula)
        if posicion != -1:
            cli = self.clientes_db.listado[posicion]
            self.limpiar_campos()
            self.entrada_cedula.insert(0, cli['cedula'])
            self.entrada_nombre.insert(0, cli['nombre'])
            self.entrada_telefono.insert(0, cli['telefono'])
            self.entrada_correo.insert(0, cli['correo'])
            self._mostrar_mensaje(f"Cliente '{cli['nombre']}' encontrado y cargado en los campos.")
        else:
            messagebox.showinfo("Búsqueda", f"No se encontró cliente con cédula '{cedula}'.")
            self._mostrar_mensaje(f"No se encontró cliente con cédula '{cedula}'.")

    def modificar_cliente(self):
        cliente = self.obtener_datos()
        if cliente:
            if self.clientes_db.modificar(cliente):
                self._mostrar_mensaje(f"Cliente '{cliente['nombre']}' modificado exitosamente.")
            else:
                messagebox.showerror("Error", "El cliente a modificar no existe.")

    def borrar_cliente(self):
        cedula = self.entrada_cedula.get()
        if self.clientes_db.borrar(cedula):
            self._mostrar_mensaje(f"Cliente con cédula '{cedula}' borrado exitosamente.")
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "El cliente a borrar no existe.")

    def listar_clientes(self):
        lista_str = "--- LISTADO DE CLIENTES ---\n"
        if not self.clientes_db.listado:
            lista_str += "No hay clientes registrados."
        else:
            for cli in self.clientes_db.listado:
                lista_str += f"\nCédula: {cli['cedula']}, Nombre: {cli['nombre']}, Teléfono: {cli['telefono']}, Correo: {cli['correo']}"
        self._mostrar_mensaje(lista_str)

if __name__ == "__main__":
    try:
        with open("clientes.json", "r", encoding="utf-8") as archivoc:
            listadoc = json.load(archivoc)
    except FileNotFoundError:
        listadoc = []

    gui_clientes = tk.Tk()
    app = AplicacionClientes(gui_clientes, listadoc)
    gui_clientes.mainloop()

    with open("clientes.json", "w", encoding="utf-8") as archivoc:
        json.dump(listadoc, archivoc, indent=4, ensure_ascii=False)