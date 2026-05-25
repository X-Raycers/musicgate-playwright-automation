from pages.common.base_page import BasePage


class PercussionPage(BasePage):

    def click_percussion_main_category(self):
        self.page.locator("#mega-menu-item-87484").click()

    def open_percussion_menu(self):
        self.page.locator(
            '#mega-menu-item-87484 span.mega-indicator'
        ).click()

    def click_darbukas(self):
        self.page.locator("#mega-menu-item-87488").click()

    def click_bongos(self):
        self.page.locator("#mega-menu-item-88211").click()

    def click_xylophones(self):
        self.page.locator("#mega-menu-item-88216").click()