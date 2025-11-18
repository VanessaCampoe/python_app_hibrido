"""CRUD é um acrônimo usado em programação e banco de dados que representa as quatro operações básicas de manipulação de dados:

✅ C – Create (Criar)

Inserir novos registros.
Ex.: adicionar um novo usuário ao sistema.

✅ R – Read (Ler)

Consultar dados existentes.
Ex.: listar todos os produtos cadastrados.

✅ U – Update (Atualizar)

Modificar dados existentes.
Ex.: editar o nome de um cliente.

✅ D – Delete (Excluir)

Remover dados do sistema.
Ex.: apagar um registro de pedido."""

import os
from datetime import datetime

def limpar():
    os.system("cls" if os.name == "nt" else "clear")
def cadastrar(session, Pessoa):
    try:
        nome = input("Informe o nome:").strip().title()
        genero = input("informe o genero:").strip().lower()
        nascimento = input("Informe a data de nascimento (dd/mm/aaaa):").strip()
        nascimento = datetime.strptime(nascimento, "%d/%m/%Y").date() # lembrar que a na formatação de datas deve ser o Y maiusculo . 
        email = input("Informe o e-mail:").strip().lower()

        pessoas = session.query(Pessoa).filter(Pessoa.email.like(email)).all()
        # buscando pessoas filtrado pelo atribto email q seja com email iguais 
        # aqui completa a linha de cma com essa da para intermpretar o codigo e o que no final esta pedido 
        # dessa forma lembre-se  ler mais lihas para compreender o codigos 
        # #  fazer um apend a na lista 
        if email in [pessoa.email for pessoa in pessoas]:
            print("E-mail já cadastrado")
        else:
            nova_pessoa = Pessoa(
                nome=nome,
                nascimento=nascimento,
                email=email,
                genero=genero
            )
            # insert into pessoa
            session.add(nova_pessoa)
            session.commit()
                                 


    except Exception as e:
        print(f"Não foi possivel cadastrar. {e}.")