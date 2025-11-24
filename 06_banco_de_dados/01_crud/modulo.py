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


# agra dando cotinuidade do programa de ontem 

# read 
def listar(session, Pessoa):
    try:
    # vamos listar criar uma lista de diciionario 
        pessoas = session.query(Pessoa).all()
            # o objetivo de listar e mostra quem esta caddastrado no banco
            # agora vamos pegar e pedir para exebir na tela 
        print("Pessoas cadastradas:\n")
         # agora vamos pedir para especificar cada um
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}") 
            print(f"Nome : {pessoa.nome}") 
            print(f"E-mail : {pessoa.email}") 
            print(f" Gênero: {pessoa.genero}") 
            print(f"Data de nascimento: {pessoa.nascimento.strftime("%d/%m/%Y")}") 
            print(f"\n{'-'*40}\n")
        
        """pessoa objeto 
        Pessoas classe 
        pessoas lista"""
        
    except Exception as e:
        print(f" Nao foi possivel listar. {e}.")


# update 
def atualizar(session, Pessoa):
    id_pessoa = ""
    email = ""
    novo_nome = "" 
    novo_email = ""
    novo_nascimento = ""
    novo_genero = ""
   
    try:
        print("Escolha o campoe que deseja pesquisar")
        print("1 - ID")
        print("2 - E-mail")
        print("3 - Retornar:")
        opcao= input("opção desejada:").strip()
        limpar()

        match opcao:
            case "1":
                id_pessoa = input("Informe o ID").strip()
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
            case "2":
                email = input("Informe o e-mail:").strip().lower()
                pessoa = session.query(Pessoa).filter_by(email=email).first()
            case "3":
                return ""
            case _:
                return "Opção inválida."
        
        if pessoa:
            limpar()
            while True:
                print(f"ID {pessoa.id_pessoa}")
                print("Qual campo deseja alterar:\n")
                print(f"1 - Nome: {pessoa.nome}")
                print(f"2 - E-mail: {pessoa.email}")
                print(f"3 - Data de nascimento: {pessoa.nascimento.strftime("%d/%m/%Y")}")
                print(f"4 - Gênero: {pessoa.genero}")
                print(f"5 - Finalizar")
                campo = input("Campo desejado: ").strip()
                limpar()
                match campo:
                    case "1":
                        novo_nome = input("Informe o novo nome: ").strip().title()
                        continue
                    case "2":
                        novo_email = input("Informe o novo e-mail: ").strip().lower()
                        pessoas = session.query(Pessoa).filter(Pessoa.email == novo_email).all()
                        if email in [pessoa.email for pessoa in pessoas]:
                            print("E-mail já cadastrado.")
                        continue
                    case "3":
                        novo_nascimento = input("Informe a nova data de nascimento (dd/mm/aaaa): ").strip()
                        continue
                    case "4":
                        novo_genero = input("Informe o novo gênero: ").strip().lower()
                        continue
                    case "5":
                        novo_nome = novo_nome if novo_nome != "" else pessoa.nome
                        novo_email = novo_email if novo_email != "" else pessoa.email
                        novo_nascimento = datetime.strptime(novo_nascimento, "%d/%m/%Y").date() if novo_nascimento != "" else pessoa.nascimento
                        novo_genero = novo_genero if novo_genero != "" else pessoa.genero
                        break
                    case _:
                        print("Campo inexistente.")
                        continue
            pessoa.nome = novo_nome
            pessoa.email = novo_email
            pessoa.nascimento = novo_nascimento
            pessoa.genero = novo_genero

            session.commit()

            return "Dados atualizados com sucesso."
        
        else:
            return "Pessoa não encontrada."
    except Exception as e:
        print(f"Não foi possível alterar os dados. {e}.")


def deletar(session, Pessoa):
    id_pessoa = ""
    email = "" 
    pessoa = ""

    print("Informe o campoe que deseja pesquisar : ")
    print("1 -  ID")
    print("2 - E-mail")
    print("3 - Retornar")
    opcao = input("Informe o campo que deseja pesquisar: ").strip()

    limpar()

    match opcao:
        case "1":
            id_pessoa = input(" Informe o ID a ser excluido: ").strip()
            pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
        case "2":
            email = input("Informe o e-mail do cadastroa ser excluido :").strip().lower()
            pessoa = session.query(Pessoa).filter_by(email=email).first() # em email email quer disser que o  atributo da entidade email . recebe valor do usuaruio pessoa ,

        case "3":
            return ""
        case _:
            return"Opção invalida."
    if pessoa: 
        limpar()
        print(f"ID: {pessoa.id_pessoa}")
        print(f"Nome: {pessoa.nome}")
        print(f"E-mail : {pessoa.email}")
        print(f"Genero: {pessoa.genero}")
        print(f"Data de nascimeto: {pessoa.nascimento.strftime("%d/%m/%Y")}")
        print({'-'*40})
        print("1 - Sim")
        print("2 - Não")
        excluir = input("Tem certeza de que deseja excluir o registro?").strip()

        match excluir:
            case " 1":
                session.delete(pessoa)
                session.commit()
                return "Pessoa excluida com sucesso."

            case "2":
                return ""

            case "_":
                return "Opção invalida."

