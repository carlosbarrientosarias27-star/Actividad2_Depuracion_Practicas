"""Módulo encargado del almacenamiento y consulta del historial de pedidos."""

_registros = []

def guardar_pedido(datos_pedido):
    """
    Almacena un pedido en el historial.
    :param datos_pedido: dict con la información del pedido.
    """
    _registros.append(datos_pedido)

def obtener_todos():
    """Retorna la lista completa de pedidos realizados."""
    return _registros

def generar_estadisticas():
    """
    Calcula el resumen de ventas.
    :return: str con el resumen o mensaje de error.
    """
    if not _registros:
        return 'No hay pedidos'
        
    totales = [r['total'] for r in _registros]
    media = sum(totales) / len(totales)
    
    return f'Total pedidos: {len(_registros)} | Media por pedido: {media:.2f}€'