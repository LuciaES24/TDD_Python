def test_mayor_lista():
    lista = [3,4,5,6,80]
    mayor = 80
    assert menor_lista(lista) == mayor

def test_menor_lista():
    lista = [32,41,5,8,80]
    menor = 8
    assert menor_lista(lista) == menor