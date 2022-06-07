inteiro = input('Digite um numero inteiro: ')
e_int = inteiro.isnumeric()

if e_int:
    parse_int = int(inteiro)
    if parse_int % 2 == 0:
        print('par')
    else:
        print('impar')
else:
    print('Não é inteiro')
