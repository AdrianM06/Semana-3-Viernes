print("Bienvenido a la tienda\n")

precio = int(input("Ingresa el precio del producto:\n-->"))
miembro = input("Es usted miembro? (si/no)")

miembro == miembro.lower()

if miembro == "si" and precio >= 50:
    precio *= 0.85
elif precio >= 50:
    precio *= 0.95
elif miembro == "si":
    precio *= 0.90
else:
    print("No tienes descuento")

print(f"Tu precio es {precio}")