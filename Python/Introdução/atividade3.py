"""
Bloco 3: Estruturas Condicionais (if, elif, else)

Verificador de Maioridade

Peça ao usuário para digitar sua idade.
Se a idade for igual ou maior que 18, imprima: "Você é maior de idade."
Senão (se a idade for menor que 18), imprima: "Você é menor de idade."
Lembre-se da indentação (espaços no início da linha) após o if e else!

Comparador de Números

Peça ao usuário para digitar dois números inteiros.
Use condicionais (if, elif, else) para verificar e imprimir qual número é o maior, ou se eles são iguais.
Exemplos de saída esperada:
O primeiro número (X) é maior que o segundo (Y).
O segundo número (Y) é maior que o primeiro (X).
Os números são iguais.

Classificador de Número (Positivo, Negativo ou Zero)

Peça ao usuário para digitar um número inteiro.
Use if, elif e else para verificar:
Se o número é positivo.
Senão, se o número é negativo.
Senão (se não for positivo nem negativo, então é zero).

Imprima a classificação correspondente.
"""
# Importação do limpa tela
import os

# Verificador de Maioridade
os.system("cls")

print("==================== Verificador de Maioridade ====================\n")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade !")
else:
    print("Você é menor de idade!")    

print("\n")

# Comparador de número
print("==================== Comparador de Números ====================\n")
numA = int(input("Digite o primeiro numero: "))
numB = int(input("Digite o segundo numero: "))

if numA > numB:
    print(f"numero {numA} é maior do que o numero {numB}")
elif numB == numA:
    print(f"numero {numA} é igual a numero {numB}") 
else:
    print(f"numero {numB} é maior do que o numero {numA}")
           
# Classificador de Número (Positivo, Negativo ou Zero)
print("==================== Classificador de Número  ====================\n")
numero = int(input("Digite um numero: "))

if numero > 0:
    print(f"{numero} é positivo!")
elif numero < 0:
    print(f"{numero} é negativo!")    
else:
    print(f"{numero} se não for positivo nem negativo, então é zero")    
