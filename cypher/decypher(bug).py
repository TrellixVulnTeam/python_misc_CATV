#Código que visa desencriptar as senhas feitas no cypher.py

inp = input("senha encriptada: ")

lista = list(inp)

tamanho = len(lista)

for i in range (0,tamanho) :

    #alfabeto

    if lista[i] == "h": 
        lista[i] = "a"

    if lista[i] == "T":
        lista[i] = "b"

    if lista[i] == ",":
        lista[i] = "c"

    if lista[i] == "a":
        lista[i] = "d"

    if lista[i] == "e":
        lista[i] = "e"

    if lista[i] == "3":
        lista[i] = "f"

    if lista[i] == "á":
        lista[i] = "g"

    if lista[i] == "b":
        lista[i] = "h"

    if lista[i] == "#":
        lista[i] = "i"

    if lista[i] == "Ç":
        lista[i] = "j"

    if lista[i] == "H":
        lista[i] = "k"

    if lista[i] == "c":
        lista[i] = "l"

    if lista[i] == "X":
        lista[i] = "m"

    if lista[i] == "ã":
        lista[i] = "n"

    if lista[i] == "D":
        lista[i] = "o"

    if lista[i] == "l":
        lista[i] = "p"

    if lista[i] == "Y":
        lista[i] = "q"

    if lista[i] == "p":
        lista[i] = "r"

    if lista[i] == "[":
        lista[i] = "s"

    if lista[i] == "9":
        lista[i] = "t"

    if lista[i] == "1":
        lista[i] = "u"

    if lista[i] == "*":
        lista[i] = "v"

    if lista[i] == "+":
        lista[i] = "w"

    if lista[i] == "f":
        lista[i] = "x"

    if lista[i] == "y":
        lista[i] = "y"

    if lista[i] == "7":
        lista[i] = "z"

#Tornar a lista uma string
senhaf = ''.join(lista)
print("sua senha original e: " + senhaf)