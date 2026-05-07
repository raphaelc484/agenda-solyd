AGENDA = {}

AGENDA["Raphael"] = {
    "telefone": "9999-9999",
    "email": "raphaelc@teste.com",
    "endereco": "Av. 1",
}

AGENDA["Rayssa"] = {
    "telefone": "8888-9999",
    "email": "rayssa@teste.com",
    "endereco": "Av. 2",
}


def mostrar_contatos():
    for nome, _ in AGENDA.items():
        buscar_contato(nome)


def buscar_contato(contato):
    for nome, dados in AGENDA.items():
        if nome.lower() == contato.lower():
            print(f"Nome: {nome}")
            print(f"Telefone: {dados['telefone']}")
            print(f"E-mail: {dados['email']}")
            print(f"Endereço: {dados['endereco']}")
            print("-" * 30)


def add_editar_contato(nome, telefone, email, endereco):
    AGENDA[nome] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
    }
    print(f"Contato {nome} foi add/editado com sucesso!!")


# def add_contato(nome, telefone, email, endereco):
#     AGENDA[nome] = {
#         "telefone": telefone,
#         "email": email,
#         "endereco": endereco,
#     }
#     print(f"Contato {nome} foi adicionado com sucesso!!")

# def editar_contato(nome, valor, novo_valor):
#     for contato, dados in AGENDA.items():
#         if nome.lower() == contato.lower():
#             dados[valor] = novo_valor
#             print(f"Contato {nome} foi editado com sucesso!!")


def excluir_contato(contato):
    AGENDA.pop(contato)
    print(f"Contato {contato} foi excluido com sucesso!!")


def imprimir_opçoes():
    print("1 - Mostrar todos os contatos da agenda")
    print("2 - Buscar contato")
    print("3 - Incluir contato")
    print("4 - Editar contato")
    print("5 - Excluir contato")
    print("0 - Fechar agenda")
    print("-" * 30)


# mostrar_contatos()
# buscar_contato("Raphael")
# add_editar_contato("Leticia", "7777-9999", "leticia@teste.com", "Av. 3")
# add_editar_contato("Leticia", "7777-9999", None, None)
# excluir_contato("Leticia")
# editar_contato("leticia", "endereco", "Av. 4")
# mostrar_contatos()

imprimir_opçoes()

opcao = input("Escolha uma opçao: ")

if opcao == "1":
    mostrar_contatos()
elif opcao == "2":
    contato = input("Qual contato deseja consultar: ")
    buscar_contato(contato)
elif opcao in ("3", "4"):
    nome = input("Qual nome do contato: ")
    telefone = input("Qual telefone do contato: ")
    email = input("Qual email do contato: ")
    endereco = input("Qual endereço do contato: ")
    add_editar_contato(nome, telefone, email, endereco)
    buscar_contato(nome)
elif opcao == "5":
    contato = input("Qual contato deseja excluir: ")
    excluir_contato(contato)
    mostrar_contatos()
elif opcao == "0":
    print("Saindo da agenda")
else:
    print("Opção inválida")
