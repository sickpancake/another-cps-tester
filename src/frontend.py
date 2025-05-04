"""Frontend code for Another-CPS-Tester"""
import flet as ft

def FrontendCPSTester(page: ft.Page):
    """Flet code for Another-CPS-Tester"""

    def close_app(e):
        page.window.destroy()

    close_button = ft.IconButton(icon="close", on_click=close_app, tooltip="close window")

    page.add(
        ft.Row(
            [close_button],
            alignment="end"
        ),
    )
    page.update()

def openCPSTester():
    """Run the app"""
    ft.app(FrontendCPSTester)
