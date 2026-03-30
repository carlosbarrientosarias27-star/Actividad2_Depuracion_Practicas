import pytest
from historial import guardar_pedido, obtener_todos, generar_estadisticas, _registros

@pytest.fixture(autouse=True)
def limpiar_historial():
    """
    Fixture que se ejecuta automáticamente antes de cada test
    para vaciar el historial global y asegurar la independencia.
    """
    _registros.clear()

def test_guardar_pedido_y_obtener_todos():
    """Verifica que los pedidos se guarden y recuperen correctamente."""
    pedido = {'id': 1, 'total': 15.5}
    guardar_pedido(pedido)
    
    resultados = obtener_todos()
    
    assert len(resultados) == 1
    assert resultados[0] == pedido
    assert resultados[0]['total'] == 15.5

def test_generar_estadisticas_vacio():
    """Verifica el mensaje cuando no hay registros en el historial."""
    mensaje = generar_estadisticas()
    assert mensaje == 'No hay pedidos'

def test_generar_estadisticas_con_datos():
    """Verifica el cálculo correcto de la media y el conteo total."""
    guardar_pedido({'total': 10.0})
    guardar_pedido({'total': 20.0})
    guardar_pedido({'total': 30.0})
    
    # Total = 60, Media = 20.00
    mensaje = generar_estadisticas()
    
    assert 'Total pedidos: 3' in mensaje
    assert 'Media por pedido: 20.00€' in mensaje

def test_integridad_multiples_pedidos():
    """Verifica que el orden y contenido se mantienen al guardar varios pedidos."""
    pedidos = [
        {'id': 101, 'total': 5.0},
        {'id': 102, 'total': 12.0}
    ]
    
    for p in pedidos:
        guardar_pedido(p)
        
    assert obtener_todos() == pedidos
    assert len(obtener_todos()) == 2