from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open_homepage(self):
        self.page.goto(
            "https://musicgate.co.il/"
        )

        self.page.wait_for_load_state(
            "networkidle"
        )