"""Frontend code for Another-CPS-Tester"""
import flet as ft
from backend import BackendCPSTester

def frontend_cps_tester(page: ft.Page):
    """Flet code for Another-CPS-Tester"""
    def reset():
        cps_tester.reset_to_default()

    def close_app(_):
        page.window.destroy()

    def button_clicked(_):
        if cps_tester.is_time_up() is True:
            cps_tester.start()
        cps_tester.add_click()

    def open_final_result():
        results = cps_tester.final_calculate()
        total_clicks = results.total_clicks
        total_cps = results.total_cps

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
                ft.IconButton(
                    icon="close",
                    on_click=lambda _: page.close(final_result_dialogue),
                    tooltip="Close Results"
                )
            ]
        )
        page.open(final_result_dialogue)
        page.update()

    def update_click_button():
        instant_results = cps_tester.instant_calculate()
        click_button.content = ft.Column(
            controls=[
                ft.Text("Countiune Clicking!"),
                ft.Text(f"Current Clicks: {instant_results.current_clicks}"),
                ft.Text(f"Current CPS: {instant_results.current_cps}"),
                ft.Text(f"Time Left: {instant_results.time_left} seconds")
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        )

        page.update()

    def reset_click_button():
        click_button.content = ft.Column(
            controls=[ft.Text("Click Me!")],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        )

        page.update()

    def callback(is_time_up: bool):
        if is_time_up is True:
            open_final_result()
            reset_click_button()
            cps_tester.reset_to_default()
        else:
            update_click_button()


    cps_tester = BackendCPSTester(callback)
    reset()

    close_button = ft.IconButton(icon="close", on_click=close_app, tooltip="Close APP")

    click_button = ft.ElevatedButton(
        content=ft.Column(
            controls=[ft.Text("Click Me!")],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        width=250,
        height=125,
        on_click=button_clicked
    )

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

def open_cps_tester():
    """Run the app"""
    ft.app(frontend_cps_tester)
