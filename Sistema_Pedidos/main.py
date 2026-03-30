"""Punto de entrada principal del sistema de cafetería."""

from pedidos import procesar_nuevo_pedido
from historial import generar_estadisticas

def ejecutar_app():
    while True:
        # Los tests simulan este input() para elegir la opción
        opcion = input("Seleccione una opción (1: Nuevo, 2: Estadísticas, 3: Salir): ")
        
        if opcion == '1':
            nombre = input("Nombre del cliente: ")
            productos_str = input("Productos (separados por coma): ")
            # Limpiamos espacios y creamos la lista
            lista_productos = [p.strip() for p in productos_str.split(',')]
            # El test verificará que esta función se llame con estos datos
            procesar_nuevo_pedido(nombre, lista_productos)
            
        elif opcion == '2':
            # El test verificará que se llame a generar_estadisticas
            stats = generar_estadisticas()
            print(stats)
            
        elif opcion == '3':
            # Rompe el bucle para que el test 'test_ejecutar_salir_inmediato' finalice
            break
            
        else:
            # Maneja el caso de 'opcion_invalida' del test
            print("Opción no válida")

if __name__ == "__main__":
    ejecutar_app()