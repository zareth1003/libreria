import sqlite3

def conectar_bd(Ventas):

  try:
    conexion = sqlite3.connect(Ventas)
    cursor=conexion.cursor()
    return conexion, cursor

  except sqlite3.OperationalError as error:
    print('Error al abrir la base de datos: ', error)
    return None, None

def desconectar_bd(conexion, cursor):
  if conexion:
    cursor.close()
    conexion.close()
    print('Conexion Cerrada')