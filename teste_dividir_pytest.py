import pytest

def dividir(a,b):
    return a / b

def test_dividir_positivos():
    assert dividir(10, 2) == 5
def test_dividir_negativos():
    assert dividir(-10, -2) == 5
def test_dividir_zero():
    assert dividir(0, 5) == 0
def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(5, 0)
