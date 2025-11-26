import flet as ft


def main(page: ft.Page):
    # função do evento 
    def exibir_nome(e):
        nome_saida.value = nome.value
        nome_saida.update()


    #PROPRIEDADE DA PAGINA
    page.title = "App de manipulação de evenetos " # titulo de aba da  pagina
    page.scroll = " adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT  # se fosse para preto esta dark
    page.update()

    # declaração de variaveis 
    nome = ft.TextField(label="Inofrme seu nome: ", on_submit=exibir_nome)
    nome_saida = ft.Text()

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Trabalhando com Eventos", size=35, weight="bold"),
                
                alignment=ft.alignment.top_center,
            ),
            #expand=True,
        ),
        
            nome,
            ft.ElevatedButton("Enviar ", on_click=exibir_nome ),
                     
            nome_saida,
                     
                    

        

        ft.Container(
                ft.Text("🌌 Entre constelações e cafés frios No meio da madrugada, quando a cidade já dormia, um gato cinza atravessava os telhados como se fosse dono do universo. Lá embaixo, um rádio esquecido ainda tocava uma música antiga, misturando-se ao som distante de um trem. O vento carregava histórias que ninguém lembrava, e cada estrela parecia piscar como se estivesse rindo de segredos guardados." ),
                
                # Alinhamento no canto superior esquerdo
                alignment = ft.alignment.top_right,
            )
    
)

ft.app(main)

"""

calcular qual o melhor conbustivel e o melhorpara o etanl ser vantajoso o etanol tem que ser 70 % mais barato 
"""