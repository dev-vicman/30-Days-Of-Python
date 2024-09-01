""" Day 9: 30 Days of python programming """

""" Exercises: Level 1 """ 

# 1. Obtenga la entrada del usuario mediante input(“Ingrese su edad: ”). Si el usuario tiene 18 años o más, proporcione comentarios: Tiene la edad suficiente para conducir. Si es menor de 18 años, proporcione comentarios para esperar la cantidad de años faltantes. Salida:

print("\nComprobar si puedes conducir")
print("------------------------------\n")
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Tienes edad suficiente para conducir")
else:
    print(f"Necesitas cumplir {18 - edad} años mas para poder conducir")
print("------------------------------")

# 2. Compara los valores de my_age y your_age usando if … else. ¿Quién es mayor (tú o yo)? Usa input(“Ingresa tu edad: ”) para obtener la edad como entrada. Puedes usar una condición anidada para imprimir 'year' para una diferencia de edad de 1 año, 'years' para diferencias mayores y un texto personalizado si my_age = your_age.

mi_edad = 41
tu_edad = int(input("Ingresa tu edad: "))

if mi_edad > tu_edad:
    print(f"Eres menor que yo por {mi_edad - tu_edad} años" )
elif mi_edad < tu_edad:
    print(f"Eres mayor que yo por {tu_edad - mi_edad} anios")
else:
    print("Tenemos la misma edad")

# Obtener dos números del usuario mediante el mensaje de entrada. Si a es mayor que b, devolver a es mayor que b; si a es menor que b, devolver a es menor que b; de lo contrario, a es igual a b.


a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))

if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else:
    print("a y b son iguales")


""" ### Exercises: Level 2 """
# 3. Escriba un código que califique a los estudiantes según sus puntuaciones:
# 90-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

calificacion_estudiante = int(input("Ingrese la calificacion del estudiante: "))

if calificacion_estudiante >= 90 and calificacion_estudiante <= 100:
    print("El estudiante recibio una `A`")
elif calificacion_estudiante >= 70 and calificacion_estudiante <= 89:
    print("El estudiante recibio una `B`")
elif calificacion_estudiante >= 60 and calificacion_estudiante <= 69:
    print("El estudiante recibio una `C`")
elif calificacion_estudiante >= 50 and calificacion_estudiante <= 59:
    print("El estudiante recibio una `D`")
elif calificacion_estudiante >= 0 and calificacion_estudiante <= 49:
    print("El estudiante recibio una `F`")
else:
    print("La calificacion introducida es invalida")

# 4. Comprueba si la estación es Otoño, Invierno, Primavera o Verano. Si la entrada del usuario es: Septiembre, Octubre o Noviembre, la estación es Otoño. Diciembre, Enero o Febrero, la estación es Invierno. Marzo, Abril o Mayo, la estación es Primavera. Junio, Julio o Agosto, la estación es Verano.

# La siguiente lista contiene algunas frutas:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# Si una fruta no existe en la lista, agréguela a la lista e imprima la lista modificada. Si la fruta existe, imprima ('Esa fruta ya existe en la lista')

""" Ejercicios: Nivel 3 """
# Aquí tenemos un diccionario de personas. ¡Siéntete libre de modificarlo!

person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
    'street': 'Space street',
    'zipcode': '02210'
}
}

# * Verifica si el diccionario de la persona tiene la clave "habilidades"; si es así, imprime la habilidad del medio en la lista de habilidades.

if "skills" in person:
    # Obteniendo las skills del diccionario
    skill = person["skills"]
    # Calculando el indice medio de skill
    indice_medio = len(skill) // 2
    # Mostramos en pantalla la skill de en medio.
    print(f"La habilidad de en medio es {skill[indice_medio]}")

# * Verifica si el diccionario de la persona tiene la clave "habilidades"; si es así, verifica si la persona tiene la habilidad 'Python' e imprime el resultado.

if "skills" in person:
    if "Python" in person["skills"]:
        print("si esta Python")
    else:
        print("Python no esta en skills")

# * Si las habilidades de una persona solo incluyen JavaScript y React, imprime('Es un desarrollador frontend'); si las habilidades de la persona incluyen Node, Python, MongoDB, imprime('Es un desarrollador backend'); si las habilidades de la persona incluyen React, Node y MongoDB, imprime('Es un desarrollador fullstack'); de lo contrario, imprime('título desconocido') - para resultados más precisos, ¡se pueden anidar más condiciones!

if 'skills' in person:
    habilidades = person['skills']
    
    if set(habilidades) == {'JavaScript', 'React'}:
        print('Es un desarrollador frontend')
    elif {'Node', 'Python', 'MongoDB'}.issubset(habilidades):
        print('Es un desarrollador backend')
    elif {'React', 'Node', 'MongoDB'}.issubset(habilidades):
        print('Es un desarrollador fullstack')
    else:
        print('título desconocido')
else:
    print('No se encontraron habilidades en el diccionario.')


# * Si la persona está casada y vive en Finlandia, imprime la información en el siguiente formato: "Asabeneh Yetayeh vive en Finlandia. El esta casado"

if person['is_marred'] == True and person['country'] == "Finland":
    print("Asabeneh Yetayeh vive en Finlandia. El esta casado")
elif person['is_marred'] == True and person['country'] != "Finland":
    print("Asabeneh Yetayeh esta casado pero no vive en Finlandia")
elif person['is_marred'] != True and person['country'] == "Finland":
    print("Asabeneh Yetayeh vive en Finlandia. El no esta casado")
else:
    print("Asabeneh Yetayeh no vive en Finlandia. El no esta casado")