# desição de  veriaveis 
nome = input("informe o nome :").strip().title()
idade = int(input("informe o idade :").strip().title())
altura = float(input("informe o altura :").strip().replace(',' , '.'))

# erificação das condiçoes 

if idade >= 12 and altura >= 1.15 :
    print(f"entrada de {nome } autorizada.")
else: 
    print(f"entrada de {nome  } não autorizada.")
