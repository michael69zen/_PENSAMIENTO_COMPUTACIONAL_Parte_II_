print("------"*7)
print("PENSAMIENTO COMPUTACIONAL")
print("Ing. Miguel Romilio ACEITUNO ROJO")
print("Est. Cristhian Michael JALLO PAREDES")
print("Código => 236543")
print("------"*7)

# Asignando Variable para requerir numero
num = int(input("INGRESE UN NUMERO ENTERO POSITIVO: "))

# Condicion para que se cumpla que sea positivo
if num > 0 :
    # Rangos para delimitar numeros a imprimir
    for i in range(num,2*num):
        #imprimimos (i)
        print(i)
# Si el usuario ingresa un numero negativo, pedir que ingrese uno positivo
else:
    print("INGRESE UN NÚMERO POSITIVO.")