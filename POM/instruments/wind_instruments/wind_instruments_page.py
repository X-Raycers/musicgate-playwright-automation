from pages.common.base_page import BasePage


class WindInstrumentsPage(BasePage):

    def click_wind_instruments_main_category(self):
        self.page.locator("#mega-menu-item-87506").click()

    def open_wind_instruments_menu(self):
        self.page.locator(
            '#mega-menu-item-87506 span.mega-indicator'
        ).click()

    def click_harmonicas(self):
        self.page.locator("#mega-menu-item-87514").click()

    def click_melodicas(self):
        self.page.locator("#mega-menu-item-87513").click()

    def click_kazoo(self):
        self.page.locator("#mega-menu-item-87516").click()