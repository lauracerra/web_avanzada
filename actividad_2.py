def verificar_palindromo(texto):
    texto_limpio = texto.lower().replace(" ", "")
    es_palindromo = texto_limpio == texto_limpio[::-1]
    return es_palindromo

entrada_usuario = input("Introduzca una palabra o frase: ")

if verificar_palindromo(entrada_usuario):
    print("¡Es un palíndromo!")
else:
    print("No es un palíndromo.")
