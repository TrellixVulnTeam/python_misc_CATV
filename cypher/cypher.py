#Código que visa encriptar senhas

inp = input("Palavra a encriptar: ")

lista = list(inp)

tamanho = len(lista)

for i in range (0,tamanho) :

    #alfabeto

    if lista[i] == "a" or lista[i] == "A":
        lista[i] = "h"

    if lista[i] == "b" or lista[i] == "B":
        lista[i] = "T"

    if lista[i] == "c" or lista[i] == "C":
        lista[i] = ","

    if lista[i] == "d" or lista[i] == "D":
        lista[i] = "a"

    if lista[i] == "e" or lista[i] == "E":
        lista[i] = "e"

    if lista[i] == "f" or lista[i] == "F":
        lista[i] = "3"

    if lista[i] == "g" or lista[i] == "G":
        lista[i] = "á"

    if lista[i] == "h" or lista[i] == "H":
        lista[i] = "b"

    if lista[i] == "i" or lista[i] == "I":
        lista[i] = "#"

    if lista[i] == "j" or lista[i] == "J":
        lista[i] = "Ç"

    if lista[i] == "k" or lista[i] == "K":
        lista[i] = "H"

    if lista[i] == "l" or lista[i] == "L":
        lista[i] = "c"

    if lista[i] == "m" or lista[i] == "M":
        lista[i] = "X"

    if lista[i] == "n" or lista[i] == "N":
        lista[i] = "ã"

    if lista[i] == "o" or lista[i] == "O":
        lista[i] = "D"

    if lista[i] == "p" or lista[i] == "P":
        lista[i] = "l"

    if lista[i] == "q" or lista[i] == "Q":
        lista[i] = "Y"

    if lista[i] == "r" or lista[i] == "R":
        lista[i] = "p"

    if lista[i] == "s" or lista[i] == "S":
        lista[i] = "["

    if lista[i] == "t" or lista[i] == "T":
        lista[i] = "9"

    if lista[i] == "u" or lista[i] == "U":
        lista[i] = "1"

    if lista[i] == "v" or lista[i] == "V":
        lista[i] = "*"

    if lista[i] == "w" or lista[i] == "W":
        lista[i] = "+"

    if lista[i] == "x" or lista[i] == "X":
        lista[i] = "f"

    if lista[i] == "y" or lista[i] == "Y":
        lista[i] = "y"

    if lista[i] == "z" or lista[i] == "Z":
        lista[i] = "7"



#Tornar a lista uma string
senhaf = ''.join(lista)
print("sua senha encriptidada e: " + senhaf)