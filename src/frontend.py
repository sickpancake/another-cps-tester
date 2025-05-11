"""Frontend code for Another-CPS-Tester"""
import flet as ft
from backend import BackendCPSTester

def FrontendCPSTester(page: ft.Page):
    """Flet code for Another-CPS-Tester"""

    def close_app(_):
        page.window.destroy()

    def open_final_result(_):
        total_clicks = 0
        total_cps = 0

        final_result_dialogue = ft.AlertDialog(
            title=ft.Text(value="CPS Test Results"),
            content=ft.Column(
                [
                    ft.Text(value=f"Total Clicks: {total_clicks}"),
                    ft.Text(value=f"Clicks Per Second (CPS): {total_cps}"),
                    ft.Text(value="Thank you for using Another-CPS-Tester!"),
                ],
                tight=True
            ),
            actions=[
                ft.IconButton(icon="close", on_click=lambda _: page.close(final_result_dialogue), tooltip="Close Results")
            ]
        )
        page.open(page.open(final_result_dialogue))
        page.update()

    close_button = ft.IconButton(icon="close", on_click=close_app, tooltip="Close APP")

    click_button = ft.ElevatedButton(text="Click Me!" , width=200, height=100)

    page.vertical_alignment = "spaceBetween"
    page.add(
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
                    value="sickpancake",
                )
            ],
            alignment="center"
        )
        
    )

    page.title = "Another-CPS-Tester"

    page.update()

def openCPSTester():
    """Run the app"""
    ft.app(FrontendCPSTester)
