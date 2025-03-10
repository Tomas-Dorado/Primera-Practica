from Cliente import Cliente
from Empresa import Empresa 

# Crear 4 clientes
cliente1 = Cliente(dni="12345678A", nombre="Juan", apellido="Pérez")
cliente2 = Cliente(dni="23456789B", nombre="María", apellido="García")
cliente3 = Cliente(dni="34567890C", nombre="Carlos", apellido="López")
cliente4 = Cliente(dni="45678901D", nombre="Ana", apellido="Martínez")

empresa=Empresa(clientes=[cliente1, cliente2, cliente3, cliente4])
# Imprimir los clientes
print(cliente1)
print(cliente2)
print(cliente3)
print(cliente4)

print('Clientes de la empresa')
print(empresa.clientes)

print("\n==MOSTRAR CLIENTES POR DNI==")
# Consulto clientes por DNI
empresa.mostrar_clientes("12345678A")
empresa.mostrar_clientes("23456789B")

#muestreo de nuevo todos los clientes
print("\n==LISTADO DE CLIENTES==")
print(empresa.clientes)

#añadir un nuevo cliente
cliente5 = Cliente(dni="56789012E", nombre="Laura", apellido="Gómez")
empresa.borrar_cliente("12345678A")
print("\n==LISTADO DE CLIENTES==")
empresa.añadir_cliente(cliente5)
print(empresa.clientes)



