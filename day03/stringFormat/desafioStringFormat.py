"""
* Criar variavéis para nome (str), idade(int),
* altura(float) e peso(float) de uma pessoa
* Criar variável com o ano atual(int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings(com chaves)
"""

name = 'Valdeni'
idade = 26
altura = 1.83
peso = 70
ano_atual = 2022
data_nasc = ano_atual - idade
imc = peso / altura ** 2

print(f'{name} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print('O IMC de {} é {:.2f}'.format(name, imc))
print('{na} nasceu em {nasc}'.format(na=name, nasc=data_nasc))
