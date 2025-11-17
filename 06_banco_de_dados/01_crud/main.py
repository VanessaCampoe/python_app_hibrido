from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker  #tecnologia usada para o proprio programa fazer as tabelas , aqui ele cria tudo sozinho a parde de ddl dml 

from entidades import criar_tb_pessoa
from modulo import limpar

def main():
    engine = create_engine("sqlite:///01_crud/database/crud.db")
    Base = declarative_base()
    Pessoa = criar_tb_pessoa(engine, Base) 
    Session = sessionmaker(bind=engine)
    session = Session()

    limpar()
    # TODO: FAZER O crud

    session.close()

if __name__ == "__main__":
    main()

"""
veja que seu erros foram 
a pasta database nao estava dentro de do crud 
logo depois tinha um erro na definição do metadata em entidade , corrigido isso e voltando a executar o crt f5 e pedir para debugar o crud aparece dentro da pasta database drud.db 
"""

"""
aqui eu vou dar f1 e digitar sqlite e escolher o opendatabase e escolher o banco que estamos usando  
"""