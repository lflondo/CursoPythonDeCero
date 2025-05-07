#Variables

my_var = "una varible string"
print(my_var)

my_int_variable = 7
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

print(my_var, my_int_variable, my_bool_variable)


# Variables de una sola linea
name, surname, nickname, age = "Luis", "Londono", "Kre", 43
print("me llamo", name, surname, "y tengo", age, "años y me dicen", nickname)


#Input de variables
name = input("¿Cual es tu nombre? ")
age = int(input("¿Cual es tu edad? "))
print("Hola", name, "tienes", age, "años")

#Input de variables con formato
name = input("¿Cual es tu nombre? ")
age = int(input("¿Cual es tu edad? "))
print(f"Hola {name} tienes {age} años")