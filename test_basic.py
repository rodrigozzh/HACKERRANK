cadena = "aWESOME is cODING"
palabras = cadena.split()
palabras_invertidas = palabras[::-1]


lista_palabra = []
for palabra in palabras_invertidas:
    frase_final = ""
    print(palabra)
    for letra in palabra:
        if letra.isupper():
            frase_final += letra.lower()
        else:
            frase_final += letra.upper()
    lista_palabra.append(frase_final)

resultado = ' '.join(lista_palabra)
print(resultado)
