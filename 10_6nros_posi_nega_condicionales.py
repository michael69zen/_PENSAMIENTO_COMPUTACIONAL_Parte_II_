print("------"*7)
print("PENSAMIENTO COMPUTACIONAL")
print("Ing. Miguel Romilio ACEITUNO ROJO")
print("Est. Cristhian Michael JALLO PAREDES")
print("Código => 236543")
print("------"*7)

# Asignando e Inicializando Variables
negativos = 0
positivos = 0
contador_positivos = 0

# Ingresando Valores
for i in range(6):
    valor = int(input(f"VALOR {i+1}: "))
    
    # evaluando si son positivos o negativos
    if valor < 0:
        negativos += valor
        
    else:
        positivos += valor
        contador_positivos += 1
        
print(f"SUMA DE LOS NÚMEROS NEGATIVOS ES {negativos}")

# si existe positivos dar el promedio
if contador_positivos > 0:
       promedio = positivos/contador_positivos
       print(f"PROMEDIO DE LOS POSITIVOS ES: {promedio}")
# no existe division entre 0
else:
        print("NO INGRESO NÚMEROS POSITIVOS")