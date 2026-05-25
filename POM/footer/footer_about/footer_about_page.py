from pages.common.base_page import BasePage


class FooterAboutPage(BasePage):

    def scroll_to_footer(self):
        self.page.evaluate(
            "window.scrollTo(0, document.body.scrollHeight)"
        )

    def footer_is_visible(self):
        return self.page.locator(".site-footer")

    def click_footer_about_us_page(self):
        self.page.locator(
            'a[href="https://musicgate.co.il/about-us"]'
        ).click()