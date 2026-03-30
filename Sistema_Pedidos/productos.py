"""Módulo encargado de la gestión del catálogo de productos y stock."""

CATALOGO = {
    'cafe': {'precio': 2.5, 'stock': 10},
    'te':   {'precio': 2.0, 'stock': 5},
    'zumo': {'precio': 3.0, 'stock': 8},
}

def obtener_precio(nombre_producto):
    """
    Retorna el precio de un producto si existe en el catálogo.
    :param nombre_producto: str con el nombre del producto.
    :return: float precio o None si no existe.
    """
    producto = CATALOGO.get(nombre_producto)
    return producto['precio'] if producto else None

def existe_producto(nombre_producto):
    """
    Verifica si un producto está en el catálogo.
    :param nombre_producto: str nombre del producto.
    :return: bool.
    """
    return nombre_producto in CATALOGO