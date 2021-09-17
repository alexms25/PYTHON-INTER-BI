def cuadrado(_lista):
    numero = _lista **2
    return numero

def Lista(lista):
    contador = len(lista)
    lista_nueva = []
    for x in lista:
        contador -= 1
        if contador >= 0:
            y = (cuadrado(x))
            lista_nueva.append(y)
        if contador == 0:
            print (lista_nueva)




lista = [1, 2, 3, 4, 5]
(Lista(lista))
