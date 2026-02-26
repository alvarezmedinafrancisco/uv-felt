import flet as ft

def main(page=ft.Page):
    page.title = "Calculadora de prpina"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_monto = ft.TextField(
        label="Monto de la cuenta",
        value="700",
        text_align=ft.TextAlign.RIGHT,
        width=200
    )

    txt_porcentaje = ft.Text("propina:5%")
    txt_resultado = ft.Text("propina:35\n Total a pagar:$735")

    def calcular_propina(e):
        try:
            monto = float(txt_monto.value)
            porcentaje = slider.value
            propina = monto * (porcentaje / 100)
            total = monto + propina

            txt_porcentaje.value = f"propina:{int(porcentaje)}%"
            txt_resultado.value = f"propina:${propina:.2f}\nTotal a pagar:${total:.2f}"
            page.update()
        except:
            txt_resultado.value = "ingresa un numero valido"
            page.update()

    slider = ft.Slider(
        min=0,
        max=30,
        divisions=30,
        value=5,
        label="{value}%",
        on_change=calcular_propina
    )

    page.add(
        ft.Column(
            [txt_monto, slider, txt_porcentaje, txt_resultado],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    
    page.title = "Calculadora de propina"
    
    page.add(ft.Text(value="Hola, esta es una calculadora de propina", size=30))
    
    
    page.add(ft.Text(value="Ingresa el monto de la cuenta", size=24 , color=ft.Colors.BLUE ,
                    weight=ft.FontWeight.BOLD, 
                    italic=True,
                    text_align=ft.TextAlign.CENTER,
                    max_lines=2,
                    overflow=ft.TextOverflow.ELLIPSIS
                    ))
    
    
    page.add(ft.Image(src="https://cdn-icons-png.flaticon.com/512/1046/1046784.png", width=200, height=200,
                    fit = "cover",
                    border_radius=ft.border_radius.all(10),
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    ))
    
    page.add(ft.Divider(height=10, thickness=2, color=ft.Colors.GREY_400))
    page.add(ft.Row(
        [ft.VerticalDivider(width=10, thickness=2, color=ft.Colors.GREY_400),
        ]))

ft.run(main)