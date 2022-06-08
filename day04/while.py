"""
    While em Python
    ultizado para realizar ações enquanto uma condição for verdadeira.
    usado para repetições.
"""

while True: # no while, ele vai checar se a expressão é verdadeira
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Digite (s) para sair.')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Voce precisa digitar um número.')
        continue # Com o continue, ele não executa o bloco abaixo

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador invalido')
