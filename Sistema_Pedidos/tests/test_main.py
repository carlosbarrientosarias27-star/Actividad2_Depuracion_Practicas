import pytest
from unittest.mock import patch
import main

def test_ejecutar_salir_inmediato():
    """Verifica que el programa termine si el usuario elige la opción de salir (3)."""
    # Simulamos que el usuario escribe '3' directamente
    with patch('main.input', return_value='3'):
        # Si no termina, el test se quedaría en un bucle infinito
        main.ejecutar_app() 

def test_ejecutar_opcion_estadisticas():
    """Verifica que la opción 2 llame a generar_estadisticas."""
    # Simulamos entrada '2' y luego '3' para salir
    with patch('main.input', side_effect=['2', '3']), \
         patch('historial.generar_estadisticas') as mock_est:
        
        mock_est.return_value = "Estadísticas de prueba"
        main.ejecutar_app()
        
        mock_est.assert_called_once()

def test_ejecutar_flujo_pedido_completo():
    """Verifica que la opción 1 pida datos y llame a procesar_nuevo_pedido."""
    inputs = [
        '1',        # Opción: Nuevo pedido
        'Carlos',   # Nombre del cliente
        'cafe,te',  # Productos
        '3'         # Opción: Salir
    ]
    
    with patch('main.input', side_effect=inputs), \
         patch('pedidos.procesar_nuevo_pedido') as mock_procesar:
        
        main.ejecutar_app()
        
        # Verificamos que se llamó a la lógica de pedidos con los datos limpios
        mock_procesar.assert_called_once_with('Carlos', ['cafe', 'te'])

@patch('main.input', side_effect=['opcion_invalida', '3'])
def test_ejecutar_opcion_no_valida(mock_input):
    """Verifica que el programa no rompa ante una opción no reconocida."""
    # Simplemente nos aseguramos de que termine sin excepciones
    main.ejecutar_app()