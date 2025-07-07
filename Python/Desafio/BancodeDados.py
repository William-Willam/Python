import os
import json
os.system("cls")

""" Área exclusiva para administradores """
BancoAluno = []
BancoProfessor = []

# Carrega dados dos alunos do arquivo, se existir
if os.path.exists("dados/BancoAluno.json"):
    with open("dados/BancoAluno.json", "r") as arquivo:
        BancoAluno = json.load(arquivo)

# Carrega dados dos professores do arquivo, se existir
if os.path.exists("dados/BancoProfessor.json"):
    with open("dados/BancoProfessor.json", "r") as arquivo:
        BancoProfessor = json.load(arquivo)

# Menu de login
print("===================================================================")
print("|                      Login Administrador                        |")
print("===================================================================\n")
login = input("Login: ")
senha = input("Senha: ")
print("\n")

if login == "Admin" and senha == "admin@123@":
    os.system("cls")
    while True:
        print("=============================================================")
        print("|                    Área dos Administradores               |")
        print("|              Aqui cadastra os alunos e professores        |")
        print("|-----------------------------------------------------------|")
        print("| 1 - Cadastrar Alunos                                      |")
        print("| 2 - Cadastrar Professores                                 |")
        print("| 3 - Listar os Alunos                                      |")
        print("| 4 - Listar os Professores                                 |")
        print("| 5 - Editar ou Excluir Professor                           |")
        print("| 6 - Editar ou Excluir Aluno                               |")
        print("| 7 - Sair                                                  |")
        print("=============================================================\n")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            os.system("cls")
            print("=================== Área de Cadastro de Alunos ====================")
            nomeAluno = input("Insira o nome do Aluno: ")
            cpf = input("Insira o CPF do Aluno: ")
            matricula = input("Insira a matrícula do Aluno: ")
            dataNasc = input("Data de nascimento (ex: DD/MM/AAAA): ")
            senha = input("Insira uma senha: ")

            novoAluno = {
                "nome": nomeAluno,
                "cpf": cpf,
                "matricula": matricula,
                "data_nasc": dataNasc,
                "senha": senha
            }

            BancoAluno.append(novoAluno)
            with open("dados/BancoAluno.json", "w") as arquivo:
                json.dump(BancoAluno, arquivo, indent=4)

            print("\n| Aluno cadastrado com sucesso! |")
            input("| Pressione ENTER para continuar |")
            os.system("cls")

        elif opcao == "2":
            os.system("cls")
            print("=================== Área de Cadastro de Professores ====================")
            nomeProfessor = input("Insira o nome do Professor: ")
            cpfProfessor = input("Insira o CPF do Professor: ")
            DataNascProf = input("Insira a data de nascimento (ex DD/MM/AAAA): ")
            matriculaProf = input("Insira a matrícula: ")
            materia = input("Insira a matéria: ")
            senhaProf = input("Insira a senha: ")

            novoProfessor = {
                "NomeProfessor": nomeProfessor,
                "CpfProf": cpfProfessor,
                "Materia": materia,
                "Data_Nasc_Prof": DataNascProf,
                "MatriculaProf": matriculaProf,
                "SenhaProf": senhaProf
            }

            BancoProfessor.append(novoProfessor)
            with open("dados/BancoProfessor.json", "w") as arquivo:
                json.dump(BancoProfessor, arquivo, indent=4)

            print("\n| Professor cadastrado com sucesso! |")
            input("| Pressione ENTER para continuar |")
            os.system("cls")

        elif opcao == "3":
            os.system("cls")
            print("===================== Lista de Alunos Cadastrados =====================")
            if BancoAluno:
                for aluno in BancoAluno:
                    print(f"Nome: {aluno['nome']} | Matrícula: {aluno['matricula']}")
            else:
                print("Nenhum aluno cadastrado!")
            input("\nPressione ENTER para continuar...")
            os.system("cls")

        elif opcao == "4":
            os.system("cls")
            print("===================== Lista de Professores Cadastrados =====================")
            if BancoProfessor:
                for professor in BancoProfessor:
                    print(f"Nome: {professor['NomeProfessor']} | Matrícula: {professor['MatriculaProf']} | Matéria: {professor['Materia']}")
            else:
                print("Nenhum professor cadastrado.")
            input("\nPressione ENTER para continuar...")
            os.system("cls")

        elif opcao == "5":
            os.system("cls")
            print("===================== Editar ou Excluir Professor =====================")
            matricula = input("Informe a matrícula do professor: ")
            encontrado = False

            for i, professor in enumerate(BancoProfessor):
                if professor["MatriculaProf"] == matricula:
                    encontrado = True
                    print(f"\nProfessor encontrado: {professor['NomeProfessor']} | Matéria: {professor['Materia']}")
                    acao = input("Digite [E]ditar, [D]eletar ou [C]ancelar: ").upper()

                    if acao == "E":
                        professor["NomeProfessor"] = input("Novo nome: ")
                        professor["CpfProf"] = input("Novo CPF: ")
                        professor["Data_Nasc_Prof"] = input("Nova data de nascimento: ")
                        professor["MatriculaProf"] = input("Nova matrícula: ")
                        professor["Materia"] = input("Nova matéria: ")
                        professor["SenhaProf"] = input("Nova senha: ")
                        print("Professor editado com sucesso!")
                    elif acao == "D":
                        BancoProfessor.pop(i)
                        print("Professor excluído com sucesso!")
                    else:
                        print("Operação cancelada.")

                    with open("dados/BancoProfessor.json", "w") as arquivo:
                        json.dump(BancoProfessor, arquivo, indent=4)
                    break

            if not encontrado:
                print("Professor não encontrado!")

            input("\nPressione ENTER para continuar...")
            os.system("cls")

        elif opcao == "6":
            os.system("cls")
            print("===================== Editar ou Excluir Aluno =====================")
            matricula = input("Informe a matrícula do aluno: ")
            encontrado = False

            for i, aluno in enumerate(BancoAluno):
                if aluno["matricula"] == matricula:
                    encontrado = True
                    print(f"\nAluno encontrado: {aluno['nome']}")
                    acao = input("Digite [E]ditar, [D]eletar ou [C]ancelar: ").upper()

                    if acao == "E":
                        aluno["nome"] = input("Novo nome: ")
                        aluno["cpf"] = input("Novo CPF: ")
                        aluno["data_nasc"] = input("Nova data de nascimento: ")
                        aluno["matricula"] = input("Nova matrícula: ")
                        aluno["senha"] = input("Nova senha: ")
                        print("Aluno editado com sucesso!")
                    elif acao == "D":
                        BancoAluno.pop(i)
                        print("Aluno excluído com sucesso!")
                    else:
                        print("Operação cancelada.")

                    with open("dados/BancoAluno.json", "w") as arquivo:
                        json.dump(BancoAluno, arquivo, indent=4)
                    break

            if not encontrado:
                print("Aluno não encontrado!")

            input("\nPressione ENTER para continuar...")
            os.system("cls")

        elif opcao == "7":
            print("Saindo...")
            break

        else:
            print("Opção inválida!\n")
else:
    print("Usuário e senha incorretos!")
