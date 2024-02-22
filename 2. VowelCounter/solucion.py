##Escribe una funcion que dado un string,
#cuente el número de vocales que contiene.
#El programa debe imprimir el número de vocales
#que contiene el string.


def count_vowels(string):
    ##Escribe tu código a partir de aquí
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count 

print(count_vowels("hola")) #debe imprimir 2

