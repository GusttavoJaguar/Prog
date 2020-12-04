a = "Gustavo"
b = "Mariana"
"""
Aula de strings em python :

-lista de caracteres
-contagem de caracteres(len)
-letra minúscula(lower)
-letra maiúscula(upper)
-remove caractere especial(strip)
-converte sequência em lista(split)
-encontra caracteres ou substring(find)

"""
concatenar = a + " & " + b + "\n"

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])

tamanho = len(concatenar)
print(tamanho)

print(concatenar[0:7])

print(concatenar)
print(concatenar.lower())
print(concatenar.upper())
concatenar = concatenar.upper()
print(concatenar.strip())

minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split()
print(minha_lista)

busca = minha_string.find("rei")
print(busca)

print(minha_string[busca:])