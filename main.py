from operator import index

from classes import Almacen, Producto
def mostrar_menu():
    print("\n---- Menú ----")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Sacar producto")
    print("4. Salir")
    opcion = input("Selecciona una opción (1/2/3/4): ")
    return opcion


def main():
    almacen = Almacen()

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            nombre = input("Introduce el nombre del producto: ")
            cantidad = int(input(f"Introduce la cantidad de {nombre}: "))
            producto = Producto(nombre, cantidad)
            almacen.agregarProducto(producto)
            print(f"{nombre} ha sido agregado al inventario.")

        elif opcion == '2':
            almacen.mostrarInventario()

        elif opcion == '3':
            nombre = input("Introduce el nombre del producto a sacar: ")
            cantidad = int(input(f"Introduce la cantidad de {nombre} a sacar: "))
            producto = next((producto for producto in almacen.inventario if producto.nombre == nombre), None)
            almacen.sacarProductos(producto, cantidad)

        elif opcion == '4':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, por favor elige 1, 2, 3 o 4.")


# Ejecutar el programa
if __name__ == "__main__":
    main()

