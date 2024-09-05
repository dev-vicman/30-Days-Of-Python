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



""" 5. Escriba una función list_of_rgb_colors que devuelva cualquier número de colores RGB en una matriz. """

""" 6. Escriba una función generate_colors que pueda generar cualquier cantidad de colores hexadecimales o rgb.
    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
    generate_colors('hexa', 1) # ['#b334ef']
    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
    generate_colors('rgb', 1)  # ['rgb(33,79, 176)'] """

#? Ejercicios: Nivel 3

""" 7. Llama a tu función shuffle_list, toma una lista como parámetro y devuelve una lista aleatoria """


""" 8. Escriba una función que devuelva una matriz de siete números aleatorios en un rango de 0 a 9. Todos los números deben ser únicos. """


