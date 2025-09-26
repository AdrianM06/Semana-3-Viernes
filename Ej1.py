number = input("Ingresa un número entero positivo\n--> ")

while not(number.isnumeric()) or int(number) < 0:
    number = input("Por favor, ingrese un número entero positivo\n--> ")

#Calcular suma de impares

number = int(number)
sum = 0

for i in range(1,number+1,2):
    sum += i

print(sum)