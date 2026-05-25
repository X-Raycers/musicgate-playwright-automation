from pages.common.base_page import BasePage


class GuitarsPage(BasePage):

    def click_guitars_main_category(self):
        self.page.locator(
            'a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa"]'
        ).click()

    def open_guitars_menu(self):
        self.page.locator(
            'a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa"] span.mega-indicator'
        ).click()

    def click_acoustic_guitars(self):
        self.page.locator(
            'a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa-%d7%90%d7%a7%d7%95%d7%a1%d7%98%d7%99%d7%95%d7%aa"]'
        ).click()

    def click_electric_guitars(self):
        self.page.locator(
            'a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa-%d7%97%d7%a9%d7%9e%d7%9c%d7%99%d7%95%d7%aa"]'
        ).click()

    def click_classical_guitars(self):
        self.page.locator(
            'a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa-%d7%a7%d7%9c%d7%90%d7%a1%d7%99%d7%95%d7%aa"]'
        ).click()