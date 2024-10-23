def es_palindromo(lista:list) -> bool:
    if(lista == lista.reverse): return True
    else: return False