"""Frontend code for Another-CPS-Tester"""
import flet as ft

def FrontendCPSTester(page: ft.Page):
    """Flet code for Another-CPS-Tester"""

    def close_app(_):
        page.window.destroy()

    close_button = ft.IconButton(icon="close", on_click=close_app, tooltip="close window")

    click_button = ft.ElevatedButton(text="Click Me!" , width=100, height=50)

    page.vertical_alignment = "spaceBetween"
    page.add(
        ft.Column(
            [
                ft.Row(
                    [close_button],
                    alignment="end"
                ),
                ft.Row(
                    [click_button],
                    alignment="center"
                ),
                ft.Row(
                    [
                        ft.Text(
                            value="Brought to you by: sickpancake",
                            color="gray"
                        )
                    ],
                    alignment="center"
                )
            ],
            alignment="spaceBetween"
        )
    )
    page.update()

def openCPSTester():
    """Run the app"""
    ft.app(FrontendCPSTester)
