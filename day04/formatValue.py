"""
    Formatando valores com modificadores

    :s - Text (str)
    :d - Inteiros (int)
    :f - Decimais (float)
    :.(NUMERO)f - Quantidade de casas decimais (float)
    :(caractere)(> ou < ou ^)(quantidade)(tipo - s, d ou f)

    > - esquerda
    < - direita
    ^ - centro
"""

# Para preencher valores usamos dessa maneira

num = 1
# Aqui iremos deixar com 10 digitos, nove 0 e o valor da variavel
# Ficou nove zeros a esquerda
print(f'{num:0>10}')

# Ficou nove zeros a direita
print(f'{num:0<10}')

# Ficou com o numero da variavel ao centro e foi preenchido ao lado
print(f'{num:0^10}')

