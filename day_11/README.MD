# 💻 Ejercicios: Día 11

## Ejercicios: Nivel 1

### 1. Declara una función add_two_numbers . Toma dos parámetros y devuelve una suma.

```python
def add_two_numbers(numero_1, numero_2):
    """
    Calcula la Suma de 2 numeros
    
    Argumentos:
        
        numero_1 (int, Float): El primer numero a sumar    
        numero_2 (int, Float): El segundo numero a sumar
        
    Return:

        int, float  La suma de 2 numeros    
    """
    return numero_1 + numero_2

print(f'La suma de los numeros es: {add_two_numbers(4, 6)}')
```
##### Print Output:
    La suma de los numeros es: 10
---
### 2. El área de un círculo se calcula de la siguiente manera: área = π x r x r. Escribe una función que calcule área_del_círculo.

```python
def area_del_circulo(radio):
    """
    Calcula el area de un circulo
    
    Argumentos:
    
        radio (int, float): El radio de el circulo
        
    Return:

        int, float: El area de un circulo
    """
    area = 3.1416 * radio * radio
    return round(area,2)

print(f'El area del circulo es: {area_del_circulo(34)}')
```
##### Print Output:
    El area del circulo es: 3631.69
---
### 3. Escriba una función llamada add_all_nums que tome una cantidad arbitraria de argumentos y sume todos los argumentos. Verifique si todos los elementos de la lista son de tipo numérico. Si no es así, proporcione una respuesta razonable.

```python
def add_all_nums(*numeros):
    suma = 0
    for num in numeros:
        if isinstance(num, (int,float)):
            suma += num
        else:
            print(f"{num} no es un numero, no se incluira en la suma")
    return suma

resultado = add_all_nums(1, 2, 'a', 3.5)
print(f"La suma de los números es: {resultado}")
```
##### Print Output:
    La suma de los números es: 6.5
---

### 4. La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. Escriba una función que convierta °C a °F, convert_celsius_to-fahrenheit.

```python
def convert_celsius_to_fahrenheit(grados):
    farenheit = (grados * 1.8) + 32
    return farenheit

print(f'La temparatura es de {convert_celsius_to_fahrenheit(40)} farenheit')
```
##### Print Output:
    La temparatura es de 104.0 farenheit
---

### 5. Escriba una función llamada check-season, toma un parámetro de mes y devuelve la temporada: Otoño, Invierno, Primavera o Verano.

```python
def check_season(mes):
    primavera = ['Marzo','Abril','Mayo']
    verano = ['Junio','Julio','Agosto']
    otonio = ['Septiembre','Octubre','Noviembre']
    invierno = ['Diciembre','Enero','Febrero']
    
    if mes in primavera:
        return 'Primavera'
    elif mes in verano:
        return 'Verano'
    elif mes in otonio:
        return 'Otoño'
    elif mes in invierno:
        return 'Invierno' 
    else:
        return 'Mes no valido'

print(f'La estacion es {check_season("Abril")}')
```
##### Print Output:
    La estacion es Primavera
---

### 6. Escriba una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal

```python
def calcular_pendiente(x1, y1, x2, y2):

    # Verifica si los puntos tienen la misma coordenada x para evitar división por cero
    if x1 == x2:
        return "La pendiente es indefinida (línea vertical)"

    # Calcula la pendiente
    pendiente = (y2 - y1) / (x2 - x1)
    return round(pendiente,2)

# Ejemplo de uso
x1, y1 = 2, 3
x2, y2 = 3, 8

pendiente = calcular_pendiente(x1, y1, x2, y2)
print(f"La pendiente de la línea que pasa por los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {pendiente}")
```
##### Print Output:
    La pendiente de la línea que pasa por los puntos (2, 3) y (3, 8) es: 5.0

### 7. Declara una función llamada print_list. Esta toma una lista como parámetro e imprime cada elemento de la lista.

```python
def print_list(lista):
    for i in lista:
        print(i)

lista = ["dedo","mano","oreja"]
print_list(lista)
```
##### Print Output:
    dedo
    mano
    oreja

### 8. Declara una función llamada reverse_list. Toma una matriz como parámetro y devuelve el inverso de la matriz (usa bucles).

```python
def reverse_list(matriz):
    # Crear una lista vacía para almacenar los elementos en orden inverso
    lista_invertida = []

    # Recorremos la lista desde el último elemento hasta el primero
    for i in range(len(matriz) - 1, -1, -1):
        # Añadimos cada elemento a la lista invertida
        lista_invertida.append(matriz[i])
    
    # Devolvemos la lista invertida
    return lista_invertida

### Ejemplo de uso
lista_original = [[1,2,4],[3,4,5],23,"carta","mangos"]
lista_invertida = reverse_list(lista_original)

print("Lista original:", lista_original)
print("Lista invertida:", lista_invertida)
```
##### Print Output:
    Lista original: [[1, 2, 4], [3, 4, 5], 23, 'carta', 'mangos']
    Lista invertida: ['mangos', 'carta', 23, [3, 4, 5], [1, 2, 4]]

## Ejercicios: Nivel 2

### 9. Declara una función denominada evens_and_odds . Toma un entero positivo como parámetro y cuenta la cantidad de pares e impares en el número.

```python
def evens_and_odds(numeros):    
    # Inicializamos las variables pares e impares para sumar la cantidad de numeros de cada uno
    pares = 0
    impares = 0
    
    # Recorremos el arreglo evaluando la condicion de si es par o impar
    for i in range(numeros + 1):
        if i % 2 == 0: # Si la condicion es True, cuenta un numero par
            pares += 1 
        elif i % 2 != 0: # Si la condicion es True, cuenta un numero impar
            impares += 1
    
    # Mostramos en pantalla
    print(f'La cantidad de numeros pares es {pares}')
    print(f'La cantidad de numeros impares es {impares}')
    
evens_and_odds(100)
```
##### Print Output:
    La cantidad de numeros pares es 51
    La cantidad de numeros impares es 50

### 10. Llama a tu función factorial, toma un número entero como parámetro y devuelve un factorial del número.

```python
def factorial(numero):
    # Inicializamos total a 1 porque el factorial se calcula con multiplicaciones
    total = 1
    # Recorremos todos los números de 1 a 'numero' (inclusive)
    for num in range(1, numero + 1):
        total *= num  # Multiplicamos 'total' por cada número en el rango
    return total  # Devolvemos el resultado final

# Ejemplo de uso
print(factorial(5))
```
##### Print Output:
    120

### 11. Llama a tu función is_empty , toma un parámetro y verifica si está vacío o no

```python
def is_empty(parametro):
    # Verifica si el parámetro está vacío
    if not parametro:
        return True
    else:
        return False

# Ejemplos de uso
print(is_empty([]))       # True, porque la lista está vacía
print(is_empty([1, 2, 3])) # False, porque la lista no está vacía
print(is_empty(""))       # True, porque la cadena está vacía
print(is_empty("texto"))  # False, porque la cadena no está vacía
print(is_empty({}))       # True, porque el diccionario está vacío
print(is_empty({"key": "value"})) # False, porque el diccionario no está vacío
```
### Print Output:
    True
    False
    True
    False
    True
    False