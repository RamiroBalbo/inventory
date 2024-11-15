class Producto:
    def __init__(self, nombre, cantidad):
        self._nombre = nombre
        self._cantidad = cantidad

    def sumarProductos(self, cantidad):
        self._cantidad += cantidad

    def restarProductos(self, cantidad):
        self._cantidad -= cantidad

    def __str__(self):
        return f"{self._nombre} - {self._cantidad}"

class Almacen:
    def __init__(self):
        self._inventario = []

    def agregarProducto(self, producto):
        productoExistente = next((elemento for elemento in self._inventario if elemento._nombre == producto._nombre), None)

        if productoExistente is None:
            self._inventario.append(producto)
        else:
            productoExistente.sumarProductos(producto._cantidad)

    def sacarProductos(self, producto, cantidad):
        if producto.restarProductos(cantidad) == 0:
            self._inventario.remove(producto)

    def mostrarInventario(self):
        return print(list(map(lambda producto: producto.__str__(), self._inventario)))

    @property
    def inventario(self):
        return self._inventario


