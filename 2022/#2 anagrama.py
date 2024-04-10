'''  
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
NO hace falta comprobar que ambas palabras existan.
Dos palabras exactamente iguales no son anagrama.
'''
p1="roma"
p2="amoR"


def anagrama(p1,p2):
    
    if p1.lower() == p2.lower():
        return False
    return sorted(p1.lower()) == sorted(p1.lower())

print(anagrama(p1,p2))