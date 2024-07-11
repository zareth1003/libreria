from sqlLibreria import conectar_bd, desconectar_bd
from prettytable import PrettyTable
from tkinter import messagebox
import sqlite3

conexion, cursor = conectar_bd('Ventas.db')

def agregarCliente(Id, nombre):
  conexion, cursor = conectar_bd('Ventas.db')
  cursor.execute("CREATE TABLE IF NOT EXISTS clientes (IdCliente INTEGER PRIMARY KEY, nombre TEXT)")
  parametros = [(int(Id)), nombre]
  sentencia ="""INSERT INTO clientes VALUES (?,?)"""
  cursor.execute(sentencia, parametros)
  conexion.commit()
  desconectar_bd(conexion, cursor)
  messagebox.showinfo("information","Cliente agregado correctamente")  
  
def validarIDClientes(valor):
    conexion, cursor = conectar_bd('Ventas.db')
    cursor.execute("SELECT * FROM clientes WHERE IdCliente = ?", (valor,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado
  
def obtener_Clientes():
  conexion, cursor = conectar_bd('Ventas.db')
  cursor.execute("SELECT * FROM clientes")
  clientes = cursor.fetchall()
  conexion.close()
  return clientes
   
   
def validadIDClientesVentas(valor):
    conexion, cursor = conectar_bd('Ventas.db')
    cursor.execute("SELECT * FROM ventas WHERE codigoCliente = ?", (valor,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado
   
def eliminar_Cliente(id):
    conexion, cursor = conectar_bd('Ventas.db')
    id = int(id)
    cursor.execute("DELETE FROM clientes WHERE IdCliente =?", (id,))
    conexion.commit()
    conexion.close()
    
   
  


#conexion.commit()
#desconectar_bd(conexion, cursor)