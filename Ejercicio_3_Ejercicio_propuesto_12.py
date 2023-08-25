#Ejercicio 3: Ejercicio propuesto 12
horastrabajadas = float(input("ingrese el número de horas trabajadas ", )) #permite al usuario ingresar el número de horas
salario = float(input("ingrese el valor de la hora ", )) #permite al usuario ingresar el valor de cada hora
porcretenfuente = 0.125

salariobruto = float(salario*horastrabajadas)
retenfuente = float(salariobruto*porcretenfuente)
salarioneto = float(salariobruto-retenfuente)

print(salariobruto)
print(retenfuente)
print(salarioneto)

