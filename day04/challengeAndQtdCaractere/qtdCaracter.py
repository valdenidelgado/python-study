"""
    Aqui é para ver a quantidade de caracteres
    o metodo len(), faz a leitura desses caracteres
    so funciona com strings, não funciona com numeros inteiros e etc
"""


num = input('Digite o usuario: ')
qtd_caractere = len(num)

if qtd_caractere < 7:
    print('Voce precisa digitar mais que 6 caracteres')
else:
    print('Usuario cadastrado')
