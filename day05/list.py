"""
    Listas em python
    fatiamento(slice)
    append, insert, pop, del, clear, extend, +
    min, max
    range
"""

# O extend é para extender a lista

l1 = [1,2,3]
l2 = [4,5,6]

l3 = l1 + l2
l1.extend(l2) # mesma coisa que l1 + l2

# Para adicionar um valor a lista, usando o append()
l2.append('b') # adiciona um valor ao final da lista

# Para definir qual indice voce quer adicionar um novo valor. Use o insert()
l2.insert(0, 'valor') # Primeiro é o indice e o segundo é o valor

# Para remover um elemento no final da lista, use o pop()
l2.pop()

# Para fatiar/deletar alguns indices, podemos usar o del()
del(l2[2:4]) # Primeiro é onde começa o indice e o segundo é até onde vai

print(l2)

# Para pegar o maior valor da lista use o max()
print(max(l3))

# Para pegar o menor valor da lista use o min()
print(min(l3))


secreto = 'perfume'
digitado = []
chance = 3

while True:
    if chance <= 0:
        print('voce perdeu')
        break
    chance -= 1
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso não vale, precisa ser maior que 1')
        continue

    digitado.append(letra)

    if letra in secreto:
        print(f'Existe essa {letra} no secreto')
    else:
        print(f'Não existe {letra} no secreto')
        digitado.pop()

    secreto_temp = ''
    for letra_secreto in secreto:
        if letra_secreto in digitado:
            secreto_temp += letra_secreto
        else:
            secreto_temp += '*'

    if secreto_temp == secreto:
        print('que legal, voce ganhou')
        break
    else:
        print(f'a palavra secreta, esta asssim {secreto_temp}')

    if letra not in secreto:
        chance -= 1

    print(f'voce ainda tem {chance} chances')
    print()
