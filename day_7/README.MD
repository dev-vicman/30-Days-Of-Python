# 💻 Exercises - Day 7

### sets

```python
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```
## *** Ejercicios: Nivel 1 *** 

#### 1. Encuentra la longitud del conjunto it_companies
```python
print(f" La longitud del conjunto it_companies es: {len(it_companies)}")
```

### 2. Añade 'Twitter' a it_companies
```python
it_companies.add("Twitter")
print(it_companies)
```

### 3. Insertar varias empresas de TI a la vez en el conjunto it_companies

```python
it_companies.update(["CGI","NVIDIA","Uber"])
print(it_companies) # {'Microsoft', 'Oracle', 'Google', 'Amazon', 'IBM', 'Facebook', 'CGI', 'NVIDIA', 'Twitter', 'Uber', 'Apple'}
```

# 4. Eliminar una de las empresas del conjunto it_companies
it_companies.remove("IBM")
print(it_companies) # {'Facebook', 'Oracle', 'Google', 'Twitter', 'Amazon', 'Microsoft', 'Apple', 'CGI', 'NVIDIA', 'Uber'}

# 5. ¿Cuál es la diferencia entre eliminar y descartar?
''' Si intentas eliminar un elemento que no existe en el conjuto con el metodo `remove`, se genera un error. El metodo `discard` no genera error si el elemento no existe en el conjunto ''' 

""" *** Ejercicios: Nivel 2 *** """

# 6. Unir A y B
print(A) # {19, 20, 22, 24, 25, 26}
print(B) # {19, 20, 22, 24, 25, 26, 27, 28}
union_A_B = A.union(B)
print(union_A_B) # {19, 20, 22, 24, 25, 26, 27, 28}

# 7. Encuentra la intersección A y B

print(A) # {19, 20, 22, 24, 25, 26}
print(B) # {19, 20, 22, 24, 25, 26, 27, 28}
intercepcion_A_B = A.intersection(B) 
print(intercepcion_A_B) # {19, 20, 22, 24, 25, 26}

# 8. A Es un subconjunto de B

print(A.issubset(B)) # True

# 5. ¿Son A y B conjuntos disjuntos?
print(A.isdisjoint(B)) # False

# 6. Unir A con B y B con A
union_A_con_B = A.union(B)
union_B_con_A = B.union(A)

print(f"La union de A con B es: {union_A_con_B}") # {19, 20, 22, 24, 25, 26, 27, 28}
print(f"La union de B con A es: {union_B_con_A}") # {19, 20, 22, 24, 25, 26, 27, 28}

# 7. ¿Cuál es la diferencia simétrica entre A y B?
diferencia_simetrica = A.symmetric_difference(B)
print(F"La diferencia simetrica de A con B es: {diferencia_simetrica}")

# 8. Eliminar los conjuntos por completo
del A
del B

""" *** Ejercicios: Nivel 3 *** """
# 9. Convierte las edades en un conjunto y compara la longitud de la lista y el conjunto, ¿cuál es más grande?
age_set = set(age)

if len(age) > len(age_set):
    print(f"La lista age tiene mas elementos")
elif len(age) < len(age_set):
    print(f"El Conjunto age_set tiene mas elementos")
else:
    print(f"La lista age y el conjunto age_set tienen la misma cantidad de elementos")

# 10. Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto.
"""
Cadena (String): Secuencia de caracteres (texto). Inmutable (no se puede cambiar después de su creación), ordenada, y indexable (se accede a sus caracteres por índice).

Lista: Colección de elementos, que pueden ser de diferentes tipos. Mutable (se puede modificar después de su creación), ordenada, indexable, y permite duplicados.

Tupla: Colección de elementos. Inmutable (no se puede modificar después de su creación), ordenada, indexable, y permite duplicados.

Conjunto (Set): Colección de elementos únicos. Mutable (se pueden añadir o eliminar elementos), desordenado, no indexable (no se accede por índice), y no permite duplicados.
"""

# 11. Soy profesor y me encanta inspirar y enseñar a la gente. ¿Cuántas palabras únicas se han utilizado en la oración? Utilice los métodos de división y de configuración para obtener las palabras únicas."""

# Definimos una variable con la cadena de texto proporcionada
oracion = "Soy profesor y me encanta inspirar y enseñar a la gente."

# Dividimos la oracion en palabras
palabras = oracion.split(" ") # ['Soy', 'profesor', 'y', 'me', 'encanta', 'inspirar', 'y', 'enseñar', 'a', 'la', 'gente.']
print(palabras)

# Convertimos la lista palabras en un conjunto para eliminar los duplicados
palabras_set = set(palabras) # {'profesor', 'la', 'y', 'Soy', 'enseñar', 'encanta', 'inspirar', 'me', 'a', 'gente.'}
print(f"La cantidad de palabras unicas es: {len(palabras_set)} palabras")
