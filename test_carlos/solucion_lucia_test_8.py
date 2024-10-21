def palindromo(palabra:str) -> bool:
    lista = list(palabra)
    lista_temporal = lista[::-1]
    if lista == lista_temporal:
        return True
    else:
        return False