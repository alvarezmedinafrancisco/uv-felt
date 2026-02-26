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

ft.run(main)