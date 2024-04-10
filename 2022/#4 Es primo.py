'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 
'''
def primo (numero):
    if numero <2:
        print(False)
    elif numero > 100:
        print("Numero no invalido")
    elif numero % numero == 0 and numero % 1 == 0:
        numero = True
        print(numero)
    else:
        numero = False
        print(numero)

primo(23)
