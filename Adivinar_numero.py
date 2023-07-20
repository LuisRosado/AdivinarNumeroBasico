
import random

numero_secreto = (random.randint(1, 5))
numero_usuario = int(input('Adivine un numero aleatorio del 1 al 5: '))

if numero_secreto == numero_usuario:
    print('Felicidades,¿Eres Adivino?')
else:
    print('Suerte para la proxima crack')
    print('El numero era: ',numero_secreto)


