print("------"*7)
print("PENSAMIENTO COMPUTACIONAL")
print("Ing. Miguel Romilio ACEITUNO ROJO")
print("Est. Cristhian Michael JALLO PAREDES")
print("Código => 236543")
print("------"*7)

# Requiriendo al Usuario una frase
frase = input("FRASE: ")

# Definiendo las vocales
vocales = "aeiou"
# convirtiendo en minusculas para no haber distincion
frase = frase.lower()

# creamos.un conjunto de las vocales que aparecen, si hay repeticion lo cuenta porque es lista
voc_frase = list()

# iteramos la frase con el bucle for 
for i in frase:
    # si es igual a una de las vocales
    if i in vocales:
        #que se añada a la lista
        voc_frase.append(i)

#imprimir conteo de la lista es decir las vocales que existen en la frase
print(len(voc_frase))