def menor_lista(lista:list) -> int:
    lista_ordenada : list[int] = sorted(lista)
    return lista_ordenada[0]

def mayor_lista(lista:list) -> int:
    lista_ordenada : list[int] = sorted(lista)
    mayor_posicion = len(lista_ordenada)
    return lista_ordenada[mayor_posicion-1]
