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
    for nome, dados in AGENDA.items():
        print(f"Nome: {nome}")
        print(f"Telefone: {dados['telefone']}")
        print(f"E-mail: {dados['email']}")
        print(f"Endereço: {dados['endereco']}")
        print("-" * 30)


mostrar_contatos()
