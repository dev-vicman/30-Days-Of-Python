# Day 1 - 30_days_of_python_challenge

# 2. Do the following operations. The operands are 3 and 4.

print(3+4) # addition(+)
print(3-4) # subtraction(-)
print(3*4) # multiplication(*)
print(3%4) # modulus(%)
print(3/4) # division(/)
print(3**4) # exponential(**)
print(3//4) # floor division operator(//)

# 3. Write strings on the python interactive shell. The strings are the following:

print("Victor")
print("Hernandez")
print("Venezuela")
print("I am enjoying 30 days of python")

# 4. Check the data types of the following data:

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Victor"))
print(type("Hernandez"))
print(type("Venezuela"))

# 5. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

number_integer = 10                         # Integer
number_float = 3.14                         # Float
number_complex = 1 + 2j                     # Complex
my_string = "Esto es una cadena"            # String
my_bool = True                              # Boolean
my_list = ["Pera", "Manzana", "Patilla"]    # List
my_tuple = (2,"Casco", True)                # Tuple
my_set = {5,7,8,9,4}                        # Set
my_dictionary = {"name":"Victor"}           # Dictionary

# 6. Find an Euclidian distance between (2, 3) and (10, 8)
# Puntos
punto1 = (2, 3)
punto2 = (10, 8)

# Cálculo de la distancia euclidiana
distancia = ((punto2[0] - punto1[0])**2 + (punto2[1] - punto1[1])**2) ** 0.5

print(f"La distancia euclidiana de los puntos {punto1} y {punto2} es: {distancia}")

