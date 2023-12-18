print("------"*7)
print("PENSAMIENTO COMPUTACIONAL")
print("Ing. Miguel Romilio ACEITUNO ROJO")
print("Est. Cristhian Michael JALLO PAREDES")
print("Código => 236543")
print("------"*7)

# Requiriendo un entero al Usuario
nro = int(input("CANTIDAD DE ITERACIONES: "))

# Asignando Variable 
suma = 0

# Realizar la cantidad de iteraciones dada por el Usuario
for i in range (nro):
    # Ingresar Valores en cada iteracion
    valor = int(input(f"INGRESE EL VALOR {i+1}: "))
    # Sumar valores 
    suma += valor

# Imprimir la suma de los valores    
print(f"LA SUMA DE LOS VALORES ES: {suma}")