""" Day 12: 30 Days of python programming """

# Importar modulos
import random
import string

# print(randint(1,100))

#? Ejercicios: Nivel 1

""" 1. Escriba una función que genere un random_user_id de seis dígitos/caracteres.
    #print(random_user_id());
    #'1ee33d' """

def random_user_id():
    # Generar una combinación de dígitos y letras minúsculas
    lista = string.digits + string.ascii_lowercase
    
    # Inicializar una lista para almacenar los caracteres seleccionados
    caracteres_seleccionados = []
    
    # Seleccionar seis caracteres aleatorios de la lista
    for _ in range(6):
        caracter_aleatorio = random.choice(lista)
        caracteres_seleccionados.append(caracter_aleatorio)
    
    # Unir los caracteres seleccionados en una sola cadena
    cadena = ''.join(caracteres_seleccionados)
    
    return cadena

print('Clave:', random_user_id())

""" 2. Escriba una función llamada rgb_color_gen. Generará colores RGB (tres valores que van de 0 a 255 cada uno).
#print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form """

print(random.randint(1,255))

def rgb_color_gen():
    return f"rgb({random.randint(1,255)},{random.randint(1,255)},{random.randint(1,255)})"

print(rgb_color_gen())


#? Ejercicios: Nivel 2

""" 3. Escriba una función list_of_hexa_colors que devuelva cualquier número de colores hexadecimales en una matriz (seis números hexadecimales escritos después de #. El sistema de numeración hexadecimal está formado por 16 símbolos, del 0 al 9 y las primeras 6 letras del alfabeto, af. Consulte la tarea 6 para ver ejemplos de salida). """

def generar_hexa_colores():
    hex_chars = '0123456789abcdef'
    color = '#' + ''.join(random.choice(hex_chars) for _ in range(6))
    return color

print(generar_hexa_colores())

def list_of_hexa_colors(num_colores):
    colores = []
    for _ in range(num_colores):
        color = generar_hexa_colores()
        colores.append(color)
    return colores

print(list_of_hexa_colors(4))

""" 5. Escriba una función list_of_rgb_colors que devuelva cualquier número de colores RGB en una matriz. """

def generate_rgb_color():
    return (random.randint(0, 255), 
            random.randint(0, 255), 
            random.randint(0, 255))

def list_of_rgb_colors(num_colores):
    colores = []
    for _ in range(num_colores):
        color = generate_rgb_color()
        colores.append(color)
    return colores

print(list_of_rgb_colors(4))


