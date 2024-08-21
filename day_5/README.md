# 💻 Exercises - Day 5

# Ejercicios nivel 1

### 1. Concatena la cadena 'Treinta', 'Días', 'De', 'Python' en una sola cadena, 'Treinta días de Python'.

```python
cadena = ['Treinta', 'Días', 'De', 'Python']
cadena_concatenada = ' '.join(cadena)
print(cadena_concatenada) # Treinta Días De Python
```

### 2. Declarar una lista con más de 5 elementos

```python
lista = ["Pera", "Mangos", "Tomates", "Manzana", "Durazno", "Fresas"]
```

### 3. Encuentra la longitud de tu lista

```python
print(len(lista)) # 6
```
### 4. Obtener el primer elemento, el elemento del medio y el último elemento de la lista.

```python
lista = ["Pera", "Mangos", "Tomates", "Manzana", "Durazno", "Fresas"]
primer_elemento = lista[0]
elemento_medio = lista[len(lista)//2]
ultimo_elemento = lista[-1]

print(primer_elemento)
print(elemento_medio)
print(ultimo_elemento)
```
### 5. Declara una lista llamada mixed_data_types, pon tu(nombre, edad, altura, estado civil, dirección)

```python
mixed_data_types = ["Victor", 41, 1.71, "Soltero", "4295 E Mexico Ave"]
```

### 6. Declare una variable de lista llamada it_companies y asigne los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.

```python
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
```

### 7. Imprima la lista usando print()

```python
print(it_companies) # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
```

### 8. Imprima el número de empresas en la lista

```python
print(len(it_companies)) # 7
```

### 9. Imprima la primera, la segunda y la última empresa.

```python
print(it_companies[0]) # Facebook
print(it_companies[1]) # Google
print(it_companies[-1]) # Amazon
```

### 10. Añadir una empresa de TI a it_companies

```python
it_companies.append("Twitter")
print(it_companies)
```

### 11. Insertar una empresa de TI en el medio de la lista de empresas

```python
it_companies.insert(len(it_companies)//2, "CompuMundoHiperMegaRed")
print(it_companies)
```
### 12. Cambie uno de los nombres de it_companies a mayúsculas (¡IBM excluido!)

```python
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

it_companies[2] = it_companies[2].upper()
print(it_companies[2]) # MICROSOFT
```

### 13. Unir it_companies con una cadena '#; '

```python
print("#; ".join(it_companies)) # Facebook#; Google#; MICROSOFT#; Apple#; IBM#; Oracle#; Amazon
```

### 14. Comprueba si una determinada empresa existe en la lista it_companies.

```python
existe_empresa = "Facebook" in it_companies
print(existe_empresa) # True

existe_empresa = "Twitter" in it_companies
print(existe_empresa) # False
```
### 15. Ordenar la lista usando el método sort()

```python
# Declaramos la lista
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Ordenamos la lista
it_companies.sort()

# Mostramos la lista
print(it_companies)
```
### 16. Invierta la lista en orden descendente utilizando el método reverse()

```python
it_companies.reverse()
print(it_companies)
```
### 17. Separa las primeras 3 empresas de la lista.

```python
# Declaramos la lista
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

tres_empresas = it_companies[0:3] 
print(tres_empresas) # ['Facebook', 'Google', 'Microsoft']
```
### 18. Elimina las últimas 3 empresas de la lista.

```python
# Declaramos la lista
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

del it_companies[-3:]
print(it_companies) # ['Facebook', 'Google', 'Microsoft', 'Apple']
```

## Exercises: Level 2

### 1. The following is a list of 10 students ages:

```python
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
```

#### 1.1 Sort the list and find the min and max age
```python
ages.sort()
min_age = ages[0]
max_age = ages[-1]

print(f"La edad minima es {min_age} y la edad maxima es {max_age}")
```
#### 1.2 Encuentra la edad media un elemento intermedio o dos elementos intermedios divididos por dos

```python
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ordenar la lista
ages.sort()

# Calcular la mediana
n = len(ages)
median_age = (ages[(n-1)//2] + ages[n//2]) / 2

print(f"La edad media (mediana) es {median_age}")
```
#### 1.3 Encuentra la edad promedio (suma de todos los elementos dividida por su número)

```python
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# sumar los elementos de la lista
sum_ages = sum(ages)

# Calculamos el promedio de las edades
average_ages = sum_ages/len(ages)

# Mostramos en pantalla el resultado
print(average_ages)
```
