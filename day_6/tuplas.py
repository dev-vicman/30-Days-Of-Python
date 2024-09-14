""" Day 6: 30 Days of python programming """

# * Ejercicios: Nivel 1

# ? Crear una tupla vacía

mi_tupla = (1, 2, 3, 4, 5)

# %%
# ? Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien)

hermanas = ("Maria", "Carla", "Gabriela", "Daniela")
hermanos = ("Rafael", "Arturo")


# ? Unir tuplas de hermanos y hermanas y asignarlas a hermanos
list(hermanos)
hermanos = hermanas + hermanos
print(hermanos)


# ? ¿Cuántos hermanos tienes?

print(f"Tengo {len(hermanos)} hermanos")


# ? Modifica la tupla de hermanos y agrega el nombre de tu padre y madre y asígnalo a family_members

# Transformamos la Tupla en una lista
hermanos = list(hermanos)

# Agregamos los nuevos elementos a lista
hermanos.append("Tata")
hermanos.append("Rafael")

# Asignamos la lista hermanos a family_members
family_members = hermanos

# Mostramos en pantalla
print(family_members)

# * Ejercicios: Nivel 2

# %%
# ? Desempaquetar hermanos y padres de family_members

*hermanos, madre, padre = family_members

print(hermanos)
print(madre)
print(padre)

# %%
# Crea tuplas de frutas, verduras y productos animales. Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp.

# Declarando las tuplas
frutas = ("Manzana", "Pera", "Mango")
productos_animales = ("Huevos", "Leche", "Carne")

# Asignando frutas y productos animales a food_stuff_tp
food_stuff_tp = frutas + productos_animales
print(food_stuff_tp, type(food_stuff_tp))
# Cambie la tupla about food_stuff_tp a una lista food_stuff_lt

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt, type(food_stuff_lt))
