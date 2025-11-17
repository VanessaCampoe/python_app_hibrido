import os
from classes import Pessoa

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    # Criando objeto com valores iniciais
    usuario = Pessoa(nome="", idade=0, altura=0.0)

    # Entrada de dados
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int(input("Informe a idade: ").strip())
    usuario.altura = float(input("Informe a altura em metros: ").strip().replace(",", "."))

    # Limpa tela e mostra resultado
    limpar()
    print(usuario)  # Mostra representação automática da dataclass
    print(f"{usuario.nome} {usuario.verificar_maioridade()}.")

if __name__ == "__main__":
    main()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              