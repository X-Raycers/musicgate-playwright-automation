from pages.common.base_page import BasePage


class SearchPage(BasePage):

    def search_product(self, product_name):
        self.page.get_by_role(
            "textbox"
        ).fill(product_name)

    def click_search_button(self):
        self.page.get_by_role(
            "button",
            name="חיפוש"
        ).click()

    def press_enter(self):
        self.page.keyboard.press(
            "Enter"
        )

    def click_sort_by_latest(self):
        self.page.get_by_role(
            "link",
            name="למיין לפי המעודכן ביותר"
        ).click()

    def catalog_title_h1(self):
        return self.page.locator(
            "h1.mf-catalog-title"
        )

    def catalog_title_h2(self):
        return self.page.locator(
            "h2.mf-catalog-title"
        )

    def body_text(self):
        return self.page.locator(
            "body"
        )