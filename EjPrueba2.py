year = int(input("Ingrese su año de nacimiento\n--> "))
age = 2025 - year

if age < 13:
    print("Estas en la etapa de la infancia")
elif age >= 13 and age < 20:
    print("Estas en la etapa de la adolescencia")
if age >= 20 and age < 65:
    print("Estas en la etapa de la adultez")
elif age >= 65:
    print("Estas en la etapa de la tercera edad")

print(f"Tu edad es {age}")