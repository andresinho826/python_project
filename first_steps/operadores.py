# operadores aritmeticos


print(f"suma: 10 + 3 = {10 + 3}")
print(f"resta: 10 - 3 = {10 - 3}")
print(f"multiplicacion: 10 * 3 = {10 * 3}")
print(f"division: 10 + 3 = {10 / 3}")
print(f"modulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"division entera: 10 // 3 = {10 // 3}")


"""
    operadores de comparacion

igualdad ==
desigualdad !=
mayor que >
menor que <
mayor o igual que >=
menor o igual que <=

    operadores logicos

and &&
or ||
not !


    operadores de asignacion

my_number = 11 #asignacion
+= asginacion y suma
-= resta y asignacion , division y asignacion y multiplicacion, modulo, exponente, divison entera. etc


    operadores de identidad

NOTA: comparan el valor en memoria, podemos comparar 2 variables para validar si estan en el mismo espacio de memoria

"""

print(f"'a' in 'andres' = {'a' in 'andres'}")   # compara si la a esta dentro de andres
print(f"'x' in 'andres' = {'x' not in 'andres'}")


"""
    operadores de bit
    
a=10 #1010
b=3 # 0011


    estructuras de control
    
if else elif

ciclo for

for i in range(10)
    print(i)
    
ciclo while


    manejo de excepciones

try:
    print(10/0)
except:
    print("se ha presentado un error")
finally:
    print("He finalizado el manejor de excepciones")
    
"""

"""
ejercicio de aplicacion

-> muestra los numero del 10 al 56
-> donde se observen solo los pares
-> que no se muestre el #16
-> ni los multiplos de 3
"""

for number in range(10,56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
