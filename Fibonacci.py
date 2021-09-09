def fibonacci(numero1, numero2, tam):
    secuencia = int(tam)
    secuencia -= 1

    if secuencia > 0:
        print (numero1, numero2, '|' ,numero1+numero2)
        return fibonacci(numero2, numero1+numero2, secuencia)
    elif secuencia == 0:
        print ('A llegado al fin del tamaño de la secuencia')
    

sec = input('Ingrese el tamaño de la secuencia: ')
fibonacci(0, 1,  sec)   
