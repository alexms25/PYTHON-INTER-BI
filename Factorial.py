def factorial(numero, multi, cons):
    multicacion = (numero*multi)
    contador = numero - 1
    if contador > 0:
        return factorial(contador, multicacion, cons)
    elif contador == 0:
        print (cons,'!=', multi)


x = input ('Ingrese un valor: ')
factor = int(x)
factorial(factor, 1, factor)