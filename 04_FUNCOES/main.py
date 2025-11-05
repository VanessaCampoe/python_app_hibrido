# biblioteca

from modulo import limpar, primeiro_grau, segundo_grau

def main():
    limpar()
    while True:
        print("0 - Sair do programa") 
        print("1 - Calcular equação do 1º grau")
        print("2 - Calcular equação do 2º grau")
        opcao = input("Opção desejada: ").strip()

        match opcao:
            case "0":
                limpar()
                print("Programa encerrado.")
                break

            case "1":
                try:
                    a = float(input("Informe o valor de 'a': ").strip().replace(",", "."))
                    b = float(input("Informe o valor de 'b': ").strip().replace(",", "."))
                    
                    limpar()
                    x = primeiro_grau(a, b, c)
                    print(f"x = {x}")
                except ValueError:
                    print("Erro: valores inválidos. Tente novamente.")
                continue
            case "2":
                a = float(input("Informe o valor de 'a': ").strip().replace(",", "."))
                b = float(input("Informe o valor de 'b': ").strip().replace(",", "."))
                c = float(input("Informe o valor de 'c': ").strip().replace(",", "."))
                limpar()
                resultados = segundo_grau(a,b,c)
                for x in resultados:
                    print(f"x = {x}")
                continue

            case _:
                limpar()
                print("Opção inválida.")
                continue

if __name__ == "__main__":
    main()
