""" Day 9: 30 Days of python programming """

""" Exercises: Level 1 """ 

# 1. Obtenga la entrada del usuario mediante input(“Ingrese su edad: ”). Si el usuario tiene 18 años o más, proporcione comentarios: Tiene la edad suficiente para conducir. Si es menor de 18 años, proporcione comentarios para esperar la cantidad de años faltantes. Salida:
""" Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive. """

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Tienes edad suficiente para conducir")
else:
    print(f"Necesitas cumplir {18 - edad} años mas para poder conducir")

# 2. Compara los valores de my_age y your_age usando if … else. ¿Quién es mayor (tú o yo)? Usa input(“Ingresa tu edad: ”) para obtener la edad como entrada. Puedes usar una condición anidada para imprimir 'year' para una diferencia de edad de 1 año, 'years' para diferencias mayores y un texto personalizado si my_age = your_age. Salida:

mi_edad = 41
tu_edad = int(input("Ingresa tu edad: "))

if mi_edad > tu_edad:
    print(f"Eres menor que yo por {mi_edad - tu_edad} años" )
elif mi_edad < tu_edad:
    print(f"Eres mayor que yo por {tu_edad - mi_edad} anios")
else:
    print("Tenemos la misma edad")

""" ### Exercises: Level 2 """
# 3. Escriba un código que califique a los estudiantes según sus puntuaciones:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

# 4. Comprueba si la estación es Otoño, Invierno, Primavera o Verano. Si la entrada del usuario es: Septiembre, Octubre o Noviembre, la estación es Otoño. Diciembre, Enero o Febrero, la estación es Invierno. Marzo, Abril o Mayo, la estación es Primavera. Junio, Julio o Agosto, la estación es Verano.

# La siguiente lista contiene algunas frutas:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# Si una fruta no existe en la lista, agréguela a la lista e imprima la lista modificada. Si la fruta existe, imprima ('Esa fruta ya existe en la lista')

""" Ejercicios: Nivel 3 """
# Aquí tenemos un diccionario de personas. ¡Siéntete libre de modificarlo!

#    person={
#    'first_name': 'Asabeneh',
#    'last_name': 'Yetayeh',
#    'age': 250,
#    'country': 'Finland',
#    'is_marred': True,
#    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#    'address': {
#        'street': 'Space street',
#        'zipcode': '02210'
#    }
#    }
# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
# * If the person is married and if he lives in Finland, print the information in the following format:
#    Asabeneh Yetayeh lives in Finland. He is married.