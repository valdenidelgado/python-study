"""
    Condições IF, ELIF E ELSE:
    se um bloco for verddeiro, ele vai passar para o primeiro IF, se for falso vai para elif ou else
"""

if True:
    print('Verdadeiro.')

variavel = False

if variavel: # no if, toda variavel ja vem como true no if
    print('Verdadeiro.')
else:
    print('Falso.')


# Exemplo do elif

if False:
    print('Verdadeiro.')
elif True: # Quando passa o primeiro if, vai cair no segundo if e ver se a condição é verdadeira
    print('Agora é verdadeiro.')
elif False: # Podem existir varios elif
    print('Mais uma verdadeira.')
else:
    print('Falso.')



