from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker  #tecnologia usada para o proprio programa fazer as tabelas , aqui ele cria tudo sozinho a parde de ddl dml 

from entidades import criar_tb_pessoa
from modulo import limpar, cadastrar, listar,atualizar, deletar

def main():
    engine = create_engine("sqlite:///01_crud/database/crud.db")
    Base = declarative_base()
    Pessoa = criar_tb_pessoa(engine, Base)
    Session = sessionmaker(bind=engine)
    session = Session()

    limpar()
    while True:
        print(f"{'-'*20} 🐍 CRUD DA COBRA 🐍 {'-'*20}\n")
        print("0 - Sair do programa")
        print("1 - Cadastrar nova pessoa")
        print("2 - Listar pessoas")
        print("3 - Atualizar dados")
        print("4 - Excluir pessoa")
        opcao = input("Opção desejada: ").strip()
        limpar()
        match opcao:
            case "0":
                print("Programa encerrado.")
                break
            case "1":
                print(cadastrar(session, Pessoa))
                continue
            case "2":
                listar(session, Pessoa)
                continue
            case "3":
                print(atualizar(session, Pessoa))
                continue
            case "4":
                print(deletar(session, Pessoa))
                continue
            case _:
                print("Opção inválida.")
                continue

    session.close()

if __name__ == "__main__":
    main()

    # para abrir o banco devo usar o f1 depois opem data base e depois o meu banco o endereço vai aparecer 

"""
veja que seu erros foram 
a pasta database nao estava dentro de do crud 
logo depois tinha um erro na definição do metadata em entidade , corrigido isso e voltando a executar o crt f5 e pedir para debugar o crud aparece dentro da pasta database drud.db 
"""

"""
aqui eu vou dar f1 e digitar sqlite e escolher o opendatabase e escolher o banco que estamos usando  
"""