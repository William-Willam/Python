"""
Bloco 2: input(), Operadores e Conversão de Tipos

Cadastro Simples
Use o comando input() para pedir ao usuário que digite o nome dele e guarde em uma variável.
Use input() para pedir a idade dele e guarde em outra variável.
Use input() para pedir a altura dele (lembre-se de usar ponto para decimais, como 1.75) e guarde em uma terceira variável.
Imprima todas as informações coletadas. Opcionalmente, use type(variavel) dentro do print() para mostrar o tipo de dado de cada variável.
Dica: Lembre-se que o input() sempre retorna texto! Se precisar de números, terá que converter.

Conversor de Anos para Meses
Peça ao usuário para digitar quantos anos ele tem usando input().
Converta essa idade para um número inteiro (usando int()).
Calcule quantos meses de vida essa pessoa tem.
Imprima o resultado de forma clara.
Exemplo de saída esperada:
Você tem 20 anos, o que equivale a 240 meses.


Média de Notas
Peça ao usuário para digitar 3 notas de provas (podem ser números decimais, como 7.5, 8.0).
Converta as notas para números decimais (usando float()).
Calcule a média dessas 3 notas.
Imprima a média final.
"""

# Cadastro Simples
nome = input("Digite seu nome: ")
idade = input("Digite a idade: ")
altura = input("Digite sua altura (ex: 1.75): ")

# Resultado
print("\n============ Informações coletadas ==============\n")
print("Nome: ", nome)
print("Idade: ", idade)
print("Altura: ", altura)

# Conversor de anos para meses
print("\n============ Conversor de ano para Meses ==============\n")
idade_ano = int(input("Quantos anos você tem: "))

idade_mes = idade_ano * 12
print(f"Você tem {idade_ano} anos, ou seja, em meses você tem {idade_mes} meses de vida")

# Média de notas
print("\n============ Calculo da Média ==============\n")
nota1 = float(input("Digite a primeira a nota: "))
nota2 = float(input("Digite a segunda a nota: "))
nota3 = float(input("Digite a terceira a nota: "))

media = (nota1 + nota2 + nota3) /3
print(f"Sua média final é: {media:.2f}")