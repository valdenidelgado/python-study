"""
    o metodo input, é para o usuario digitar algum valor pelo terminal, mas tambem ele pode ja passar diretamente uma msg para o usuario, ex: input('digite um valor')
    Todo valor do input vai ser retornado como string
    para reverter isso, podemos usar o casting para manipular os dados que serão enviados
"""

name = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

ano_nasc = 2022 - int(idade)

print() # print() vazio, quebra uma linha
print(f'{name} tem {idade} anos. '
      f'{name} nasceu em {ano_nasc}.')

# Calculadora com casting

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outr número:' ))

print()
print(num1 + num2)
