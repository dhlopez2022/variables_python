# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
print('Ingrese por consola el primer número entero a operar:')
numero_1 = int(input())

print('Ingrese por consola el segundo número entero a operar:')
numero_2 = int(input())

# Alumno: Imprima en pantalla los dos números enteros solicitados
print('los numeros ingresados son', numero_1 , numero_2)

# Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
Total_Suma = (numero_1) + (numero_2)
Total_Resta = (numero_1) - (numero_2)
Total_Division = (numero_1) / (numero_2)
Total_Multiplication = (numero_1) * (numero_2)
Total_Potencia = (numero_1) ** (numero_2)
 
print('la resta de los numeros ingresados es', Total_Resta)
print('la Division de los numeros ingresados es', Total_Division)
print('la Multiplicacion de los numeros ingresados es', Total_Multiplication)

# numero_1, numero_2
# Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
# El resultado de sumar 4 y 2 es 6
# NOTA: No coloque usted los nùmeros y resultados, use las variables

# Suma
print('la suma de los numeros' ,numero_1,  'y' ,numero_2,'es', Total_Suma)

# Resta

print('la resta de los numeros' ,numero_1,  'y' ,numero_2,'es', Total_Resta)

# División

print('la Division de los numeros' ,numero_1,  'y' ,numero_2,'es', Total_Division)

# Multiplicación

print('la Multiplicacion de los numeros' ,numero_1,  'y' ,numero_2,'es', Total_Multiplication)

#  Exponente/Potencia

print('La potencia entre', numero_1, 'y', numero_2, 'es', Total_Potencia)

print('')