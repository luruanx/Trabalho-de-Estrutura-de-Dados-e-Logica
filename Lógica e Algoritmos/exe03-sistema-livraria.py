print("Bem-vindo à Livraria do Ruan Richard\n")

#Lista para armazenar os livros
lista_livro = []
id_global = 0

#Função para cadastrar um livro
def cadastrar_livro(id):
    print("\n---------------------------------------------------")
    print("-------------MENU CADASTRAR LIVRO------------------")
    print("---------------------------------------------------")
    print(f"Id do Livro: {id}")
    nome = input("Por favor, digite o Nome do livro: ")
    autor = input("Por favor, digite o Autor do livro: ")
    editora = input("Por favor, digite a Editora do livro: ")

    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }
    lista_livro.append(livro)
    print("Livro cadastrado com sucesso!")

#Função para consultar livros
def consultar_livro():
    while True:
        print("\n---------------------------------------------------")
        print("-------------MENU CONSULTAR LIVRO------------------")
        print("---------------------------------------------------")
        print("Escolha a opção desejada:")
        print("1 - Consultar Todos os Livros")
        print("2 - Consultar por ID")
        print("3 - Consultar por Autor")
        print("4 - Retornar ao menu principal")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            print("\nLista de todos os livros cadastrados:")
            for livro in lista_livro:
                print(f"\nId: {livro['id']}")
                print(f"Nome: {livro['nome']}")
                print(f"Autor: {livro['autor']}")
                print(f"Editora: {livro['editora']}")
        elif opcao == "2":
            try:
                id_busca = int(input("Digite o ID do livro que deseja consultar: "))
                encontrado = False
                for livro in lista_livro:
                    if livro["id"] == id_busca:
                        print(f"\nId: {livro['id']}")
                        print(f"Nome: {livro['nome']}")
                        print(f"Autor: {livro['autor']}")
                        print(f"Editora: {livro['editora']}")
                        encontrado = True
                        break
                if not encontrado:
                    print("Livro com esse ID não encontrado.")
            except ValueError:
                print("ID inválido. Digite um número inteiro.")
        elif opcao == "3":
            autor_busca = input("Digite o nome do autor: ")
            encontrados = [livro for livro in lista_livro if livro["autor"].lower() == autor_busca.lower()]
            if encontrados:
                for livro in encontrados:
                    print(f"\nId: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
            else:
                print("Nenhum livro encontrado para esse autor.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

#Função para remover livro
def remover_livro():
    while True:
        try:
            id_remover = int(input("Digite o ID do livro que deseja remover: "))
            for livro in lista_livro:
                if livro["id"] == id_remover:
                    lista_livro.remove(livro)
                    print("Livro removido com sucesso!")
                    return
            print("Id inválido. Tente novamente.")
        except ValueError:
            print("ID inválido. Digite um número inteiro.")

#Menu principal
while True:
    print("\n---------------------------------------------------")
    print("----------------MENU PRINCIPAL---------------------")
    print("---------------------------------------------------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro(s)")
    print("3 - Remover Livro")
    print("4 - Encerrar Programa")

    opcao_menu = input("Digite a opção desejada: ")

    if opcao_menu == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao_menu == "2":
        consultar_livro()
    elif opcao_menu == "3":
        remover_livro()
    elif opcao_menu == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")