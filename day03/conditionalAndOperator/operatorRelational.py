"""
    Operadores Relacionais
    ==  : igual a
    >   : maior que
    >=  : maior ou igual a
    <   : menor que
    <=  : menor ou igual a
    !=  : diferente de
    and : e
"""

name = input('Qual o seu nome? ')
idade = int(input('Qual sua idade? '))

# Limite para pegar emprestimo
idade_menor = 20
idade_maior = 30

if idade >= idade_menor:
    print(f'Sr. {name} de {idade} anos. Emprestimo liberado')
else:
    print(f'Sr. {name} de {idade} anos. Emprestimo recusado. Idade não permitida.')


if idade >= idade_menor and idade <= idade_maior:
    print(f'Sr. {name} de {idade} anos. Emprestimo liberado')
else:
    print(f'Sr. {name} de {idade} anos. Emprestimo recusado. Idade não permitida.')
