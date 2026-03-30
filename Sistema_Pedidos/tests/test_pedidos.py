import pytest
from unittest.mock import patch, MagicMock
from pedidos import calcular_total, procesar_nuevo_pedido
import datetime

# --- Tests para calcular_total ---

def test_calcular_total_productos_validos():
    """Verifica el cálculo correcto cuando todos los productos existen."""
    # Simulamos que productos.obtener_precio devuelve valores específicos
    with patch('productos.obtener_precio') as mock_precio:
        mock_precio.side_effect = lambda x: 2.5 if x == 'cafe' else 2.0
        
        items = ['cafe', 'te']
        total = calcular_total(items)
        
        assert total == 4.5
        assert mock_precio.call_count == 2

def test_calcular_total_con_producto_inexistente():
    """Verifica que ignore productos que no están en el catálogo (retornan None)."""
    with patch('productos.obtener_precio') as mock_precio:
        # 'cafe' devuelve 2.5, 'invisible' devuelve None
        mock_precio.side_effect = lambda x: 2.5 if x == 'cafe' else None
        
        items = ['cafe', 'invisible']
        total = calcular_total(items)
        
        assert total == 2.5

# --- Tests para procesar_nuevo_pedido ---

def test_procesar_nuevo_pedido_vacio():
    """Verifica que si no hay items, no se guarde nada en el historial."""
    with patch('historial.guardar_pedido') as mock_guardar:
        procesar_nuevo_pedido("Juan", [])
        mock_guardar.assert_not_called()

def test_procesar_nuevo_pedido_completo():
    """Verifica que el pedido se construya y envíe al historial correctamente."""
    cliente = "Ana"
    items = ['cafe', 'zumo']
    total_esperado = 5.5
    fecha_hoy = datetime.date.today()

    # Mockeamos tanto la lógica de precios como la de guardado
    with patch('productos.obtener_precio') as mock_precio, \
         patch('historial.guardar_pedido') as mock_guardar:
        
        # Configuramos los retornos de los mocks
        mock_precio.side_effect = lambda x: 2.5 if x == 'cafe' else 3.0
        
        procesar_nuevo_pedido(cliente, items)
        
        # Verificamos que se llamó a guardar_pedido con el diccionario correcto
        mock_guardar.assert_called_once()
        args, _ = mock_guardar.call_args
        pedido_generado = args[0]
        
        assert pedido_generado['cliente'] == cliente
        assert pedido_generado['pedido'] == items
        assert pedido_generado['total'] == total_esperado
        assert pedido_generado['fecha'] == fecha_hoy