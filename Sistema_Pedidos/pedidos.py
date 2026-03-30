"""Módulo encargado de la lógica de procesamiento y registro de pedidos."""

import datetime
import productos
import historial

def calcular_total(lista_items):
    """
    Suma los precios de los productos válidos en el pedido.
    :param lista_items: list de strings con los nombres de productos.
    :return: float total calculado.
    """
    total = 0.0
    for item in lista_items:
        precio = productos.obtener_precio(item)
        if precio is not None:
            total += precio
        else:
            print(f"Advertencia: El producto '{item}' no existe en la carta.")
    return total

def procesar_nuevo_pedido(cliente, lista_items):
    """
    Valida, calcula y envía el pedido al historial.
    :param cliente: str nombre del cliente.
    :param lista_items: list de productos solicitados.
    """
    if not lista_items:
        return

    total = calcular_total(lista_items)
    
    nuevo_pedido = {
        'cliente': cliente,
        'pedido':  lista_items,
        'total':   total,
        'fecha':   datetime.date.today()
    }
    
    historial.guardar_pedido(nuevo_pedido)
    print(f"Pedido de {cliente} registrado: {total:.2f}€")