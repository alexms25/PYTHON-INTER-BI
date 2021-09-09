def adivinanza(color, o):
    #La fruta es fresa
    o -= 1
    fruta = color.upper()
    if fruta == ("Rojo") and o > 0:
        print ('¡Felicidades!, la fruta en la que estaba pensando es la FRESA :)')
    elif fruta != ("Rojo") and o > 0:
        print ('¡No!, la fruta en que estoy pensando no es de color:', color, ', te quedan', o, 'oportunidades.')
        color = input('Adivina el color de la fruta en la que estoy pensando: ')
        return adivinanza(color, o)
    elif o == 0:
        print ('GAME OVER')
        print ('Estaba pensando en una FRESA ROJA :(')


color_fruta = input('Adivina el color de la fruta en la que estoy pensando: ')
adivinanza(color_fruta, 3)