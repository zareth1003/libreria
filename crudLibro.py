from sqlLibreria import conectar_bd, desconectar_bd
from prettytable import PrettyTable
from tkinter import messagebox
import sqlite3

conexion, cursor = conectar_bd('Ventas.db')


def agregarLibro(isbn, nombre, precio, inventario):
  conexion, cursor = conectar_bd('Ventas.db')
  
  cursor.execute("CREATE TABLE IF NOT EXISTS libros (ISBN INTEGER PRIMARY KEY, nombre TEXT, precio NUMERIC, inventario NUMERIC)")
  parametros = [(int(isbn)), nombre, precio, inventario]
  sentencia ="""INSERT INTO libros VALUES (?,?,?,?)"""
  cursor.execute(sentencia, parametros)
  conexion.commit()
  desconectar_bd(conexion, cursor)
  messagebox.showinfo("information","Libro agregado correctamente")  
  
def validarLibro(valor):
  conexion, cursor = conectar_bd('Ventas.db')
  cursor.execute("SELECT * FROM libros WHERE ISBN = ?", (valor,))
  resultado = cursor.fetchone()
  conexion.close()
  return resultado

def cantidadLibros(id_libro):
    conexion, cursor = conectar_bd('Ventas.db')
    cantLibros = "SELECT inventario FROM libros WHERE ISBN = ?"
    parametroLibro = [id_libro]
    cursor.execute(cantLibros, parametroLibro)
    inventarios = cursor.fetchone()
    for inventario in inventarios:
        inventarioLibros = inventario
    conexion.close()
    return inventarioLibros
  
def validarLibrosVentas(valor):
    conexion, cursor = conectar_bd('Ventas.db')
    cursor.execute("SELECT * FROM ventas WHERE codigoLibro = ?", (valor,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado
   
def eliminar_libro(isbn):
    conexion, cursor = conectar_bd('Ventas.db')
    cursor.execute("DELETE FROM libros WHERE ISBN = ?", (isbn,))
    conexion.commit()
    conexion.close()
    print("Libro eliminado con exito.")