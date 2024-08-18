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

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2

# Definir los coeficientes
m = 2 # Pendiente
b = -2 # Intercepcion en y

