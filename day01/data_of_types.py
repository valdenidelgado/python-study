"""
    Tipos de dados
    str - string - textos "assim"
    int - inteiro - 10, 20, 30
    float - real/ponto - 1.23, 52.1, -19.398
    bool - booleano/logico - true/false
"""
# O python é interpretado, ele automaticamente sabe qual tipo de dados está trabalhando
# Para voce saber qual dado esta retornando, use o type()

print('Test', type('Test')) # Ele retorna o tipo, não mostra o valor
print(10, type(10))
print(10.42, type(10.42))
print('L' == 'L', type('L' == 'L'))

# podemos fazer o casting tambem

print('10', type('10'), type(int('10')))
print(10, type(10), type(float(10)))


##############################
# Exercicio

# Nome: String
print('Valdeni', type('Valdeni'))

# Idade: int
print(25, type(25))

# Altura: float
print(1.83, type(1.83))

# É maior de idade ?
print(25 > 18, type(25 > 18))

