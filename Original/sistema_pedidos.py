# sistema_pedidos.py  — CON ERRORES INTENCIONADOS

import datetime

productos = {
    'cafe':    {'precio': 2.5,  'stock': 10},
    'te':      {'precio': 2.0,  'stock': 5},
    'zumo':    {'precio': 3.0              },  # ← falta 'stock'
}

historial = []

def calcular_total(pedido):
    total = 0
    for item in pedido:
        total = total + productos[item]['precio']  # ← KeyError si no existe
    return total / len(pedido)                     # ← BUG: debería ser sum, no promedio

def registrar_pedido(cliente, pedido):
    if len(pedido) > 0:
        total = calcular_total(pedido)
        fecha = datetime.date.today
        historial.append({
            'cliente': cliente,
            'pedido':  pedido,
            'total':   total,
            'fecha':   fecha
        })
        print('Pedido de ' + cliente + ' registrado: ' + total)  # ← TypeError

def obtener_resumen():
    if historial == []:
        return 'No hay pedidos'
    totales = []
    for registro in historial:
        totales.append(registro['total'])
    media = sum(totales) / len(totales)
    return f'Total pedidos: {len(historial)} | Media: {media}'

# Test
registrar_pedido('Ana', ['cafe', 'te'])
registrar_pedido('Luis', ['zumo', 'cafe'])
print(obtener_resumen())
