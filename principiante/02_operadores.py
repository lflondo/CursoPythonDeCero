""""Operadores"""
print("Operadores aritméticos")

print(3 + 4)  # Suma
print(3 - 4)  # Resta
print(3 * 4)  # Multiplicación
print(3 / 4)  # División
print(3 // 4)  # División entera
print(3 % 4)  # Módulo
print(3 ** 4)  # Potencia
print(3 + 4 * 5)  # Operadores de precedencia
print((3 + 4) * 5)  # Operadores de precedencia
print(3 + 4 * 5 - 2)  # Operadores de precedencia
print(3 + 4 * (5 - 2))  # Operadores de precedencia
print(3 + 4 * (5 - 2) / 2)  # Operadores de precedencia
print()
print("Hola "+" luis")
print("Hola " + str (3))
print("Hola", 5)
print("Hola " *5)
print()

"""Operadores de comparación"""
print("Operadores de comparación")

print(3<4)  # Menor que
print(3>4)  # Mayor que
print(3>=4)  # Mayor o igual que
print(3<=4)  # Menor o igual que
print(3==4)  # Igual que
print(3!=4)  # Diferente de
print(3==3<4)  # Igual que y menor que
print(3==3>4)  # Igual que y mayor que
print()

print("hola" == "python")  # Igual que
print("hola" != "python")  # Diferente de
print("hola" < "python")  # Menor que
print("hola" > "python")  # Mayor que
print("hola" <= "python")  # Menor o igual que
print("hola" >= "python")  # Mayor o igual que
print("hola" < "python" < "java")  # Menor que y menor que
print()

print("aaa">="aba")  # Ordenador alfabético
print(len("aaa")>=len("aba"))  # Contador de caracteres
print()
""" Operadores lógicos"""
print("Operadores lógicos")

print(3>4 and "hola">"python")  # Y
print(3>4 or "hola">"python")  # O
print(3<4 and "hola"<"python")  # Y
print(3<4 or "hola"<"python")  # O
print(3<4 or ("hola">"python" and 4==4))  # O Y
print(not(3>4))  # Negación True
print(not(3<4))  # Negación False