# 💻 Exercises - Day 8

### 1. Crea un diccionario vacío llamado perro
```python
perro = {}
```

### 2. Añade nombre, color, raza, patas y edad al diccionario de perros

```python
perro["nombre"] = "Fido"
perro["color"] = "Marron"
perro["raza"] = "Mestizo"
perro["patas"] = "Cortas"
perro["edad"] = 3
```

### 3. Cree un diccionario de estudiantes y agregue nombre, apellido, género, edad, estado civil, habilidades, país, ciudad y dirección como claves para el diccionario.

```python
estudiantes = {
    "Nombre": "Victor",
    "Apellido": "Hernandez",
    "Genero": "Masculino",
    "Edad": 41,
    "Estado Civil": "Soltero",
    "Habilidades": ["Puntualidad","Trabajo en esquipo"],
    "Pais": "EEUU",
    "Ciudad": "Denver",
    "Direccion": "4295 E Mexico Ave"
}
```

### 4. Obtenga la longitud del diccionario del estudiante

```python
print(len(estudiantes))
```

### 5. Obtenga el valor de las habilidades y verifique el tipo de datos, debe ser una lista

```python
print(estudiantes["Habilidades"], type(estudiantes["Habilidades"]))
```

### 6. Modifique los valores de las habilidades agregando una o dos habilidades

```python
estudiantes["Habilidades"].extend(["Organizacion","Responsabilidad"])
```

### 7. Obtenga las claves del diccionario como una lista

```python
claves_estudiantes = list(estudiantes.keys())
print(claves_estudiantes, type(claves_estudiantes))
```

### 8. Obtener los valores del diccionario como una lista

```python
valores_estudiantes  = list(estudiantes.values())
print(valores_estudiantes, type(valores_estudiantes))
```

### 9. Cambie el diccionario a una lista de tuplas usando el método items()

```python
items_estudiantes = estudiantes.items()
print(items_estudiantes)
```

### 10. Eliminar uno de los elementos del diccionario

```python
estudiantes.pop("Edad")
print(estudiantes)
```

### 11. Eliminar uno de los diccionarios

```python
del perro
```