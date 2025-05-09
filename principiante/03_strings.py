### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))  # Length of the string
print(len(my_other_string))

print(my_string +" "+ my_other_string)  # Concatenate strings

my_new_line_string = "Este es un String\ncon salto de linea"  # New line
print(my_new_line_string)

my_tab_string = "Este es un String\tcon tabulacion"  # Tab
print(my_tab_string)

# Formateo
print()
name, surname, age = "Luis", "Londono", 43

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))  # Format with format()")
print()
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))  # Format with % operator
print()
print("Mi nombre es " + name + " " + surname + " y mi edad es "+str(age))  # Format with format() with indexes
print()
print(f"Mi nombre es {name} {surname} y mi edad es {age}")  # Format with f-string
print()

# Desempaquetado de caracteres
desp = "hola parce"
a, b, c, d, e, f, g, h ,i, j= desp  # Unpacking characters
print(a)  # H
print(c, b)  # l

# Division de strings
print()
desp_slice = desp[1:3]  # Slicing strings
print(desp_slice)  # ol
print()
desp_slice = desp[1:]  # Slicing strings
print(desp_slice)  # ola
print()
desp_slice = desp[-2]  # Slicing strings
print(desp_slice) # l

print()
desp_slice = desp[::-1]  # Slicing strings
print(desp_slice)  # aloH


# Funciones
print()
print(desp.capitalize())  # Capitalize first letter
print(desp.upper())  # Uppercase
print(desp.lower())  # Lowercase
print(desp.title())  # Title case
print(desp.count("l"))  # Count occurrences of a character
print(desp.find("h"))  # Find first occurrence of a character
print(desp.isnumeric())  # Check if string is numeric
print(desp.isalpha())  # Check if string is alphabetic
print(desp.isalnum())  # Check if string is alphanumeric
print(desp.isdigit())  # Check if string is digit
print(desp.upper().isupper())  # Check if string is uppercase
print(desp.lower().isupper())  # Check if string is lowercase
print(desp.replace("h", "M"))  # Replace character
print(desp.split("l"))  # Split string by character
print(desp.split())  # Split string by whitespace
print(desp.strip())  # Remove whitespace from both sides
print(desp.lstrip())  # Remove whitespace from left side
print(desp.rstrip())  # Remove whitespace from right side
print(desp.startswith("ho"))  # Check if string starts with character


