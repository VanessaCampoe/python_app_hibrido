from sqlalchemy import Column, String, Integer, Date 

# função que cria banco de dados e as entidades 
def criar_tb_pessoa(engine, Base):
    try:
        class Pessoa(Base):
    # tratamento de execeção 
    
            __tablename__ = "pessoa" 
            # agora vou criar meus atributos  q  e o q uma classe  e banco de adados tem em comum 

            #atributos 
            # o que vai organizar minhas colunas  vai ser a primary kaey 
            id_pessoa = Column(Integer, primary_key=True, autoincrement=True)     # metodo da classe base (como se fosse uma herança da classe )
            nome = Column(String, nullable=False)
            nascimento = Column(Date, nullable=False)
            email = Column(String, nullable=False, unique=True)
            genero = Column(String, nullable=True)
        Base.metadata.create_all(engine)      # responsavel por criar meu banco 

        return Pessoa   #retoma a minha classe



    except Exception as e:
        print(f"Não foi possivel conectar com o banco de dados{e}.")
