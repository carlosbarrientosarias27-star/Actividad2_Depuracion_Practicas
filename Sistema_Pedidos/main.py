"""Punto de entrada principal del sistema de cafetería."""

from pedidos import procesar_nuevo_pedido
from historial import generar_estadisticas

def ejecutar_app():
    # --- Test de ejecución ---
    procesar_nuevo_pedido('Ana', ['cafe', 'te'])
    procesar_nuevo_pedido('Luis', ['zumo', 'cafe'])
    
    # Test de producto inexistente para probar robustez
    procesar_nuevo_pedido('Marta', ['cafe', 'galletas'])

    print("---")
    print(generar_estadisticas())
    

if __name__ == "__main__":
    ejecutar_app()