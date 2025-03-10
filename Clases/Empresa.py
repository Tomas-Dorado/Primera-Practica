class Empresa:
    def __init__(self, clientes=[]):
        self.clientes = clientes
        
    def mostrar_clientes(self, dni=None):
        for c in self.clientes:
            if c.dni== dni:
                print(c)
                return 
        print('Cliente no encontrado')
        
    def borrar_cliente(self, dni=None):
        for i, c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c), '> BORRADO')
                return
        print('Cliente no encontrado')
    
    def añadir_cliente(self, cliente):
        self.clientes.append(cliente)
        print(cliente, '> AÑADIDO')