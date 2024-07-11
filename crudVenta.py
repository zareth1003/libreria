from sqlLibreria import conectar_bd, desconectar_bd
from prettytable import PrettyTable
from tkinter import messagebox
import sqlite3

conexion, cursor = conectar_bd('Ventas.db')


def agregarVenta(isbn, cliente, cantidad):
  conexion, cursor = conectar_bd('Ventas.db')
  
  cursor.execute("CREATE TABLE IF NOT EXISTS ventas (IdVentas TEXT PRIMARY KEY, codigoCliente TEXT, codigoLibro NUMERIC, cantidad NUMERIC, precio NUMERIC)")
  cursor.execute('SELECT * FROM libros WHERE ISBN = ?', [isbn])
  libro = cursor.fetchone()
  precio= libro[2]*cantidad
  codMaxVenta = 1020 + (cursor.execute('SELECT COUNT(*) FROM ventas').fetchone()[0] * 5)
  codMaxVentaFinal = 'V-' + str(codMaxVenta)
  parametros = [codMaxVentaFinal, cliente, isbn, cantidad, precio]
  sentencia ="""INSERT INTO ventas VALUES (?,?,?,?,?)"""
  cursor.execute(sentencia, parametros)
  conexion.commit()
  desconectar_bd(conexion, cursor)
  messagebox.showinfo("information","Venta agregada correctamente") 