import string

caracteres_ascii = string.ascii_letters
print(caracteres_ascii)

def verificar(cadena):
    # Verifica  carácter por caracter de la cadena 
    for caracter in cadena:
        if caracter not in caracteres_ascii:
            return False
    return True

cadena1 = "Estoesunacadena"
print(verificar(cadena1))
