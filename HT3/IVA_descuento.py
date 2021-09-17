#DESCUENTO DEL IVA
def IVA(precio):
    return (precio-(precio*0.12)) 

#DECUENTO DEL 50%
def descuento(precio):
    return (precio-(precio*0.10))


#Suma y descuento
def Cesta(precio_final):
    x = list(precio_final.values())
    y = 0
    for x in x:
       y += x
       total = y
    return (factura(total))

    

def factura (total):
    x = print('Su total es de:', total)
    y = print('Su total sin IVA es de:', IVA(total))
    z = print('Debido a que estamos de ANIVERSARIO, le aplicaremos un 10% de descuento en su total')
    t = print('Su total a pagar es de:', descuento(total))
    return (x, y, z, t)




cesta = {'Leche' : 7.5, 'Huevos' : 31, 'Azúcar' : 5, 'Frijol' : 7, 'Arroz' : 4}
(Cesta(cesta))






