import datetime

productos = {
    'cafe': {'precio': 2.5, 'stock': 10},
    'te':   {'precio': 2.0, 'stock': 5},
    'zumo': {'precio': 3.0, 'stock': 8}, # Corregido: añadido stock faltante
}

historial = []

def calcular_total(pedido):
    total = 0
    for item in pedido:
        # Validación: Comprobar si el producto existe antes de sumar
        if item in productos:
            total += productos[item]['precio']
        else:
            print(f"Advertencia: El producto '{item}' no existe en la carta.")
            
    # BUG CORREGIDO: Eliminada la división por len(pedido) para que sea el total real
    return total

def registrar_pedido(cliente, pedido):
    if len(pedido) > 0:
        total = calcular_total(pedido)
        
        # BUG CORREGIDO: Añadidos () para llamar a la función y obtener la fecha real
        fecha = datetime.date.today() 
        
        historial.append({
            'cliente': cliente,
            'pedido':  pedido,
            'total':   total,
            'fecha':   fecha
        })
        
        # BUG CORREGIDO: Uso de f-string para evitar el TypeError de concatenación
        print(f"Pedido de {cliente} registrado: {total:.2f}€")

def obtener_resumen():
    if not historial: # Forma más "Pythonic" de preguntar si una lista está vacía
        return 'No hay pedidos'
        
    totales = [registro['total'] for registro in historial]
    media = sum(totales) / len(totales)
    
    return f'Total pedidos: {len(historial)} | Media por pedido: {media:.2f}€'

# --- Test de ejecución ---
registrar_pedido('Ana', ['cafe', 'te'])
registrar_pedido('Luis', ['zumo', 'cafe'])
# Test de producto inexistente para probar robustez
registrar_pedido('Marta', ['cafe', 'galletas']) 

print("---")
print(obtener_resumen())