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


# mostrar_contatos()
# buscar_contato("Raphael")
add_editar_contato("Leticia", "7777-9999", "leticia@teste.com", "Av. 3")
add_editar_contato("Leticia", "7777-9999", None, None)
excluir_contato("Leticia")

# editar_contato("leticia", "endereco", "Av. 4")


mostrar_contatos()
