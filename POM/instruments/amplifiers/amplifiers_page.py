from pages.common.base_page import BasePage


class AmplifiersPage(BasePage):

    def click_amplifiers_main_category(self):
        self.page.locator(
            'a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%9e%d7%92%d7%91%d7%a8%d7%99%d7%9d"]'
        ).click()

    def open_amplifiers_menu(self):
        self.page.locator(
            'a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%9e%d7%92%d7%91%d7%a8%d7%99%d7%9d"] span.mega-indicator'
        ).click()

    def click_electric_guitar_amplifiers(self):
        self.page.locator("#mega-menu-item-87454").click()

    def click_acoustic_guitar_amplifiers(self):
        self.page.locator("#mega-menu-item-87452").click()

    def click_amplifier_accessories(self):
        self.page.locator("#mega-menu-item-87451").click()