# 💻 Exercises - Day 1

## Exercise: Level 1

### 1. Check the python version you are using
```shell
$ python --version
Python 3.12.3
```
## Exercise: Level 2
Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

### 2. Do the following operations. The operands are 3 and 4.
* addition(+)
* subtraction(-)
* multiplication(*)
* modulus(%)
* division(/)
* exponential(**)
* floor division operator(//)

```python
print(3+4) # addition(+)
print(3-4) # subtraction(-)
print(3*4) # multiplication(*)
print(3%4) # modulus(%)
print(3/4) # division(/)
print(3**4) # exponential(**)
print(3//4) # floor division operator(//)
```
### 3. Write strings on the python interactive shell. The strings are the following:
* Your name
* Your family name
* Your country
* I am enjoying 30 days of python

```python
print("Victor")
print("Hernandez")
print("Venezuela")
print("I am enjoying 30 days of python")
```

### 4. Check the data types of the following data:
* 10
* 9.8
* 3.14
* 4 - 4j
* ['Asabeneh', 'Python', 'Finland']
* Your name
* Your family name
* Your country
```python
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Victor"))
print(type("Hernandez"))
print(type("Venezuela"))
```

## Exercise: Level 3

### 5. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

```python
number_integer = 10                         # Integer
number_float = 3.14                         # Float
number_complex = 1 + 2j                     # Complex
my_string = "Esto es una cadena"            # String
my_bool = True                              # Boolean
my_list = ["Pera", "Manzana", "Patilla"]    # List
my_tuple = (2,"Casco", True)                # Tuple
my_set = {5,7,8,9,4}                        # Set
my_dictionary = {"name":"Victor"}           # Dictionary
```

### 6. Find an Euclidian distance between (2, 3) and (10, 8)

```python
punto1 = (2, 3)
punto2 = (10, 8)

# Cálculo de la distancia euclidiana
distancia = ((punto2[0] - punto1[0])**2 + (punto2[1] - punto1[1])**2) ** 0.5

print(f"La distancia euclidiana de los puntos {punto1} y {punto2} es: {distancia}")
```
