from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sqlLibreria import conectar_bd, desconectar_bd
from crudCliente import agregarCliente, validarIDClientes, obtener_Clientes, validadIDClientesVentas, eliminar_Cliente
from crudLibro import agregarLibro, eliminar_libro, validarLibrosVentas

def agregarVentaInterfaz():
  mostrar_agregar_venta= Toplevel()
  mostrar_agregar_venta.title("Agregar venta")
  mostrar_agregar_venta.geometry("600x200")
  
  codigoCliente_label = Label(mostrar_agregar_venta, text="Codigo Cliente:")
  codigoCliente_label.pack()
  codigoCliente_entry= Entry(mostrar_agregar_venta)
  codigoCliente_entry.pack()
  
  codigoLibro_label = Label(mostrar_agregar_venta, text="Codigo Libro:")
  codigoLibro_label.pack()
  codigoLibro_entry= Entry(mostrar_agregar_venta)
  codigoLibro_entry.pack()
  
  codigoCantidad_label = Label(mostrar_agregar_venta, text="Cantidad:")
  codigoCantidad_label.pack()
  codigoCantidad_entry= Entry(mostrar_agregar_venta)
  codigoCantidad_entry.pack()
  
  def guardarVenta():
    libro = codigoLibro_entry.get()
    cliente = codigoCliente_entry.get()
    cantidad = codigoCantidad_entry.get()
    if libro != "" and cliente != "" and cantidad != "":
      if validarLibro(libro):
        if validarIDClientes(cliente):
          if int(cantidadLibros(libro)) < int(cantidad):
            messagebox.showinfo("Cantidad","No hay la cantidad suficiente de libros.")
          else:
            agregarVenta(libro, cliente, cantidad)
            messagebox.showinfo("Agregado","Venta agregada correctamente.")
            mostrar_agregar_venta.destroy()
        else:
          messagebox.showerror("Error", "El ID del cliente no existe.")
          mostrar_agregar_venta.destroy() 
      else:
        messagebox.showerror("Error","El Isbn del libro no existe.")
        mostrar_agregar_venta.destroy()
    else:
      messagebox.showerror("Error", "Todos los campos deben estar registrados.")
      mostrar_agregar_venta.destroy()
  guardar_button = Button(mostrar_agregar_venta, text="Guardar", command=guardarVenta)
  guardar_button.pack()
  
#Crear venta de crear Libro
def agregarLibrosInterfaz():
  mostrar_agregar_libro= Toplevel()
  mostrar_agregar_libro.title("Agregar Libro")
  mostrar_agregar_libro.geometry("400x200")
  
  isbn_label = Label(mostrar_agregar_libro, text="ISBN:")
  isbn_label.pack()
  isbn_entry= Entry(mostrar_agregar_libro)
  isbn_entry.pack()
  
  nombre_label = Label(mostrar_agregar_libro, text="Nombre:")
  nombre_label.pack()
  nombre_entry= Entry(mostrar_agregar_libro)
  nombre_entry.pack()
  
  precio_label = Label(mostrar_agregar_libro, text="Precio:")
  precio_label.pack()
  precio_entry= Entry(mostrar_agregar_libro)
  precio_entry.pack()
  
  inventario_label = Label(mostrar_agregar_libro, text="Inventario:")
  inventario_label.pack()
  inventario_entry= Entry(mostrar_agregar_libro)
  inventario_entry.pack()
  def guardarLibro():
    isbn = isbn_entry.get()
    nombre = nombre_entry.get()
    precio = precio_entry.get()
    inventario = inventario_entry.get()
    
    if isbn != "" and nombre != "" and precio != "" and inventario != "":
      if validarLibro(isbn):
        messagebox.showerror("Error","Ya hay un Libro con el mismo ISBN.")
        mostrar_agregar_libro.destroy()
      else:
        agregarLibro(isbn, nombre, precio, inventario)
        mostrar_agregar_libro.destroy()
    else:
      messagebox.showinfo("ERROR..", "Por favor ingresa todos los campos")
  guardar_button = Button(mostrar_agregar_libro, text="Guardar", command=guardarLibro)
  guardar_button.pack()
 
