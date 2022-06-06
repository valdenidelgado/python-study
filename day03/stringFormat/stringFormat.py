"""
    Para criar uma formatação e tornar mais legivel e de facil manipulação, podemos usar o fstrings, de formatação, ex: string(f'string {variavel}')
"""


nome = 'Valdeni'
idade = 25
peso = 70
altura = 1.83
imc = peso / altura ** 2

# A formatação de quantidade de casas decimais, usa a {variavel:.quantidadeCasasf}
print(f'Eu {nome}, tenho {idade} anos, meu imc é de {imc:.2f}')

# Outra forma é usando o .format(), coloca as variaveis na msm sequencia 
print('Eu {}, tenho {} anos, meu imc é de {:.2f}'.format(nome, idade, imc))

# Com essa forma, eu posso dizer a ordem tambem, colocando o valor
print('Eu {2}, tenho {0} anos, meu imc é de {1} {1}'.format(nome, idade, imc))
# E posso repetir varias vezes a msm variavel so colocando o indice que ela está

# Tambem posso colocar um alias e definir um nome para cada variavel. ex:
print('Eu {no}, tenho {i} anos, meu imc é de {im:.3f}'.format(no=nome, i=idade, im=imc))
# E como eu ja nomiei as variaveis, tambem posso mudar a ordem
