#Diseña un algoritmo que permita mostrar las
#tablas de multiplicar del 1 al 10

#Entrada
print('tabla de multiplicación')

for x in range(11):
    for y in range(11):
        print(f'{x} * {y} es {x*y}')
