"""
    Operadores logicos
    and   : e
    or    : ou
    not   : não
    in    : em
    not in: não em
"""

# Exemplo de comparação com and
var1 = 2
var2 = 4
var3 = 3
print('Comparanção se a variavel1 é igual variavel2 e ela é menor que variavel3')
print(var1 == var2 and var2 < var3)

# Exemplo com or, se uma das duas for verdadeiro, vai retornar true
print(var1 == var2 or var2 < var3)

# Exemplo com not, not é para inverter uma expressão,not a == b(se a não é iguala b)
print(not var1 == var2 or not var2 < var3)

# Um trecho de codigo explicando melhor o not, por default o if, é true, mas se colocar not, ele vai esperar false

a = 2
b = 3
if not b > a: # com o not, ele vai retornar false, ent ele vai cair no else
    print('B é maior que A')
else:
    print('A é maior q B')

# Exemplo com in, basicamente ele vai chegar algo dentro da variavel
nome = 'Valdeni'

if 'e' in nome:
    print('Existe a letra "e" no seu {nome}.')

# Exemplo com not in, basicamente ele inverte a expressão in

if 'eeee' not in nome: # aqui está assim:  se 'eeee' não estiver dentro da variavel
    print('Não existe isso no nome')
else:
    print('Existe')

# Programa de login basico.

usuario = input('User: ')
senha = input('Password: ')

usuario_bd = 'valxd'
senha_bd = '321'

if usuario_bd == usuario and senha_bd == senha:
    print('Logado.')
else:
    print('Senha invalida.')

