""" Day 3: 30 Days of python programming """

# %%
# Concatena la cadena 'Treinta', 'Días', 'De', 'Python' en una sola cadena, 'Treinta días de Python'.

cadena = ['Treinta', 'Días', 'De', 'Python']
cadena_concatenada = ' '.join(cadena)
print(cadena_concatenada) # Treinta Días De Python

# %%
# 2. Concatenar la cadena 'Codificación', 'Para', 'Todos' en una sola cadena, 'Codificación para todos'.

cadena = ['Codificación', 'Para', 'Todos']
cadena_concatenada = ' '.join(cadena)
print(cadena_concatenada) # Codificación Para Todos

# %%
# 3. Declare una variable llamada empresa y asígnele un valor inicial "Codificación para todos".

empresa = "Codificación Para Todos"

# 4. Imprima la variable empresa utilizando print()
print(empresa) # Codificación Para Todos

# 5. Imprima la longitud de la cadena de la empresa utilizando el método len() y print().

print(len(empresa)) # 23

# 6. Cambie todos los caracteres a letras mayúsculas utilizando el método upper().

print(empresa.upper()) # CODIFICACIÓN PARA TODOS

# 7. Cambie todos los caracteres a letras minúsculas utilizando el método lower().

print(empresa.lower()) # codificación para todos

# 8. Utilice los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena "Codificación para todos".

print(empresa.capitalize()) # Codificación para todos
print(empresa.title()) # Codificación Para Todos
print(empresa.swapcase()) # cODIFICACIÓN pARA tODOS

# %%
# 9. Recortar (cortar) la primera palabra de la cadena Codificación para todos.

recortar = empresa.split()
print(recortar[0]) # Codificación


# %%
# 10. Compruebe si la cadena Codificación Para Todos contiene una palabra Codificación utilizando el método index, find u otros métodos.

print(empresa.count("Codificación")) # 1 -> el metodo count encontro una coincidencia en la cadena
print(empresa.index("Codificación")) # 0 -> el metodo index devolvio el indice mas bajo de la coincidencia en la cadena
print(empresa.find("Codificación")) # 0 -> El metodo find encontro la coincidencia en la posicion [0]

# %%
# 11. Reemplace la palabra codificación en la cadena 'Codificación para todos' por Python.

print(empresa.replace("Codificación", "Python")) # Codificación Para Todos
# %%
# 12. Divida la cadena 'Coding For All' usando el espacio como separador (split()).

print(empresa.split(" ")) # ['Codificación', 'Para', 'Todos']

# %%
# 13. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" divide la cadena en la coma.

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", ")) #['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# %%
# 14. ¿Cuál es el carácter en el índice 0 en la cadena Codificación para todos ?

print(empresa[0]) # C

# 15. ¿Cuál es el último índice de la cadena Codificación Para Todos .

print(empresa[-1]) # s

# 16. ¿Qué carácter está en el índice 10 en la cadena "Codificación para todos"?

print(empresa[10]) # ó
# %%
# 17. Crea un acrónimo o una abreviatura para el nombre 'Python para todos'

#Cadena original
frase = "Python para todos"

# Separamos la cadena en una lista
palabras = frase.split(" ")

# Creamos una cadena de texto, usando el metodo `.format` concatenamos las primeras letras de cada elemento de la lista haciendo una eleccion de caracteres. Usando el metodo `.upper` cambiamos a mayuscula y finalizamos con la creacion del acrononimo.
acronimo = '{}{}{}'.format(palabras[0][:1],palabras[1][:1],palabras[2][:1]).upper()

# Mostramos en pantalla
print(acronimo)
# %%
# 18. Crea un acrónimo o una abreviatura para el nombre 'Coding For All'.

#Cadena original
frase = "Coding for all"

# Separamos la cadena en una lista
palabras = frase.split(" ")

# Creamos una cadena de texto, usando el metodo `.format` concatenamos las primeras letras de cada elemento de la lista haciendo una eleccion de caracteres. Usando el metodo `.upper` cambiamos a mayuscula y finalizamos con la creacion del acrononimo.
acronimo = '{}{}{}'.format(palabras[0][:1],palabras[1][:1],palabras[2][:1]).upper()

# Mostramos en pantalla
print(acronimo)
# %%
