import flet as ft
class MainMenu:
    def __init__(self, page: ft.Page):
        self.page = page

        # -- Name Window --
        self.page.title = "FBills"

        # -- Calling app's widgets --

        # -- 1st layer --
        self.app_bar()
        self.navigation_bars()

        # 2nd layer --
        self.widget()

        # -- 3rd Layer --
        self.list_bills()

    def app_bar(self):
        """The menu bar of the app that is only showed at the main menu"""
        def handle_checked_item_click(e: ft.Event[ft.PopupMenuItem]):
            e.control.checked = not e.control.checked

        self.page.appbar = ft.AppBar(
            leading=ft.Icon(ft.Icons.PALETTE),
            leading_width=40,
            title=ft.Text("FBills"),
            center_title=False,
            bgcolor="#2ECC71",
            actions=[
                ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
                ft.IconButton(ft.Icons.FILTER_3),
                ft.PopupMenuButton(
                    key="popup",
                    items=[
                        ft.PopupMenuItem(content="Item 1"),
                        ft.PopupMenuItem(),  # divider
                        ft.PopupMenuItem(
                            content="Checked item",
                            checked=False,
                            on_click=handle_checked_item_click,
                        ),
                    ],
                ),
            ],
        )
        self.page.add(ft.SafeArea(content=ft.Column()))

    def navigation_bars(self):
        """It draws the navigation bar"""
        self.page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icon(
                        ft.Icons.DOMAIN,
                        badge=ft.Badge(small_size=10),
                    ),
                    label="Explore",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.EXPLORE,
                    label="Explore",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icon(
                        ft.Icons.SETTINGS,
                        badge="10",
                    ),
                    label="settings",
                ),
            ]
        )
        self.page.add(ft.SafeArea(content=ft.Column()))

    def widget(self):
        """It draws separated widgets, which always are going to show at the 2nd 
        layer."""
        self.page.floating_action_button = ft.FloatingActionButton(
            icon=ft.Icons.ADD, on_click=None
        )

    def list_bills(self):
        """It shows how many bills exist depending on a list"""
        r = ft.Row(wrap=True, scroll="always", expand=True)
        self.page.add(r)

        for i in range(5):
            r.controls.append(
                ft.Container(
                    ft.Text(f"Item {i}"),
                    width=100,
                    height=100,
                    alignment=ft.Alignment.CENTER,
                    bgcolor=ft.Colors.AMBER_100,
                    border=ft.Border.all(1, ft.Colors.AMBER_400),
                    border_radius=ft.BorderRadius.all(5),
                )
            )
        self.page.update()

def main(page: ft.Page):
    MainMenu(page)

if __name__ == "__main__":
    ft.run(main)
