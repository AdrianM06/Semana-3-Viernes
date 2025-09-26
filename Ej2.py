import random

primo = False
generados = [] #Numeros generados

while not primo:
    num = random.randint(0,101)
    generados.append(num)
    if num in [0,1]:
        pass
    elif num >= 2:
        divisores = []
        for div in range(1,num+1):
            if num % div == 0:
                divisores.append(div)
        if len(divisores) <= 2:
            primo = True

print(generados)