print("------"*7)
print("PENSAMIENTO COMPUTACIONAL")
print("Ing. Miguel Romilio ACEITUNO ROJO")
print("Est. Cristhian Michael JALLO PAREDES")
print("Código => 236543")
print("------"*7)

# Requerimos al Usuario que ingrese la Frase
frase = input("ESCRIBA LA FRASE: ")

# Creamos un conjunto, para que no se repita los mismos valores
vocales = set()
# convertimos la frase en minusculas para no diferenciar entre (Mayusc/minusc).
frase = frase.lower()

# utilizando el bucle for, para iterar cada caracter de la cadena de caracteres
for i in frase:
    # si cumple la condicion, de que sean vocales que le añada al conjunto vocales
    if i == "a":
        vocales.add(i)
    elif i == "e":
        vocales.add(i)
    elif i == "i":
        vocales.add(i)
    elif i == "o":
        vocales.add(i)
    elif i == "u":
        vocales.add(i)

#imprimimos las vocales que aparecen en la frase dada por el Usuario      
print(vocales)