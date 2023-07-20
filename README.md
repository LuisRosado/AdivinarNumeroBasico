# AdivinarNumeroBasico
Juego basico de adivinar un numero entre 1 y 5

Este código en Python es un pequeño juego en el que el usuario debe adivinar un número aleatorio del 1 al 5. A continuación, te explico cada parte del código:

import random: Importa el módulo "random" de Python, que proporciona funciones para generar números aleatorios.

numero_secreto = (random.randint(1, 5)): Genera un número aleatorio entre 1 y 5 (ambos inclusive) y lo guarda en la variable numero_secreto.

numero_usuario = int(input('Adivine un numero aleatorio del 1 al 5: ')): Pide al usuario que ingrese un número y lo guarda en la variable numero_usuario. La función input() toma el valor ingresado por el usuario como una cadena de caracteres, por lo que se utiliza int() para convertirlo a un número entero.

if numero_secreto == numero_usuario:: Comprueba si el número secreto (numero_secreto) es igual al número ingresado por el usuario (numero_usuario).

print('Felicidades,¿Eres Adivino?'): Si el número ingresado por el usuario es igual al número secreto, imprime un mensaje de felicitaciones.

else:: Si el número ingresado por el usuario no es igual al número secreto, ejecuta el bloque de código que sigue.

print('Suerte para la proxima crack'): Imprime un mensaje de aliento indicando que tenga más suerte la próxima vez.

print('El numero era: ',numero_secreto): Muestra el número secreto que el usuario debía adivinar, para que sepa cuál era.

En resumen, el programa genera un número aleatorio del 1 al 5, le pide al usuario que adivine ese número y luego verifica si el número ingresado por el usuario es correcto o no, mostrando un mensaje apropiado en cada caso.
