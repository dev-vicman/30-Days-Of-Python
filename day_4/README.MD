# # 💻 Exercises - Day 4

### 1. Concatena la cadena 'Treinta', 'Días', 'De', 'Python' en una sola cadena, 'Treinta días de Python'.

```python
cadena = ['Treinta', 'Días', 'De', 'Python']
cadena_concatenada = ' '.join(cadena)
print(cadena_concatenada) # Treinta Días De Python
```

### 2. Concatenar la cadena 'Codificación', 'Para', 'Todos' en una sola cadena, 'Codificación para todos'.

```python
cadena = ['Codificación', 'Para', 'Todos']
cadena_concatenada = ' '.join(cadena)
print(cadena_concatenada) # Codificación Para Todos
```

### 3. Declare una variable llamada empresa y asígnele un valor inicial "Codificación para todos".

```python
empresa = "Codificación Para Todos"
```

### 4. Imprima la variable empresa utilizando print()

```python
print(empresa) # Codificación Para Todos
```

### 5. Imprima la longitud de la cadena de la empresa utilizando el método len() y print().

```python
print(len(empresa)) # 23
```

### 6. Cambie todos los caracteres a letras mayúsculas utilizando el método upper().

```python
print(empresa.upper()) # CODIFICACIÓN PARA TODOS
```

### 7. Cambie todos los caracteres a letras minúsculas utilizando el método lower().

```python
print(empresa.lower()) # codificación para todos
```

### 8. Utilice los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena "Codificación para todos".

```python
print(empresa.capitalize()) # Codificación para todos
print(empresa.title()) # Codificación Para Todos
print(empresa.swapcase()) # cODIFICACIÓN pARA tODOS
```

### 9. Recortar (cortar) la primera palabra de la cadena Codificación para todos.

```python
recortar = empresa.split()
print(recortar[0]) # Codificación
```

### 10. Compruebe si la cadena Codificación Para Todos contiene una palabra Codificación utilizando el método index, find u otros métodos.

```python
print(empresa.count("Codificación")) # 1 -> el metodo count encontro una coincidencia en la cadena
print(empresa.index("Codificación")) # 0 -> el metodo index devolvio el indice mas bajo de la coincidencia en la cadena
print(empresa.find("Codificación")) # 0 -> El metodo find encontro la coincidencia en la posicion [0]
```

### 11. Reemplace la palabra codificación en la cadena 'Codificación para todos' por Python.

```python
print(empresa.replace("Codificación", "Python")) # Codificación Para Todos
```
### 12. Divida la cadena 'Coding For All' usando el espacio como separador (split()).

```python
print(empresa.split(" ")) # ['Codificación', 'Para', 'Todos']
```
### 13. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" divide la cadena en la coma.

```python
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", ")) #['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
```

### 14. ¿Cuál es el carácter en el índice 0 en la cadena Codificación para todos ?

```python
print(empresa[0]) # C
```

### 15. ¿Cuál es el último índice de la cadena Codificación Para Todos .

```python
print(empresa[-1]) # s
```

### 16. ¿Qué carácter está en el índice 10 en la cadena "Codificación para todos"?

```python
print(empresa[10]) # ó
```

### 17. Crea un acrónimo o una abreviatura para el nombre 'Python para todos'

```python
#Cadena original
frase = "Python para todos"

# Separamos la cadena en una lista
palabras = frase.split(" ")

# Creamos una cadena de texto, usando el metodo `.format` concatenamos las primeras letras de cada elemento de la lista haciendo una eleccion de caracteres. Usando el metodo `.upper` cambiamos a mayuscula y finalizamos con la creacion del acrononimo.
acronimo = '{}{}{}'.format(palabras[0][:1],palabras[1][:1],palabras[2][:1]).upper()

# Mostramos en pantalla
print(acronimo) # PPT
```

### 18. Crea un acrónimo o una abreviatura para el nombre 'Coding For All'.

```python
# Cadena original
frase = "Coding for all"

# Separamos la cadena en una lista
palabras = frase.split(" ")

# Creamos una cadena de texto, usando el metodo `.format` concatenamos las primeras letras de cada elemento de la lista haciendo una eleccion de caracteres. Usando el metodo `.upper` cambiamos a mayuscula y finalizamos con la creacion del acrononimo.
acronimo = '{}{}{}'.format(palabras[0][:1],palabras[1][:1],palabras[2][:1]).upper()

# Mostramos en pantalla
print(acronimo) # CFA
```
### 19. Utilice el índice para determinar la posición de la primera aparición de C en Codificación para todos.

```python
frase = "Codificación para todos"
print(frase.find("C")) # 0
```

### 20. Utilice el índice para determinar la posición de la primera aparición de F en Codificación para todos.

```python
print(frase.find("F")) # -1 -> No se encuentra la 'F' ya que el lenguaje distingue minusculas de mayusculas. Asi que haremos una modificacion para que pueda encontrar la "F o f"

print(frase.upper().find("F")) # 4 -> transformando toda la cadena a mayusculas es posible encontrar la "F"
```
### 20. Utilice rfind para determinar la posición de la última aparición de l en Coding For All People.

```python
frase = "Coding For All People"
print(frase.lower().rfind("l")) # 19 -> como en el ejercio anterior llevamos todos los caracteres a minuscula para encontrar la letra deseada sin distincion entre caracter mayuscula o miniscula.
```

### 21. Utilice index o find para encontrar la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'

```python
frase = "No puedes terminar una oración con porque porque porque es una conjunción"

print(frase.find("porque")) # 35
```
### 22. Elimina la frase 'porque porque porque' de la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'

```python
print(frase.replace("porque porque porque ","")) # No puedes terminar una oración con es una conjunción
```

### 23. ¿''Coding For All' comienza con una subcadena Coding ?

```python
frase = "Coding For All"
print(frase.startswith("Coding")) # True
```
### 24. ¿'Coding For All' termina con una subcadena ' coding' ?

```python
print(frase.endswith("Coding")) # False
```

#### 25. 'Codificación para todos', elimina los espacios finales izquierdo y derecho en la cadena dada.

```python
frase = " Codificación para todos "
print(frase.strip(" ")) # Codificación para todos
```
### 26. ¿Cuál de las siguientes variables devuelve Verdadero cuando usamos el método isidentifier()? 30 días de Python, Treinta días de Python

```python
variable = "30díasdePython"
print(variable.isidentifier()) # False

variable = "treintadíasdePython"
print(variable.isidentifier()) # True
```

### 27. La siguiente lista contiene los nombres de algunas bibliotecas de Python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Únase a la lista con un hash con una cadena de espacios.

```python
lista = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(lista)) # Django Flask Bottle Pyramid Falcon
```