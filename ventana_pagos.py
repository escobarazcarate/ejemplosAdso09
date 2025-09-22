import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
from pagos import Pagos

class AplicacionPagos:
    def __init__(self, ventana, listado):
        self.ventana = ventana
        self.ventana.title("Gestión de Pagos")
        self.ventana.geometry("700x500")

        self.pagos_db = Pagos(listado)

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
        tk.Label(self.frame_entrada, text="ID Pago:", width=12).grid(row=0, column=0, pady=5, sticky="w")
        self.entrada_id = tk.Entry(self.frame_entrada, width=30)
        self.entrada_id.grid(row=0, column=1, pady=5)

        tk.Label(self.frame_entrada, text="Cédula Cliente:", width=12).grid(row=1, column=0, pady=5, sticky="w")
        self.entrada_cedula = tk.Entry(self.frame_entrada, width=30)
        self.entrada_cedula.grid(row=1, column=1, pady=5)

        tk.Label(self.frame_entrada, text="Monto:", width=12).grid(row=2, column=0, pady=5, sticky="w")
        self.entrada_monto = tk.Entry(self.frame_entrada, width=30)
        self.entrada_monto.grid(row=2, column=1, pady=5)

        tk.Label(self.frame_entrada, text="Fecha:", width=12).grid(row=3, column=0, pady=5, sticky="w")
        self.entrada_fecha = tk.Entry(self.frame_entrada, width=30)
        self.entrada_fecha.grid(row=3, column=1, pady=5)

    def crear_botones(self):
        estilo = ttk.Style()
        estilo.configure('TButton', font=('Helvetica', 10), padding=5)
        ttk.Button(self.frame_botones, text="Agregar", command=self.agregar_pago).grid(row=0, column=0, padx=5)
        ttk.Button(self.frame_botones, text="Buscar", command=self.buscar_pago).grid(row=0, column=1, padx=5)
        ttk.Button(self.frame_botones, text="Modificar", command=self.modificar_pago).grid(row=0, column=2, padx=5)
        ttk.Button(self.frame_botones, text="Borrar", command=self.borrar_pago).grid(row=0, column=3, padx=5)
        ttk.Button(self.frame_botones, text="Listar", command=self.listar_pagos).grid(row=0, column=4, padx=5)
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
        self.entrada_id.delete(0, tk.END)
        self.entrada_cedula.delete(0, tk.END)
        self.entrada_monto.delete(0, tk.END)
        self.entrada_fecha.delete(0, tk.END)

    def obtener_datos(self):
        try:
            id_pago = self.entrada_id.get()
            cedula = self.entrada_cedula.get()
            monto = float(self.entrada_monto.get())
            fecha = self.entrada_fecha.get()
            if not id_pago or not cedula:
                messagebox.showerror("Error", "El ID del pago y la cédula son obligatorios.")
                return None
            return {"id_pago": id_pago, "cedula": cedula, "monto": monto, "fecha": fecha}
        except ValueError:
            messagebox.showerror("Error", "El monto debe ser un número.")
            return None

    def agregar_pago(self):
        pago = self.obtener_datos()
        if pago:
            resultado = self.pagos_db.agregar(pago)
            if resultado == 0:
                self._mostrar_mensaje(f"Pago {pago['id_pago']} registrado exitosamente.")
            else:
                self._mostrar_mensaje(f"Error: Ya existe un pago con ID '{pago['id_pago']}'.")

    def buscar_pago(self):
        id_pago = self.entrada_id.get()
        pos = self.pagos_db.buscar(id_pago)
        if pos != -1:
            pag = self.pagos_db.listado[pos]
            self.limpiar_campos()
            self.entrada_id.insert(0, pag['id_pago'])
            self.entrada_cedula.insert(0, pag['cedula'])
            self.entrada_monto.insert(0, pag['monto'])
            self.entrada_fecha.insert(0, pag['fecha'])
            self._mostrar_mensaje(f"Pago {id_pago} encontrado y cargado en los campos.")
        else:
            messagebox.showinfo("Búsqueda", f"No se encontró pago con ID '{id_pago}'.")
            self._mostrar_mensaje(f"No se encontró pago con ID '{id_pago}'.")

    def modificar_pago(self):
        pago = self.obtener_datos()
        if pago:
            if self.pagos_db.modificar(pago):
                self._mostrar_mensaje(f"Pago {pago['id_pago']} modificado exitosamente.")
            else:
                messagebox.showerror("Error", "El pago a modificar no existe.")

    def borrar_pago(self):
        id_pago = self.entrada_id.get()
        if self.pagos_db.borrar(id_pago):
            self._mostrar_mensaje(f"Pago {id_pago} borrado exitosamente.")
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "El pago a borrar no existe.")

    def listar_pagos(self):
        lista_str = "--- LISTADO DE PAGOS ---\n"
        if not self.pagos_db.listado:
            lista_str += "No hay pagos registrados."
        else:
            for pag in self.pagos_db.listado:
                lista_str += f"\nID: {pag['id_pago']}, Cédula Cliente: {pag['cedula']}, Monto: {pag['monto']}, Fecha: {pag['fecha']}"
        self._mostrar_mensaje(lista_str)

if __name__ == "__main__":
    try:
        with open("pagos.json", "r", encoding="utf-8") as archivop:
            listadopg = json.load(archivop)
    except FileNotFoundError:
        listadopg = []

    gui_pagos = tk.Tk()
    app = AplicacionPagos(gui_pagos, listadopg)
    gui_pagos.mainloop()

    with open("pagos.json", "w", encoding="utf-8") as archivop:
        json.dump(listadopg, archivop, indent=4, ensure_ascii=False)  