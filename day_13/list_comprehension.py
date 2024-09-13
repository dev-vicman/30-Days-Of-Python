""" Day 13: 30 Days of python programming """
#? 1. Filtrar solo los negativos y ceros en la lista usando la comprensión de listas

numeros = [-4, -3, -2, -1, 0, 2, 4, 6]
numeros_menores_cero = [i for i in numeros if i <= 0]
print(numeros_menores_cero) # Salida: [-4, -3, -2, -1, 0]

#? 2. Aplanar la siguiente lista de listas de listas a una lista unidimensional:

lista_de_listas = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista_aplanada = [numero for sub_lista_1 in lista_de_listas for sub_lista_2 in sub_lista_1 for numero in sub_lista_2]

print(lista_aplanada) # Salida: [1, 2, 3, 4, 5, 6, 7, 8, 9]

#? 3. Usando la comprensión de listas, crea la siguiente lista de tuplas:

lista_tuplas = [(i, *[i**j for j in range(7)]) for i in range(11)]
print(lista_tuplas) #Salida: [(0, 1, 0, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1, 1, 1), (2, 1, 2, 4, 8, 16, 32, 64), (3, 1, 3, 9, 27, 81, 243, 729), (4, 1, 4, 16, 64, 256, 1024, 4096), (5, 1, 5, 25, 125, 625, 3125, 15625), (6, 1, 6, 36, 216, 1296, 7776, 46656), (7, 1, 7, 49, 343, 2401, 16807, 117649), (8, 1, 8, 64, 512, 4096, 32768, 262144), (9, 1, 9, 81, 729, 6561, 59049, 531441), (10, 1, 10, 100, 1000, 10000, 100000, 1000000)]

#? 4. Aplanar la siguiente lista para formar una nueva lista:
paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Función para obtener la abreviatura del país
def obtener_abreviatura(nombre):
    return nombre[:3].upper()

# Transformar la lista de tuplas
lista_transformada = [
    [pais.upper(), obtener_abreviatura(pais), capital.upper()]
    for sublista in paises
    for pais, capital in sublista
]

print(lista_transformada) # salida: [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]