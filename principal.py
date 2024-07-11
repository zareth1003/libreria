from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from interfaz import agregarClienteInterfaz, agregarLibrosInterfaz, agregarVentaInterfaz, eliminarClienteInterfaz, eliminarLibroInterfaz
import sqlite3

root = Tk()
root.title('Libreria ZAC')
root.geometry('800x400')

barraMenu= Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_command(label="Salir")

clientesMenu= Menu(barraMenu, tearoff=0)
clientesMenu.add_command(label="Crear", command=agregarClienteInterfaz)
clientesMenu.add_command(label="Leer", command=eliminarClienteInterfaz)
clientesMenu.add_command(label="Actualizar")
clientesMenu.add_command(label="Eliminar", command=eliminarClienteInterfaz)

librosMenu= Menu(barraMenu, tearoff=0)
librosMenu.add_command(label="Crear", command=agregarLibrosInterfaz)
librosMenu.add_command(label="Leer")
librosMenu.add_command(label="Actualizar")
librosMenu.add_command(label="Eliminar", command=eliminarLibroInterfaz)

ventasMenu= Menu(barraMenu, tearoff=0)
ventasMenu.add_command(label="Crear", command=agregarVentaInterfaz)
ventasMenu.add_command(label="Leer")
ventasMenu.add_command(label="Actualizar")
ventasMenu.add_command(label="Eliminar")

estadisticaMenu= Menu(barraMenu, tearoff=0)
estadisticaMenu.add_command(label="Consultar Libro")
estadisticaMenu.add_command(label="Más y Menos Vendido")
estadisticaMenu.add_command(label="Cliente mayor Venta")


barraMenu.add_cascade(label="BBDD", menu= bbddMenu)
barraMenu.add_cascade(label="Clientes", menu= clientesMenu)
barraMenu.add_cascade(label="Libros", menu=librosMenu)
barraMenu.add_cascade(label="Ventas", menu=ventasMenu)
barraMenu.add_cascade(label="Estadistico", menu=estadisticaMenu)








root.mainloop()