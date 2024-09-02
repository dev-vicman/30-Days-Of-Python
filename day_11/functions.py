
#* Ejercicios: Nivel 1
# 1. Declara una función add_two_numbers . Toma dos parámetros y devuelve una suma.

def add_two_numbers(numero_1, numero_2):
    """
    Calcula la Suma de 2 numeros
    
    Argumentos:
        
        numero_1 (int, Float): El primer numero a sumar    
        numero_2 (int, Float): El segundo numero a sumar
        
    Return:

        int, float  La suma de 2 numeros    
    """
    return numero_1 + numero_2

print(f'La suma de los numeros es: {add_two_numbers(4, 6)}') # La suma de los numeros es: 10

# 2. El área de un círculo se calcula de la siguiente manera: área = π x r x r. Escribe una función que calcule área_del_círculo.

def area_del_circulo(radio):
    """
    Calcula el area de un circulo
    
    Argumentos:
    
        radio (int, float): El radio de el circulo
        
    Return:

        int, float: El area de un circulo
    """
    area = 3.1416 * radio * radio
    return round(area,2)

print(f'El area del circulo es: {area_del_circulo(34)}') # El area del circulo es: 3631.69

# 3. Escriba una función llamada add_all_nums que tome una cantidad arbitraria de argumentos y sume todos los argumentos. Verifique si todos los elementos de la lista son de tipo numérico. Si no es así, proporcione una respuesta razonable.

def add_all_nums(*numeros):
    suma = 0
    for num in numeros:
        if isinstance(num, (int,float)):
            suma += num
        else:
            print(f"{num} no es un numero, no se incluira en la suma")
    return suma

resultado = add_all_nums(1, 2, 'a', 3.5)
print(f"La suma de los números es: {resultado}") # La suma de los números es: 6.5

# 4. La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. Escriba una función que convierta °C a °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(grados):
    farenheit = (grados * 1.8) + 32
    return farenheit

print(f'La temparatura es de {convert_celsius_to_fahrenheit(40)} farenheit') # La temparatura es de 104.0 farenheit

# 5. Escriba una función llamada check-season, toma un parámetro de mes y devuelve la temporada: Otoño, Invierno, Primavera o Verano.

def check_season(mes):
    
    # Definimos las estaciones segun sus meses
    primavera = ['Marzo','Abril','Mayo']
    verano = ['Junio','Julio','Agosto']
    otonio = ['Septiembre','Octubre','Noviembre']
    invierno = ['Diciembre','Enero','Febrero']
    
    # Evaluamos a que estacion pertenece el mes que se paso como argumento
    if mes in primavera:
        return 'Primavera'
    elif mes in verano:
        return 'Verano'
    elif mes in otonio:
        return 'Otoño'
    elif mes in invierno:
        return 'Invierno' 
    else:
        return 'Mes no valido'

# Mostramos por pantalla
print(f'La estacion es {check_season("Abril")}') # La estacion es Primavera


# 6. Escriba una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal

def calcular_pendiente(x1, y1, x2, y2):
    
    # Verifica si los puntos tienen la misma coordenada x para evitar división por cero
    if x1 == x2:
        return "La pendiente es indefinida (línea vertical)"
    
    # Calcula la pendiente
    pendiente = (y2 - y1) / (x2 - x1)
    return round(pendiente,2)

# Ejemplo de uso
x1, y1 = 2, 3
x2, y2 = 3, 8

pendiente = calcular_pendiente(x1, y1, x2, y2)
print(f"La pendiente de la línea que pasa por los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {pendiente}")


# 7. La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0. Escriba una función que calcule el conjunto de soluciones de una ecuación cuadrática, solve_quadratic_eqn .
# 8. Declara una función llamada print_list. Esta toma una lista como parámetro e imprime cada elemento de la lista.
# 9. Declara una función llamada reverse_list. Toma una matriz como parámetro y devuelve el inverso de la matriz (usa bucles).