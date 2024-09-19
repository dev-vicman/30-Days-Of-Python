# 💻 Ejercicios: Día 14

## Ejercicios de Nivel 1
### 1. Explique la diferencia entre mapa, filtro y reducción.

* **map():** La función map() toma una función y un iterable como parámetros, y devuelve un nuevo iterable donde cada elemento es el resultado de aplicar la función a cada elemento del iterable original. En esencia, map() te permite aplicar una transformación a cada elemento de una lista.

* **filter():** La función filter() toma una función y un iterable, y devuelve un nuevo iterable que contiene solo los elementos del iterable original para los cuales la función devuelve True. En otras palabras, filter() te permite seleccionar elementos de una lista basados en una condición.

* **reduce():** La función reduce() toma una función y un iterable, y devuelve un único valor. La función que se pasa a reduce() debe tomar dos argumentos y devolver un único valor. reduce() aplica la función a los elementos del iterable de dos en dos, acumulando el resultado hasta que se procesan todos los elementos y se obtiene un único valor.
'''

### 2. Explique la diferencia entre función de orden superior, cierre y decorador.

* Función de Orden Superior:
Una función de orden superior es una función que puede tomar una o más funciones como argumentos o devolver una función como resultado.
Permiten un manejo flexible de funciones, fomentando la reutilización de código y la creación de abstracciones más potentes.

* Cierre:
Un cierre ocurre cuando una función anidada accede a una variable de su función externa (función envolvente) incluso después de que la función externa ha finalizado su ejecución.
La función interna "recuerda" el valor de la variable en el entorno de la función externa.

* **Decorador:**
Un decorador es una función de orden superior que modifica el comportamiento de otra función sin cambiar su código directamente.
Toma una función como argumento, la envuelve con funcionalidad adicional y retorna la función modificada.
Se utiliza la sintaxis "@" para aplicar un decorador a una función.

### 4. Utilice el bucle for para imprimir cada país en la lista de países.

```python
print("\nLa lista de paises contiene:")
for pais in countries:
    print(pais)
```

### 5. Utilice for para imprimir cada nombre en la lista de nombres.
```python
print("\nLa lista de nombres contiene:")
for nombre in names:
    print(nombre)
```
### 6. Utilice for para imprimir cada número en la lista de números.
```python
print("\nLa lista de numeros contiene:")
for numero in numbers:
    print(numero)
```

## Ejercicios de Nivel 2

### 7. Utilice el mapa para crear una nueva lista cambiando cada país a mayúscula en la lista de países
```python
pais_mayuscula = list(map(lambda countries: countries.upper(), countries))
print(pais_mayuscula)
```

### 8. Utilice el mapa para crear una nueva lista cambiando cada número por su cuadrado en la lista de números.
```python
numero_cuadrado = list(map(lambda numbers: numbers ** 2, numbers))
```

### 9. Utilice el mapa para cambiar cada nombre a mayúsculas en la lista de nombres

```python
nombre_mayuscula = list(map(lambda names: names.upper(), names))
```

### 10. Utilice el filtro para filtrar los países que contienen la palabra "land".
```python
filtro_tierra = list(filter(lambda countries: 'land'.lower() in countries.lower(), countries))
```

### 11. Utilice el filtro para filtrar los países que tengan exactamente seis caracteres.

```python
paises_seis_caracteres = list(filter(lambda countries: len(countries) == 6, countries))
```

### 12. Utilice el filtro para filtrar los países que contengan seis letras o más en la lista de países.

```python
paises_seis_o_mas_letras = list(filter(lambda countries: len(countries) >= 6, countries))
```

### 13. Utilice el filtro para filtrar los países que comienzan con 'E'

```python
paises_primer_letra_e = list(filter(lambda countries: countries.startswith('E'), countries))
```

### 14. Declare una función get_last_ten_countries que devuelva los últimos diez países de la lista de países.

```python
def get_last_ten_countries(lista):
    '''Devuelve los ultimos 10 elementos de una lista'''
    ultimos_diez = lista[-10:]
    return ultimos_diez

print('\nEstos son los últimos 10 países:\n' get_last_ten_countries(countries))
```
### 15. Utilice reducir para sumar todos los números en la lista de números.

```python
sumar_todos_los_numeros = reduce(lambda x, y: x + y, numbers)
```

### 16. Utilice reduce para concatenar todos los países y producir esta oración: Estonia, Finlandia, Suecia, Dinamarca, Noruega e Islandia son países del norte de Europa.
```python
concatenar_paises = reduce(lambda pais_1, pais_2: pais_1 + ', ' + pais_2, countries[0:-2]) + " e" + " " + countries[-1] + " son países del norte de Europa."

print('\n',concatenar_paises)
```