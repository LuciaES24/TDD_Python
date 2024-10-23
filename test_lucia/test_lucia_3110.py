from carlos_3110 import *

def test_menor_numero():
    menor = 8
    lista = [8,10,12,31]
    assert menor_numero_encontrado(lista) == menor

def test_mayor_numero():
    mayor = 80
    lista = [12,80,33,43]
    assert mayor_numero_encontrado(lista) == mayor 