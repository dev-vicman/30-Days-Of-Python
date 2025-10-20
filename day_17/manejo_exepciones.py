'''
1. Conversión de Entrada Insegura (ValueError)
Escribe un programa que solicite al usuario ingresar un número entero. Utiliza un bloque try y except para capturar la excepción ValueError si el usuario ingresa texto o un número decimal. Si la conversión es exitosa, imprime el número; de lo contrario, imprime un mensaje de error amigable.

'''

try:
    resultado = 10/0
    print("El Resultado es: ", resultado)
except:
    print("No se puede dividir entre 0")
    resultado = 0