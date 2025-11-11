from classes import Pessoa
def main ():
    usuario = Peso(nome="", cpf="")

    usuario.nome = input("Informe  seu :").strip().title()
    usuario.cpf = input("Informe  seu :").strip().title()

    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    if __