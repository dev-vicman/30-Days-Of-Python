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

### 6. 