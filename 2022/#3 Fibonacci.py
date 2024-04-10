''' 
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 '''
#prime numero
num1 = 0
#segundo numero
num2 = 1
#contador
cont = 0
#resultado
while cont < 50:
    
    print(num1)
    
    cont += 1
    total =  (num1 + num2)
    #Actualizamos las variables
    num1 = num2
    num2 = total
    
    
print ("-----------------------------------------------")
    
    
#Otra mandera de resolver el fibonacci   
def fibonacci(n):
    # Validar
    if n == None:
        return 
    elif n < 0:
        return "Número erróneo"
    # Algoritmo
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))
    
print ("-----------------------------------------------")

#otra solucion
def fibonaccii():
    
    anterior = 0
    siguiente = 1
    
    for j in range(0,51):
        print(siguiente)
        fibonacci = anterior + siguiente
        anterior = siguiente
        siguiente = fibonacci

fibonaccii()