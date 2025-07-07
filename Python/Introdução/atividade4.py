"""
Bloco 4: Desafios Combinados (Para quem quiser ir além!)

Aprovado ou Reprovado com Recuperação
Peça ao usuário para digitar 3 notas (decimais).
Calcule a média dessas notas.
Use condicionais (if, elif, else) para classificar o aluno:
Média maior ou igual a 7: "Aprovado!"
Média entre 5 e 6.9 (inclusive 5): "Recuperação."
Média menor que 5: "Reprovado."

Login Simples
Defina um usuario_correto (por exemplo, "admin") e uma senha_correta (por exemplo, "12345") como variáveis no seu código.
Peça ao usuário para digitar o usuário e a senha usando input().
Use operadores lógicos (and) com if/else para verificar se o usuário E a senha digitados estão corretos.
Se ambos estiverem corretos, imprima: "Login bem-sucedido!"
Senão, imprima: "Usuário ou senha incorretos."
"""

# importação
import os

#Desafios Combinados
os.system("cls")

#####  prof eu coloquei os dois exercicio em "um" como desafio do desafio !!! ######

print("========================= Sistema de login =========================\n")
login = input("Digite o seu login: ")
senha = input("Digite sua senha: ")
print("\n")

if login == "admin" and senha == "1234":
    print("Login bem-sucedido!\n")
    print("====================== Insira as notas ==========================\n")
    
    # inserindo Notas
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    # calculo da média
    media = (nota1 + nota2 + nota3)/3
    
    #processamento de dados
    if media >= 7:
        print("\n")
        print(f"Aluno aprovado, a sua média foi: {media:.2f}")
    elif media >= 5 and media < 6.9:
        print("\n")
        print(f"Aluno está em recuperação, a sua média foi: {media:.2f}")
    else:
        print("\n")
        print(f"Aluno está reprovado, a sua média foi: {media:.2f}")

    print("\n")
    print("Fim do acesso!\n")         
else:
    print("Usuário ou senha incorretos.")