#criar um programa que ajude o usuario a fazer calculos basicos rapidamente 
from time import sleep


print('[1] Adiçao' )
print('[2] Subtraçao' )
print('[3] Multiplicaçao' )
print('[4] Divisao')
operador = int(input('Olá, qual será o operador deste calculo? '))
if operador == 1:
    n1 = int(input('Digite um numero para calcularmos: '))
    n2 = int(input('Digite outro numero: '))
    resultado = n1 + n2
    print('A resultado da soma entre {} mais {} é {}! '.format(n1, n2, resultado))
    sleep(3.5)

elif operador == 2:
    n1 = int(input('Digite um numero para calcularmos: '))
    n2 = int(input('Digite outro numero: '))
    resultado = n1 - n2
    print('O resultado da subtraçao dos numeros {} menos {} é {}! '. format(n1, n2, resultado))
    sleep(3.5)

elif operador == 3:
    n1 = int(input('Digite um numero para calcularmos: '))
    n2 = int(input('Digite outro numero: '))
    resultado = n1 * n2
    print('O resultado da multiplicaçao entre {} multiplicado por {} é {}! '.format(n1, n2, resultado))
    sleep(3.5)

elif operador == 4:
    n1 = int(input('Digite um numero para calcularmos: '))
    n2 = int(input('Digite outro numero: '))
    resultado = n1 / n2
    print('O resultado da divisao entre {} divido por {} é {}! '.format(n1, n2, resultado)) 
    sleep(3.5)
                
else:
    print('Digite um numero que esteja de acordo com os operadores. ')
    sleep(3.5)
        
    
        
    
        
        
        
             