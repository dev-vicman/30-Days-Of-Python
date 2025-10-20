# 💻 Ejercicios: Día 17


### 1. Conversión de Entrada Insegura (ValueError)
     Escribe un programa que solicite al usuario ingresar un número entero. Utiliza un bloque try y except para capturar la excepción ValueError si el usuario ingresa texto o un número decimal. Si la conversión es exitosa, imprime el número; de lo contrario, imprime un mensaje de error amigable.

```python
try:
    numero_entero = int(input("Ingresa un numero entero: "))
    print("El numero que ingresaste es: ", numero_entero)
except ValueError:
    print("Debes ingresar un numero entero")
```


### 2. División con Control de Flujo (ZeroDivisionError y else)
     Crea una función llamada dividir_seguro(a, b) que tome dos argumentos.Implementa try para la división $a/b$.Captura específicamente el ZeroDivisionError. Si ocurre, retorna el mensaje: "Error: El divisor no puede ser cero."Si la división es exitosa (el bloque try no falló), usa el bloque else para retornar el resultado de la división.

```python

def dividir_seguro(a,b):
    try:
        resultado = a/b
        print("El resultado es: ", resultado)
    except ZeroDivisionError:
        print("El divisor no puede ser 0")

dividir_seguro(10,2)

```

### 3. Acceso a Diccionario (KeyError)
     Define un diccionario de productos y precios: precios = {"manzana": 1.5, "banana": 0.5, "naranja": 1.0}. Pide al usuario el nombre de un producto.

     Usa try para buscar e imprimir el precio del producto usando precios[producto].

     Captura el KeyError si el producto no está en el diccionario y retorna: "Producto no encontrado. Verifique el nombre."

```python
precios = {"manzana": 1.5, "banana": 0.5, "naranja": 1.0}

try:
    buscar_producto = input("Ingrese el nombre del producto: ")
    print(f"El precio de {buscar_producto} es de: {precios[buscar_producto]}")
except KeyError:
    print("Producto no encontrado. Verifique el nombre")
```