def agregarClienteInterfaz():
  mostrar_agregar_cliente= Toplevel()
  mostrar_agregar_cliente.title("Agregar Cliente")
  mostrar_agregar_cliente.geometry("200x150")
  
  IdCliente_label = Label(mostrar_agregar_cliente, text="ID Cliente:")
  IdCliente_label.pack()
  IdCliente_entry= Entry(mostrar_agregar_cliente)
  IdCliente_entry.pack()
  
  nombre_label = Label(mostrar_agregar_cliente, text="Nombre:")
  nombre_label.pack()
  nombre_entry = Entry(mostrar_agregar_cliente)
  nombre_entry.pack()
  
  def guardarCliente():
    Id = IdCliente_entry.get()
    nombre = nombre_entry.get()
    if Id != "" and nombre != "":
      if validarIDClientes(Id):
        messagebox.showerror("Error","Ya hay un cliente con el mismo id.")
        mostrar_agregar_cliente.destroy()
      else:
        agregarCliente(Id, nombre)
        mostrar_agregar_cliente.destroy()
    else:
      messagebox.showinfo("ERROR..", "Por favor ingresa todos los campos")
      
  def cargar_usuarios():
    usuarios = obtener_Clientes()
    tabla_usuarios.delete(*tabla_usuarios.get_children())
    for usuario in usuarios:
      tabla_usuarios.insert("", index='end', values=(usuario[0], usuario[1])) 
            
  guardar_button = Button(mostrar_agregar_cliente, text="Guardar", command=guardarCliente)
  guardar_button.pack()
  
def listaClienteInterfaz():
  ventana_Lista_Clientes = Toplevel()
  ventana_Lista_Clientes.title("LISTA DE CLIENTES")
  ventana_Lista_Clientes.geometry("600x400")
  def cargar_usuarios():
    usuarios = obtener_Clientes()

    for usuario in usuarios:
      tabla_usuarios.insert("", index='end', values=(usuario[0], usuario[1]))
      tabla_frame = Frame(ventana_Lista_Clientes)
      tabla_frame.pack(pady=10)
      
      tabla_usuarios = ttk.Treeview(tabla_frame, columns=("id", "nombre"), show="headings")
      tabla_usuarios.heading("IdCliente", text="ID")
      tabla_usuarios.heading("nombre", text="Nombre")
      tabla_usuarios.pack(side=LEFT, fill=Y)
    
      scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_usuarios.yview)
      scrollbar.pack(side=RIGHT, fill=Y)

      tabla_usuarios.configure(yscrollcommand=scrollbar.set)
      scrollbar.configure(command=tabla_usuarios.yview)

      tabla_usuarios.bind("<ButtonRelease-1>")
    
      cargar_usuarios()
      
      
def eliminarClienteInterfaz():
  mostrar_eliminar_cliente= Toplevel()
  mostrar_eliminar_cliente.title("Eliminar Client")
  mostrar_eliminar_cliente.geometry("200x150")
  
  IdCliente_label = Label(mostrar_eliminar_cliente, text="ID Cliente:")
  IdCliente_label.pack()
  IdCliente_entry= Entry(mostrar_eliminar_cliente)
  IdCliente_entry.pack()

  def eliminar_clientes():
        id = IdCliente_entry.get()
        if id != "":
            if validarIDClientes(id):
                if validadIDClientesVentas(id):
                    messagebox.showerror("En venta", "El usuario ya tiene ventas registradas.")
                else:
                    eliminar_Cliente(id)
                    messagebox.showinfo("Eliminado","El cliente ha sido Eliminado")
                    mostrar_eliminar_cliente.destroy()
            else:
                messagebox.showerror("Error","No hay un cliente con ese Id.")
                mostrar_eliminar_cliente.destroy()
        else:
            messagebox.showerror("Error","Debe llenar el campo")
            cargar_clientes()
  eliminar_button= Button(mostrar_eliminar_cliente, text="Eliminar", command=eliminar_clientes)
  eliminar_button.pack()
    
    
def eliminarLibroInterfaz():
  mostrar_eliminar_libro= Toplevel()
  mostrar_eliminar_libro.title("Eliminar Client")
  mostrar_eliminar_libro.geometry("200x150")
  
  libro_label = Label(mostrar_eliminar_libro, text="ID Cliente:")
  libro_label.pack()
  libro_entry= Entry(mostrar_eliminar_libro)
  libro_entry.pack()

  def eliminar_libro():
        isbn = libro_entry.get()
        if isbn != "":
            if validarLibrosVentas(isbn):
              eliminar_libro()
              messagebox.showinfo("Eliminado","El Libro ha sido Eliminado")
              mostrar_eliminar_libro.destroy()
            else:
                messagebox.showerror("Error","No hay un libro con ese ISBN.")
                mostrar_eliminar_libro.destroy()
        else:
          messagebox.showerror("Error","Debe de haber un ISBN")
          mostrar_eliminar_libro.destroy()
                
  eliminar_button= Button(mostrar_eliminar_libro, text="Eliminar", command=eliminar_libro)
  eliminar_button.pack()

    
    
      





