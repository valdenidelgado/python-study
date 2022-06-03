"""
    As variaveis tem que começar com letras
    pode conter numeros
    separar por _
    letras minusculas

    sinal de igual ("=") é de atribuição, atribui valor em uma variavel ex:
    name = "alex"

    o padrão é snake_case
"""

name = "Alex"
peso_alex = 80
mes_2019 = 8

print("nome", name, ", peso", peso_alex, ", mes 2019", mes_2019)

print('Exercicio IMC')

name = 'Valdeni Delgado'
idade = 25
altura = 1.83
peso = 70

imc = peso / (altura * altura)

print(name, 'tem', idade, 'de idade e seu imc é', imc)


"""
    Exercicios:

    01 - Analisando o código abaixo:
        nome = 'Joãozinho'
        idade = """40"""
        peso = 80.5
        e_maior = True
 
        print(nome, 'tem', idade, 'anos e pesa', peso, 'quilos')
        print(nome, 'é maior de idade?', e_maior)

        Qual o tipo das variáveis nome, idade, peso e e_maior?

        R> string, string, float e bool
