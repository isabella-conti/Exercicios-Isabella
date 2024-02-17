# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;


string = input("Digite uma string para ser invertida: ")

lista_de_caracteres = list(string)

lista_invertida = []
for caracter in lista_de_caracteres:
    lista_invertida.insert(0, caracter)  

string_invertida = ''.join(lista_invertida)

print("String invertida:", string_invertida)
