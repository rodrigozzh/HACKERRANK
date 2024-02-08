def encuentra_valor(lista, string):
    valor = 0 
    # Lee la lista completa y revisa cuantas veces se repite y lo suma
    for palabra in lista:
        valor += string.count(palabra)
    return valor

def variaciones(letras, string):
    lista = []
    for letra in letras:
        # La posición del la primera aparición de la letra
        indice = string.find(letra)
        # Iteramos en la posición donde se encuentra la letra hasta el final de la palabra y se crea la palabra
        palabra = ""
        for pos in range(indice, len(string)):
            palabra = palabra + string[pos]
            lista.append(palabra)
    return(lista)


def minion_game(string):
    # your code goes here

    # Separo las volcales y las consonantes del string
    vocales = "aeiouAEIOU"
    vocales = [caracter for caracter in string if caracter in vocales]
    consonantes = [letra for letra in string if letra not in vocales]
    vocales = list(set(vocales))
    consonantes = list(set(consonantes))
    # Lista que contendra todas las variaciones

    lista_consonantes = variaciones(consonantes, string)
    lista_vocales = variaciones(vocales, string)

    # Encontrar el valor de cada palabra de la lista
    valor_consonantes =  encuentra_valor(lista_consonantes, string)
    valor_vocales=  encuentra_valor(lista_vocales, string)

    if valor_consonantes > valor_vocales:
        return(print(f"Stuart {valor_consonantes}"))
    else:
        return(print(f"Kevin {valor_vocales}"))





        
    
if __name__ == '__main__':
    s = input()
    minion_game(s)