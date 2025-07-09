""" Portal do professor """
# importação de bibliotecas e json
import os
import json

# limpa tela
os.system("cls")

# carregar o banco de dados professor
bancoProf = "../Desafio/dados/BancoProfessor.json"
BancoProfessor = []

# carregar o banco de dados avaliações
bancoAvaliacao = "../Desafio/dados/Avaliacoes.json"
BancoAvaliacao = []

# carregar o banco de dados alunos
bancoAluno = "../Desafio/dados/BancoAluno.json"
BancoAluno = []

# leitura do banco professor
if os.path.exists(bancoProf):
    with open(bancoProf, "r") as arquivo:
        BancoProfessor = json.load(arquivo)
else:
    print("Nenhum professor cadastrado ainda.")
    exit()

# leitura do banco avaliações
if os.path.exists(bancoAvaliacao):
    with open(bancoAvaliacao, "r") as arquivo:
        BancoAvaliacao = json.load(arquivo)
else:
    print("Nenhuma avaliação registrada ainda.")
    exit()

# leitura do banco Aluno
if os.path.exists(bancoAluno):
    with open(bancoAluno, "r") as arquivo:
        BancoAluno = json.load(arquivo)
else:
    print("Nenhum aluno cadastrado!")
    exit()

# Função para filtrar avaliações do professor logado
def filtrarAvaliacao(BancoAvaliacao, prof_encontrado):
    return [av for av in BancoAvaliacao if av["professor"] == prof_encontrado["NomeProfessor"]]


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
        print("| 2 - Área das notas e faltas                                      |")
        print("| 3 - Atualizar a senha                                            |")
        print("| 4 - Sair                                                         |")
        print("====================================================================")        

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            os.system("cls")
            Avaliacao = filtrarAvaliacao(BancoAvaliacao, prof_encontrado)

            if Avaliacao:
                notas = [av["nota"] for av in Avaliacao]
                media = sum(notas) / len(notas)

                print("=" * 66)
                print("|{:^64}|".format("Visualizar Avaliações"))
                print("|{:^64}|".format("Atenção: É para melhoria profissional e educacional"))
                print("=" * 66)
                print("| {:<40} {:>21} |".format("Total de Avaliações Recebidas:", len(notas)))
                print("| {:<40} {:>21.2f} |".format("Média Geral das Avaliações:", media))
                print("=" * 66)
                print("|{:^64}|".format("Sua Classificação"))

                if media >= 9:
                    print("|{:^64}|".format("Excelente professor e tem domínio do conteúdo!"))
                elif media >= 7:
                    print("|{:^64}|".format("Bom professor e tem bom domínio do conteúdo!"))
                elif media >= 5:
                    print("|{:^64}|".format("Professor mediano. Pode melhorar sua didática."))
                else:
                    print("|{:^64}|".format("A diretoria irá conversar para feedbacks!"))
                print("=" * 66)
            else:
                print(f"{prof_encontrado['NomeProfessor']}, você ainda não foi avaliado!")

        elif opcao == "2":
            while True:
                os.system("cls")
                print("=================================================================")
                print("|                       Área das notas                          |")
                print("=================================================================")
                print("| 1 - Listar os alunos                                          |")
                print("| 2 - Aplicar notas e faltas                                    |")
                print("| 3 - Voltar                                                    |")
                print("=================================================================")
                subopcao = input("Escolha a opção: ")

                if subopcao == "1":
                    os.system("cls")
                    if BancoAluno:
                        for i, aluno in enumerate(BancoAluno, start=1):
                            print(f"=========================== Aluno {i} ===========================")
                            print(f"Nome: {aluno['nome']}")
                            print(f"Matrícula: {aluno['matricula']}")
                    else:
                        print("Nenhum aluno cadastrado!")
                    input("\nPressione ENTER para continuar...")

                elif subopcao == "2":
                    os.system("cls")
                    if BancoAluno:
                        for i, aluno in enumerate(BancoAluno, start=1):
                            print(f"========================= Aluno {i} ===============================")
                            print(f"Nome: {aluno['nome']} | Matrícula: {aluno['matricula']}")
                            
                            materia = input(f"Matéria: {prof_encontrado['Materia']}")

                            try:
                                nota1 = float(input("Insira a primeira nota: "))
                                nota2 = float(input("Insira a segunda nota: "))
                                nota3 = float(input("Insira a terceira nota: "))
                                faltas = int(input("Quantidade de faltas: "))
                            except ValueError:
                                print("Erro: Digite apenas números válidos!")
                                continue

                            media = round((nota1 + nota2 + nota3) / 3, 2)
                            situacao = "Aprovado" if media >= 7 and faltas <= 10 else "Reprovado"

                            notas_materia = {
                                "nota1": nota1,
                                "nota2": nota2,
                                "nota3": nota3,
                                "media": media,
                                "situacao": situacao,
                                "faltas": faltas
                            }

                            if "notas" not in aluno:
                                aluno["notas"] = {}

                            aluno["notas"][materia] = notas_materia

                        with open(bancoAluno, "w") as arquivo:
                            json.dump(BancoAluno, arquivo, indent=4)
                        print("\nNotas e faltas salvas com sucesso!")
                    else:
                        print("Nenhum aluno cadastrado!")
                    input("\nPressione ENTER para continuar...")

                elif subopcao == "3":
                    break
                else:
                    print("Opção inválida!")
                    input("\nPressione ENTER para continuar...")
    
        elif opcao == "3":
            os.system("cls")
            print("=================================================================")
            print("                       Atualizar a senha                         ")
            print("=================================================================")
            senha_atual = input("Digite a sua senha atual: ")

            if senha_atual == prof_encontrado["SenhaProf"]:
                nova_senha = input("Digite a nova senha: ")
                confirma_senha = input("Confirme a nova senha: ")

                if nova_senha == confirma_senha:
                    prof_encontrado["SenhaProf"] = nova_senha
                    with open(bancoProf, "w") as arquivo:
                        json.dump(BancoProfessor, arquivo, indent=4)
                    print("Senha atualizada com sucesso!")
                else:
                    print("As senhas não coincidem. Tente novamente.")
            else:
                print("Senha incorreta!")

        elif opcao == "4":
            print("Saindo do Portal do Professor...")
            break

        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione ENTER para continuar...")
        os.system("cls")

else:
    print("Matrícula ou senha incorreta. Acesso negado.")
