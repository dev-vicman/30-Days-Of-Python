# 💻 Exercises - Day 9

## Ejercicios: Nivel 1

### Itera del 0 al 10 usando el bucle for, haz lo mismo usando el bucle while.

```python
for i in range(0,11):
    print(i)

contador = 0
while contador < 11:
    print(contador)
    contador += 1
```

### Itera de 10 a 0 usando el bucle for, haz lo mismo usando el bucle while.

```python
for i in range(10,0,-1):
    print(i)

contador = 10
while contador > -1:
    print(contador)
    contador -= 1
```

### Escriba un bucle que realice siete llamadas a print(), de modo que obtengamos en la salida el siguiente triángulo:

```#
##
###
####
#####
######
#######
```

```python
for i in range(1,8):
    print("#"*i)
```

### Utilice bucles anidados para crear lo siguiente:

```
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
```

```python
for i in range(9):
    for j in range(9):
        print("#", end=" ")
    print()
```

### Imprima el siguiente patrón:

```
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
```
```python
for i in range(11):
    print(f"{i} x {i} = {i * i}" )
```

### Itere a través de la lista, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] usando un bucle for e imprima los elementos.

```
lista =  ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for i in lista:
    print(i)
```

### Utilice el bucle for para iterar de 0 a 100 e imprimir solo números pares

```python
for i in range(0,101):
    if i % 2 == 0:
        print(i)
```
### Utilice el bucle for para iterar de 0 a 100 e imprimir solo números impares

```python
for i in range(0,101):
    if i % 2 != 0:
        print(i)
```

## Ejercicios: Nivel 2

### Utilice el bucle for para iterar de 0 a 100 e imprimir la suma de todos los números.

```python
suma_total = 0
for i in range(0,101):
    suma_total += i
print(f"\nLa suma de todos los numeros del 0 al 100 es: {suma_total}")
```

### Utilice el bucle for para iterar de 0 a 100 e imprimir la suma de todos los números pares y la suma de todos los números impares.

```python
suma_pares = 0
suma_impares = 0

for i in range(0,101):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i

print(f"\nLa suma de numeros pares es {suma_pares} y la de numeros impares es {suma_impares}")
```

## Ejercicios: Nivel 3
#### Vaya a la carpeta de datos y utilice el archivo countries.py . Recorra los países y extraiga todos los países que contengan la palabra land.

```python
for pais in countries:
    if "land" in pais:
        print(pais)
```

## Esta es una lista de frutas, ['banana', 'naranja', 'mango', 'limón'] invierte el orden usando un bucle.

```python
frutas = ['banana', 'naranja', 'mango', 'limón']

frutas_invertidas = []

for fruta in range(len(frutas) - 1,-1,-1):
    frutas_invertidas.append(frutas[fruta])

print(frutas)
print(frutas_invertidas)
```

### ¿Cuál es el número total de idiomas en los datos?

```python
numero_idiomas = []

for pais in countries_data:
    for idioma in pais["languages"]:
        numero_idiomas.append(idioma)

set(numero_idiomas)
print(f"\nEl numero total de idiomas es {len(numero_idiomas)} idiomas distintos")
```