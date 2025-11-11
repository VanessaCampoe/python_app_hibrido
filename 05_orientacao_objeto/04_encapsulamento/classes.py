class Pessoa:
    def __init__(self, nome, cpf):
        #self.nome = nome 
        #self.cpf = cpf
        #era assim , agora a baixo deixr ele encapsulado 

        self.__nome = nome 
        self.__cpf = cpf