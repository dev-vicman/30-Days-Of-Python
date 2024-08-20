""" Day 5: 30 Days of python programming """

# Ejercicios: Nivel 1

# %%
# 1. Declarar una lista vacía
lista = []
print(lista) # []

# 2. Declarar una lista con más de 5 elementos

lista = ["Pera", "Mangos", "Tomates", "Manzana", "Durazno", "Fresas"]

# 3. Encuentra la longitud de tu lista

print(len(lista)) # 6

# %%
# 4. Obtener el primer elemento, el elemento del medio y el último elemento de la lista.
lista = ["Pera", "Mangos", "Tomates", "Manzana", "Durazno", "Fresas"]
primer_elemento = lista[0]
elemento_medio = lista[len(lista)//2]
ultimo_elemento = lista[-1]

print(primer_elemento)
print(elemento_medio)
print(ultimo_elemento)

# %%
# 5. Declara una lista llamada mixed_data_types, pon tu(nombre, edad, altura, estado civil, dirección)

mixed_data_types = ["Victor", 41, 1.71, "Soltero", "4295 E Mexico Ave"]

# 6. Declare una variable de lista llamada it_companies y asigne los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Imprima la lista usando print()
print(it_companies) # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 8. Imprima el número de empresas en la lista

print(len(it_companies)) # 7

# 9. Imprima la primera, la segunda y la última empresa.
print(it_companies[0]) # Facebook
print(it_companies[1]) # Google
print(it_companies[-1]) # Amazon

# 10. Añadir una empresa de TI a it_companies

it_companies.append("Twitter")
print(it_companies)

# 11. Insertar una empresa de TI en el medio de la lista de empresas
it_companies.insert(len(it_companies)//2, "CompuMundoHiperMegaRed")
print(it_companies)

# %%
# 12. Cambie uno de los nombres de it_companies a mayúsculas (¡IBM excluido!)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

it_companies[2] = it_companies[2].upper()
print(it_companies[2]) # MICROSOFT

# 13. Unir it_companies con una cadena '#; '

print("#; ".join(it_companies)) # Facebook#; Google#; MICROSOFT#; Apple#; IBM#; Oracle#; Amazon

# 14. Comprueba si una determinada empresa existe en la lista it_companies.

existe_empresa = "Facebook" in it_companies
print(existe_empresa) # True

existe_empresa = "Twitter" in it_companies
print(existe_empresa) # False
# %%
# 15. Ordenar la lista usando el método sort()

# Declaramos la lista
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Ordenamos la lista
it_companies.sort()

# Mostramos la lista
print(it_companies)

# 16.Invierta la lista en orden descendente utilizando el método reverse()

it_companies.reverse()
print(it_companies)
# %%
# 17. Separa las primeras 3 empresas de la lista.

# Declaramos la lista
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

tres_empresas = it_companies[0:3] 
print(tres_empresas) # ['Facebook', 'Google', 'Microsoft']

# %%
# 18. Elimina las últimas 3 empresas de la lista.

# Declaramos la lista
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

del it_companies[-3:]
print(it_companies) # ['Facebook', 'Google', 'Microsoft', 'Apple']
# %%
