# # Day 3: 30 Days of python programming

# 1. Declare your age as integer variable

my_age = 41

# 2. Declare your height as a float variable

my_height = 1.71

# 3. Declare a variable that store a complex number

complex_number = 1 + 2j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

base = int(input(f"Ingresa la base del triangulo: "))
height = int(input(f"Ingresa la altura del triangulo: "))
area = 0.5 * base * height
print(f"El area del triangulo es: {area}")

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

side_a = int(input(f"Ingresa la medida del lado a: "))
side_b = int(input(f"Ingresa la medida del lado b: "))
side_c = int(input(f"Ingresa la medida del lado c: "))
perimeter = side_a + side_b + side_c
print(f"El perimetro del triangulo es: {perimeter}")

# 6. Find the length of 'python' and 'dragon' and make a falsy comparison statement.

print(len("python") != len("dragon"))

# 7. Use and operator to check if 'on' is found in both 'python' and 'dragon'

result = "on" in "python" and "on" in "dragon"
print(result)

# %%
# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2

# Definimos la pendiente (m) y el intercepto en y (b) de la ecuación y = mx + b
m = 2  # Pendiente de la ecuación, que es 2 en este caso
b = -2  # Intercepto en y, que es -2 en este caso

# Calcular el intercepto en y
y_intercept = (0, b)  # El intercepto en y ocurre cuando x = 0, así que es (0, -2)

# Calcular el intercepto en x
# Para encontrar el intercepto en x, establecemos y = 0 y resolvemos para x
# La ecuación era 0 = 2x - 2, entonces x = 1
x_intercept = (1, 0) if m != 0 else "No tiene intercepto en x"

# Mostrar resultados
print(f"Pendiente: {m}")  # Imprime la pendiente
print(f"Intercepto en y: {y_intercept}")  # Imprime el intercepto en y
print(f"Intercepto en x: {x_intercept}")  # Imprime el intercepto en x

# %%
# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

# Puntos dados
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calcular la pendiente
m = (y2 - y1) / (x2 - x1)

# Calcular la distancia euclidiana
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Mostrar los resultados
print(f"Pendiente: {m}")
print(f"Distancia Euclidiana: {d:.2f}")

# %%
# 10. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

sentece = "I hope this course is not full of jargon"
print("jargon" in sentece)

# %%
# 11. There is no 'on' in both dragon and python
result = "on" not in "python" and "on" in "dragon"
print(result)

# %%
# 12. Find the length of the text python and convert the value to float and convert it to string

convert = str(float(len("python")))
print(convert,type(convert))

# %%
# 13. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

numero = 5
numero_es_divisible = numero % 2 == 0
print(f"El numero es divisible entre 2: {numero_es_divisible}")

# %%
# 14. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7

floor_division = 7 // 3
int_converted = int(2.7)
print(floor_division == int_converted)
# %%
# 15. Check if type of '10' is equal to type of 10

print(type("10") == type(10))

# %%
# 16. Check if int('9.8') is equal to 10

print(int(9.8) == 10)
# %%
# 17. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

# Solicitar al usuario que ingrese la cantidad de horas trabajadas
horas = int(input("Introduce la cantidad de horas trabajadas: "))

# Solicitar al usuario que ingrese el valor de su hora de trabajo
valor_hora = int(input("Ingresa el valor de la hora: "))

# Calcular el total del pago al multiplicar el valor hora por las horas trabajadas
total_pago = horas * valor_hora

# Mostrar el resultado
print(f"Tu pago sera de {total_pago}")

# %%
# 18. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

# Solicitar al usuario que ingrese el número de años que ha vivido
años_vividos = int(input("Introduce el número de años que has vivido: "))

# Calcular el número de segundos que ha vivido
segundos_vividos = años_vividos * 365 * 24 * 60 * 60

# Mostrar el resultado
print(f"Has vivido durante {segundos_vividos} segundos.")
