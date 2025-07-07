# Importação de biblioteca e arquivos json
import os
import json

# limpa tela
os.system("cls")

# carrega o banco de alunos
bancoDados = "../Desafio/dados/BancoAluno.json"
BancoAluno = []

# carrega o banco de professores
bancoDados2 = "../Desafio/dados/BancoProfessor.json"
BancoProfessor = []

# carrega o banco de avaliações
bancoAvaliacoes = "../Desafio/dados/Avaliacoes.json"
Avaliacoes = []

# carrega o banco de notas
bancoNotas = "../Desafio/dados/Notas.json"
Notas = []

if os.path.exists(bancoDados):
    with open(bancoDados, "r") as arquivo:
        BancoAluno = json.load(arquivo)
else:
    print("Nenhum aluno cadastrado ainda.")
    exit()

if os.path.exists(bancoDados2):
    with open(bancoDados2, "r") as arquivo:
        BancoProfessor = json.load(arquivo)
else:
    print("Nenhum professor cadastrado ainda.")
    exit()

if os.path.exists(bancoAvaliacoes):
    with open(bancoAvaliacoes, "r") as arquivo:
        Avaliacoes = json.load(arquivo)

if os.path.exists(bancoNotas):
    with open(bancoNotas, "r") as arquivo:
        Notas = json.load(arquivo)

# Menu login do aluno
print("=======================================================")
print("|               Portal do Aluno - Login               |")
print("=======================================================")
loginAluno = input("Matricula: ")
senhaAluno = input("Senha: ")
print("\n")

# condicional para verificar se a senha ta certa e a matricula
aluno_encontrado = None
for aluno in BancoAluno:
    if aluno["matricula"] == loginAluno and aluno["senha"] == senhaAluno:
        aluno_encontrado = aluno
        break

# Se aluno for encontrado, exibe o menu do portal
if aluno_encontrado:
    os.system("cls")
    print(f"Bem-vindo(a), {aluno_encontrado['nome']}!\n")

    while True:
        print("====================================================================")
        print("|                          Área do Aluno                           |")
        print("|==================================================================|")
        print("| 1 - Avaliar professores                                          |")
        print("| 2 - Visualizar notas                                             |")
        print("| 3 - Atualizar a senha                                            |")
        print("| 4 - Sair                                                         |")
        print("====================================================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            os.system("cls")
            print("===================================================================")
            print("|                   Avaliar os Professores                        |")
            print("===================================================================")
            for i, professor in enumerate(BancoProfessor):
                print(f"{i+1}. {professor['NomeProfessor']} - {professor['Materia']}")
            escolha = int(input("\nEscolha o número do professor a ser avaliado: ")) - 1

            if 0 <= escolha < len(BancoProfessor):
                nota = int(input("Dê uma nota de 1 a 10: "))
                comentario = input("Deixe um comentário (opcional): ")
                avaliacao = {
                    "aluno": aluno_encontrado["nome"],
                    "matricula_aluno": aluno_encontrado["matricula"],
                    "professor": BancoProfessor[escolha]["NomeProfessor"],
                    "materia": BancoProfessor[escolha]["Materia"],
                    "nota": nota,
                    "comentario": comentario
                }
                Avaliacoes.append(avaliacao)
                with open(bancoAvaliacoes, "w") as arquivo:
                    json.dump(Avaliacoes, arquivo, indent=4)
                print("\nAvaliação registrada com sucesso!")
            else:
                print("\nOpção inválida.")

        elif opcao == "2":
            os.system("cls")
            print("===================================================================")
            print("|                   Visualizar Notas e Médias                     |")
            print("===================================================================")
            encontrou = False
            for nota in Notas:
                if nota["matricula"] == aluno_encontrado["matricula"]:
                    encontrou = True
                    print(f"Matéria: {nota['materia']} | Nota 1: {nota['nota1']} | Nota 2: {nota['nota2']} | Média: {nota['media']}")
            if not encontrou:
                print("Nenhuma nota registrada para você até o momento.")

        elif opcao == "3":
            os.system("cls")
            print("===================================================================")
            print("|                   Atualizar a senha                             |")
            print("===================================================================")
            senha_atual = input("Digite sua senha atual: ")

            if senha_atual == aluno_encontrado["senha"]:
                nova_senha = input("Digite a nova senha: ")
                confirma_senha = input("Confirme a nova senha: ")

                if nova_senha == confirma_senha:
                    aluno_encontrado["senha"] = nova_senha
                    with open(bancoDados, "w") as arquivo:
                        json.dump(BancoAluno, arquivo, indent=4)
                    print("Senha atualizada com sucesso!")
                else:
                    print("As senhas não coincidem. Tente novamente.")
            else:
                print("Senha atual incorreta.")

        elif opcao == "4":
            print("Saindo do Portal do Aluno...")
            break

        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione ENTER para continuar...")
        os.system("cls")

else:
    print("Matrícula ou senha inválida. Acesso negado.")
