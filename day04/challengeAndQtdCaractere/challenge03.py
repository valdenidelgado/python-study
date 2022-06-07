nome = input('Digite seu nome: ')

qtd = len(nome)

if qtd <= 4:
    print('Seu nome é muito curto. ')
elif qtd > 4 and qtd <= 6:
    print('Seu nome é normal. ')
else:
    print('Seu nome é muito grande. ')
