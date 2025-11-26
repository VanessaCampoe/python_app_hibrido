import flet as ft


def main(page: ft.Page):
    """counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )"""
    # aqui eu comnetei mas em um programa normal eu devo excluir essa parte para eu reutilizar o codigo 
    #  tb deletamoso couter e fica mesmo dando erro  e mantenho a virgula e ai segue ft.Text, a virgula apos recebe meu paramentro 


    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Minha primeria aplicação ", size=40, weight="bold", color="green", font_family="Montserrat" ), # aqui eu meu print do flet 
                alignment=ft.alignment.center,
            )
        # expand=True, excluir 
        

        ),
        ft.Container(
            ft.Image(
                src="1.jpg",
                fit=ft.ImageFit.CONTAIN,
                error_content=ft.Text("Não foi possivel carregar a imagem."),
                width=800,
                height=600,
                opacity=0.4
            ),
            alignment=ft.alignment.center,
            expand=True, 
        
        )
    )
    
    
    

ft.app(main)
