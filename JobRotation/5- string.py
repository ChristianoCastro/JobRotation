# Definindo a string a ser invertida
string = "String a ser invertida"

# Convertendo a string para uma lista de caracteres
lista_caracteres = list(string)

# Obtendo o tamanho da lista de caracteres
tamanho_lista = len(lista_caracteres)

# Invertendo os caracteres da lista
for i in range(tamanho_lista // 2):
    lista_caracteres[i], lista_caracteres[tamanho_lista - i - 1] = lista_caracteres[tamanho_lista - i - 1], lista_caracteres[i]

# Convertendo a lista de caracteres de volta para uma string
string_invertida = "".join(lista_caracteres)

# Imprimindo a string invertida
print(string_invertida)
