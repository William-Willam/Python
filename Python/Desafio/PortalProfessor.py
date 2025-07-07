""" Portal do professor """
# importação de bibliotecas e json
import os
import json

# limpa tela
os.system("cls")

# carregar o banco de dados professor
bancoProf = "../Desafio/dados/BancoProfessor.json"
BancoProfessor = []

# leitura do banco professor
if os.path.exists(bancoProf):
    with open(bancoProf, "r") as arquivo:
        BancoProfessor = json.load(arquivo)
else:
    print("Nenhum professor cadastrado ainda.")
    exit()

# Menu login
print("===========================================================")
print("|               Portal do Professor - Login               |")
print("===========================================================")
loginProf = input("Matrícula: ")
senhaProf = input("Senha: ")
print("\n")

# Verifica se o professor está cadastrado
prof_encontrado = None
for prof in BancoProfessor:
    if prof["MatriculaProf"] == loginProf and prof["SenhaProf"] == senhaProf:
        prof_encontrado = prof
        break

if prof_encontrado:
    os.system("cls")
    print(f"Bem-vindo(a), {prof_encontrado['NomeProfessor']}!")
    print(f"Sua matéria: {prof_encontrado['Materia']}\n")

    while True:
        print("====================================================================")
        print("|                      Área do Professor                           |")
        print("|==================================================================|")
        print("| 1 - Visualizar suas avaliações                                   |")
        print("| 2 - Inserir notas de cada aluno                                  |")
        print("| 3 - Atualizar a senha                                            |")
        print("| 4 - Sair                                                         |")
        print("====================================================================")        

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Em desenvolvimento!")
        
        elif opcao == "2":
            print("Em desenvolvimento!")

        elif opcao == "3":
            print("Em desenvolvimento!")

        elif opcao == "4":
            print("Saindo do Portal do Professor...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione ENTER para continuar...")
        os.system("cls")

else:
    print("Matrícula ou senha incorreta. Acesso negado.")
