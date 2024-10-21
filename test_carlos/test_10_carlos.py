from solucion_lucia_test_10 import *

def test_mayor_lista():
    lista = [3,4,5,6,80]
    mayor = 80
    assert mayor_lista(lista) == mayor

def test_menor_lista():
    lista = [32,41,9,8,80]
    menor = 8
    assert menor_lista(lista) == menor