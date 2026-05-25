from pages.common.base_page import BasePage


class KeyboardsPage(BasePage):

    def click_keyboards_main_category(self):
        self.page.locator("#mega-menu-item-87457").click()

    def open_keyboards_menu(self):
        self.page.locator(
            '#mega-menu-item-87457 span.mega-indicator'
        ).click()

    def click_keyboards_category(self):
        self.page.locator("#mega-menu-item-87458").click()

    def click_electric_pianos(self):
        self.page.locator("#mega-menu-item-87462").click()

    def click_sheet_music_stands(self):
        self.page.locator("#mega-menu-item-87468").click()