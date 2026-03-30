import pytest
from productos import obtener_precio, existe_producto, CATALOGO

def test_existe_producto_exitoso():
    """Verifica que los productos presentes en el catálogo sean detectados."""
    assert existe_producto('cafe') is True
    assert existe_producto('te') is True
    assert existe_producto('zumo') is True

def test_existe_producto_inexistente():
    """Verifica que devuelva False para productos que no están en el catálogo."""
    assert existe_producto('agua') is False
    assert existe_producto('') is False
    assert existe_producto(None) is False

def test_obtener_precio_correcto():
    """Verifica que se recupere el precio exacto definido en el catálogo."""
    assert obtener_precio('cafe') == 2.5
    assert obtener_precio('te') == 2.0
    assert obtener_precio('zumo') == 3.0

def test_obtener_precio_inexistente():
    """Verifica que devuelva None si el producto no existe."""
    assert obtener_precio('cerveza') is None

@pytest.mark.parametrize("producto, precio_esperado", [
    ('cafe', 2.5),
    ('te', 2.0),
    ('zumo', 3.0),
])
def test_obtener_precio_parametrizado(producto, precio_esperado):
    """Prueba redundante pero elegante usando parametrización para múltiples casos."""
    assert obtener_precio(producto) == precio_esperado

def test_integridad_catalogo():
    """Verifica que el catálogo tenga la estructura de datos esperada."""
    for producto, datos in CATALOGO.items():
        assert 'precio' in datos
        assert 'stock' in datos
        assert isinstance(datos['precio'], (int, float))
        assert isinstance(datos['stock'], int)